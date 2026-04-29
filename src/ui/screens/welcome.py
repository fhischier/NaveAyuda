"""
Welcome screen with app introduction and start functionality.
"""

from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QFont
from src.ui.components.buttons import PrimaryButton, IconButton
from src.ui.components.labels import TitleLabel, InfoLabel
from src.config.settings import Theme, UIConfig, AppConfig
from src.utils.helpers import get_asset_path

class WelcomeScreen(QWidget):
    """Welcome screen with app title and start button."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
        self._setup_animation()
        
    def _setup_ui(self):
        """Setup the welcome screen UI."""
        self.setStyleSheet(f"background-color: {Theme.BACKGROUND};")
        
        # Main layout
        layout = QVBoxLayout(self)
        layout.setSpacing(UIConfig.SECTION_SPACING)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignCenter)
        
        # Top bar with close button
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        
        close_button = IconButton("×", 50)
        close_button.clicked.connect(self.close)
        top_bar.addWidget(close_button)
        
        layout.addLayout(top_bar)
        
        # Logo Clamers
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        # Cargar y escalar el logo
        logo_path = get_asset_path("Logo_Clamers_Blanco.png")
        pixmap = QPixmap(logo_path)
        if not pixmap.isNull():
            # Escalar logo manteniendo aspect ratio
            scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.logo_label.setPixmap(scaled_pixmap)
        else:
            # Fallback si no se encuentra el logo
            self.logo_label.setText("🦐 CLAMERS")
            self.logo_label.setStyleSheet(f"""
                QLabel {{
                    color: {Theme.TEXT};
                    font-size: 48px;
                    font-weight: bold;
                    padding: 20px;
                }}
            """)
        
        layout.addWidget(self.logo_label)
        
        # App title
        title = TitleLabel("TRIVIA CLAMERS")
        layout.addWidget(title)
        
        # Subtitle
        subtitle = InfoLabel("Responde las preguntas y pon a prueba tus conocimientos")
        layout.addWidget(subtitle)
        
        # Start button
        self.start_button = PrimaryButton("COMENZAR")
        self.start_button.clicked.connect(self.start_survey)
        layout.addWidget(self.start_button)
        
        # Instructions
        instructions = InfoLabel("🎯 Responde correctamente y pon a prueba tus conocimientos")
        layout.addWidget(instructions)
        
        layout.addStretch()
        
    def _setup_animation(self):
        """Setup subtle animation for the logo and start button."""
        self.animation_timer = QTimer()
        self.animation_step = 0
        self.animation_direction = 1
        self.logo_y = 0
        self.logo_direction = 1
        self.animation_timer.timeout.connect(self._animate_elements)
        self.animation_timer.start(AppConfig.ANIMATION_SPEED * 3)
        
    def _animate_elements(self):
        """Animate the logo and start button with subtle effects."""
        # Animate logo floating effect
        self.logo_y += self.logo_direction
        if abs(self.logo_y) > 10:
            self.logo_direction *= -1
        self.logo_label.move(self.logo_label.x(), self.logo_y)
        
        # Animate button pulse effect
        self.animation_step += self.animation_direction
        if abs(self.animation_step) > 5:
            self.animation_direction *= -1
        
    def start_survey(self):
        """Signal to start the survey."""
        if hasattr(self.parent(), 'show_survey'):
            self.parent().show_survey()
        else:
            # Fallback for standalone usage
            from PySide6.QtWidgets import QApplication
            QApplication.quit()
