"""
Custom label components for the survey application.
"""

from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from src.config.settings import Theme, UIConfig

class TitleLabel(QLabel):
    """Title label with modern styling."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply title styling."""
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                color: {Theme.TEXT};
                font-size: {UIConfig.TITLE_FONT_SIZE}px;
                font-weight: 900;
                padding: {UIConfig.CARD_PADDING}px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {Theme.SURFACE}, stop:1 {Theme.PRIMARY});
                border: 2px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                margin: 10px;
            }}
        """)
        self.setWordWrap(True)

class QuestionLabel(QLabel):
    """Question label with card design."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply question styling."""
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                color: {Theme.TEXT};
                font-size: {UIConfig.QUESTION_FONT_SIZE}px;
                font-weight: 700;
                padding: {UIConfig.CARD_PADDING}px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.SURFACE}, stop:1 {Theme.BACKGROUND});
                border: 2px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                line-height: 1.5;
                margin: 5px;
            }}
        """)
        self.setWordWrap(True)

class InfoLabel(QLabel):
    """Information label with modern styling."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply info styling."""
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                color: {Theme.PRIMARY_LIGHT};
                font-size: 18px;
                font-weight: 500;
                padding: 15px;
                background: {Theme.SURFACE};
                border: 1px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS // 2}px;
                margin: 5px;
            }}
        """)
        self.setWordWrap(True)

class ScoreLabel(QLabel):
    """Score display label with modern card design."""
    
    def __init__(self, correct: int, incorrect: int, parent=None):
        text = f"✓ Correctas: {correct}\n✗ Incorrectas: {incorrect}"
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply score styling."""
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                color: {Theme.TEXT};
                font-size: 32px;
                font-weight: 800;
                padding: {UIConfig.CARD_PADDING}px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 {Theme.SURFACE}, stop:0.5 {Theme.PRIMARY}, stop:1 {Theme.SURFACE});
                border: 3px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                line-height: 1.8;
                margin: 10px;
            }}
        """)
        self.setWordWrap(True)

class ProgressLabel(QLabel):
    """Progress indicator label with modern design."""
    
    def __init__(self, current: int, total: int, parent=None):
        text = f"📍 Pregunta {current} de {total}"
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply progress styling."""
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                color: {Theme.PRIMARY_LIGHT};
                font-size: 16px;
                font-weight: 600;
                padding: 12px 20px;
                background: {Theme.SURFACE};
                border: 2px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                margin: 5px;
            }}
        """)
    
    def update_progress(self, current: int, total: int):
        """Update progress text."""
        self.setText(f"📍 Pregunta {current} de {total}")
