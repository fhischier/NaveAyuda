"""
Results screen showing survey completion and scores.
"""

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt
from src.ui.components.buttons import PrimaryButton, IconButton
from src.ui.components.labels import TitleLabel, ScoreLabel, InfoLabel
from src.config.settings import Theme, UIConfig
from src.models.survey import UserSession

class ResultsScreen(QWidget):
    """Results screen showing final scores and statistics."""
    
    def __init__(self, session: UserSession, parent=None):
        super().__init__(parent)
        self.session = session
        self._setup_ui()
        
    def _setup_ui(self):
        """Setup the results screen UI."""
        self.setStyleSheet(f"background-color: {Theme.BACKGROUND};")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(UIConfig.SECTION_SPACING)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        
        # Top bar with back button
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        
        back_button = IconButton("←", 40)
        back_button.clicked.connect(self.go_back)
        top_bar.addWidget(back_button)
        
        layout.addLayout(top_bar)
        
        # Results title
        title = TitleLabel("RESULTADOS")
        layout.addWidget(title)
        
        # Score display
        score_label = ScoreLabel(self.session.correct_answers, self.session.incorrect_answers)
        layout.addWidget(score_label)
        
        # Accuracy percentage
        accuracy_percent = int(self.session.accuracy * 100)
        accuracy_label = InfoLabel(f"Precisión: {accuracy_percent}%")
        accuracy_label.setStyleSheet(f"""
            QLabel {{
                color: {Theme.PRIMARY};
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }}
        """)
        layout.addWidget(accuracy_label)
        
        # Performance message
        message = self._get_performance_message(accuracy_percent)
        message_label = InfoLabel(message)
        layout.addWidget(message_label)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        retry_button = PrimaryButton("REINTENTAR")
        retry_button.clicked.connect(self.retry_survey)
        button_layout.addWidget(retry_button)
        
        new_survey_button = PrimaryButton("NUEVA ENCUESTA")
        new_survey_button.clicked.connect(self.new_survey)
        button_layout.addWidget(new_survey_button)
        
        layout.addLayout(button_layout)
        
        layout.addStretch()
        
    def _get_performance_message(self, accuracy: int) -> str:
        """Get performance message based on accuracy."""
        if accuracy >= 90:
            return "¡Excelente trabajo! 🌟"
        elif accuracy >= 70:
            return "¡Buen trabajo! 👍"
        elif accuracy >= 50:
            return "Puedes mejorar 💪"
        else:
            return "Sigue practicando 📚"
            
    def retry_survey(self):
        """Reset and restart the same survey."""
        if hasattr(self.parent(), 'retry_survey'):
            self.parent().retry_survey()
            
    def new_survey(self):
        """Return to welcome screen for a new survey."""
        if hasattr(self.parent(), 'show_welcome'):
            self.parent().show_welcome()
            
    def go_back(self):
        """Return to welcome screen."""
        if hasattr(self.parent(), 'show_welcome'):
            self.parent().show_welcome()
