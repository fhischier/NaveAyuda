"""
Survey screen with questions and answer options.
"""

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer
from src.ui.components.buttons import OptionButton, IconButton
from src.ui.components.labels import QuestionLabel, ProgressLabel
from src.config.settings import Theme, UIConfig, AppConfig
from src.models.survey import Question, UserSession

class SurveyScreen(QWidget):
    """Main survey screen with questions and answer options."""
    
    def __init__(self, survey, session: UserSession, parent=None):
        super().__init__(parent)
        self.survey = survey
        self.session = session
        self.option_buttons = []
        self._setup_ui()
        self._load_question()
        
    def _setup_ui(self):
        """Setup the survey screen UI."""
        self.setStyleSheet(f"background-color: {Theme.BACKGROUND};")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(UIConfig.SECTION_SPACING)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignTop)
        
        # Top bar with back button and progress
        top_bar = QHBoxLayout()
        
        back_button = IconButton("←", 40)
        back_button.clicked.connect(self.go_back)
        top_bar.addWidget(back_button)
        
        top_bar.addStretch()
        
        # Progress indicator
        current_q = self.survey.current_index + 1
        total_q = self.survey.total_questions
        self.progress_label = ProgressLabel(current_q, total_q)
        top_bar.addWidget(self.progress_label)
        
        layout.addLayout(top_bar)
        
        # Question label
        self.question_label = QuestionLabel("")
        layout.addWidget(self.question_label)
        
        # Option buttons
        self.option_buttons = []
        for i in range(4):  # Support up to 4 options
            button = OptionButton("")
            button.clicked.connect(lambda checked, idx=i: self.select_answer(idx))
            button.hide()  # Hide initially
            layout.addWidget(button)
            self.option_buttons.append(button)
            
        layout.addStretch()
        
    def _load_question(self):
        """Load the current question and options."""
        try:
            question = self.survey.get_current_question()
            self.question_label.setText(question.text)
            
            # Update progress
            current_q = self.survey.current_index + 1
            total_q = self.survey.total_questions
            self.progress_label.update_progress(current_q, total_q)
            
            # Setup option buttons - reset all first
            for button in self.option_buttons:
                button.reset_style()
                button.hide()
            
            # Show and configure buttons for current question
            for i, option in enumerate(question.options):
                if i < len(self.option_buttons):
                    button = self.option_buttons[i]
                    button.setText(option)
                    button.show()
                    button.setEnabled(True)
                    
        except IndexError:
            # No more questions, show results
            self.show_results()
            
    def select_answer(self, selected_index: int):
        """Handle answer selection."""
        try:
            question = self.survey.get_current_question()
            is_correct = question.is_correct(selected_index)
            
            # Record the answer
            self.session.record_answer(question, selected_index)
            
            # Show feedback
            selected_button = self.option_buttons[selected_index]
            if is_correct:
                selected_button.set_correct()
            else:
                selected_button.set_incorrect()
            
            # Disable all buttons
            for button in self.option_buttons:
                if button.isVisible():
                    button.setEnabled(False)
            
            # Auto-advance to next question after delay
            QTimer.singleShot(AppConfig.FEEDBACK_DELAY, self.next_question)
            
        except IndexError:
            pass
            
    def next_question(self):
        """Move to the next question or show results."""
        try:
            self.survey.next_question()
            self._load_question()
        except IndexError:
            self.show_results()
            
    def show_results(self):
        """Show the results screen."""
        if hasattr(self.parent(), 'show_results'):
            self.parent().show_results()
            
    def go_back(self):
        """Return to welcome screen."""
        if hasattr(self.parent(), 'show_welcome'):
            self.parent().show_welcome()
