"""
Custom button components for the survey application.
"""

from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt
from src.config.settings import Theme, UIConfig

class PrimaryButton(QPushButton):
    """Primary action button with modern styling."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply primary button styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.PRIMARY_HOVER}, stop:1 {Theme.PRIMARY});
                color: {Theme.TEXT};
                border: 2px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                font-size: {UIConfig.BUTTON_FONT_SIZE}px;
                font-weight: bold;
                padding: {UIConfig.BUTTON_PADDING}px;
                min-height: {UIConfig.BUTTON_MIN_HEIGHT}px;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.PRIMARY_LIGHT}, stop:1 {Theme.PRIMARY_HOVER});
                border-color: {Theme.PRIMARY_LIGHT};
                box-shadow: 0px 4px 8px {Theme.SHADOW};
            }}
            QPushButton:pressed {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.PRIMARY}, stop:1 {Theme.PRIMARY});
                border-color: {Theme.PRIMARY};
            }}
            QPushButton:disabled {{
                background: {Theme.SURFACE};
                color: {Theme.TEXT_MUTED};
                border-color: {Theme.BORDER};
            }}
        """)
        self.setCursor(Qt.PointingHandCursor)

class OptionButton(QPushButton):
    """Button for answer options with modern feedback styling."""
    
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self._setup_style()
    
    def _setup_style(self):
        """Apply option button styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {Theme.SURFACE}, stop:1 {Theme.PRIMARY});
                color: {Theme.TEXT};
                border: 2px solid {Theme.BORDER};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                font-size: {UIConfig.BUTTON_FONT_SIZE}px;
                font-weight: 600;
                padding: {UIConfig.BUTTON_PADDING}px;
                min-height: {UIConfig.BUTTON_MIN_HEIGHT}px;
                min-width: {UIConfig.BUTTON_MIN_WIDTH}px;
                text-align: left;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {Theme.PRIMARY}, stop:1 {Theme.PRIMARY_HOVER});
                border-color: {Theme.PRIMARY_LIGHT};
            }}
            QPushButton:disabled {{
                font-weight: bold;
                border: 2px solid transparent;
            }}
        """)
        self.setCursor(Qt.PointingHandCursor)
    
    def set_correct(self):
        """Apply correct answer styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.SUCCESS_LIGHT}, stop:1 {Theme.SUCCESS});
                color: {Theme.TEXT};
                border: 3px solid {Theme.SUCCESS};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                font-size: {UIConfig.BUTTON_FONT_SIZE}px;
                font-weight: bold;
                padding: {UIConfig.BUTTON_PADDING}px;
                min-height: {UIConfig.BUTTON_MIN_HEIGHT}px;
                text-align: left;
            }}
            QPushButton:disabled {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.SUCCESS_LIGHT}, stop:1 {Theme.SUCCESS});
                color: {Theme.TEXT};
                border: 3px solid {Theme.SUCCESS};
            }}
        """)
    
    def set_incorrect(self):
        """Apply incorrect answer styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.ERROR_LIGHT}, stop:1 {Theme.ERROR});
                color: {Theme.TEXT};
                border: 3px solid {Theme.ERROR};
                border-radius: {UIConfig.BORDER_RADIUS}px;
                font-size: {UIConfig.BUTTON_FONT_SIZE}px;
                font-weight: bold;
                padding: {UIConfig.BUTTON_PADDING}px;
                min-height: {UIConfig.BUTTON_MIN_HEIGHT}px;
                min-width: {UIConfig.BUTTON_MIN_WIDTH}px;
                text-align: left;
            }}
            QPushButton:disabled {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.ERROR_LIGHT}, stop:1 {Theme.ERROR});
                color: {Theme.TEXT};
                border: 3px solid {Theme.ERROR};
            }}
        """)
    
    def reset_style(self):
        """Reset button to default styling."""
        self._setup_style()
        self.setEnabled(True)

class IconButton(QPushButton):
    """Modern icon-based button for navigation actions."""
    
    def __init__(self, icon_text: str, size: int = 40, parent=None):
        super().__init__(icon_text, parent)
        self.setFixedSize(size, size)
        self._setup_style()
    
    def _setup_style(self):
        """Apply icon button styling."""
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.SURFACE}, stop:1 {Theme.PRIMARY});
                color: {Theme.TEXT};
                border: 2px solid {Theme.BORDER};
                border-radius: {self.width() // 2}px;
                font-size: {self.width() // 2}px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.PRIMARY}, stop:1 {Theme.PRIMARY_HOVER});
                border-color: {Theme.PRIMARY_LIGHT};
                box-shadow: 0px 2px 4px {Theme.SHADOW};
            }}
            QPushButton:pressed {{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {Theme.PRIMARY}, stop:1 {Theme.PRIMARY});
                border-color: {Theme.PRIMARY};
            }}
        """)
        self.setCursor(Qt.PointingHandCursor)
