"""
Application configuration settings and theme definitions.
"""

class Theme:
    """Color scheme and styling constants."""
    BACKGROUND = "#1a1a2e"
    SURFACE = "#16213e"
    PRIMARY = "#0f4c75"
    PRIMARY_HOVER = "#3282b8"
    PRIMARY_LIGHT = "#bbe1fa"
    SUCCESS = "#22c55e"
    SUCCESS_LIGHT = "#86efac"
    ERROR = "#ef4444"
    ERROR_LIGHT = "#fca5a5"
    WARNING = "#f59e0b"
    TEXT = "#ffffff"
    TEXT_MUTED = "#94a3b8"
    TEXT_DARK = "#1e293b"
    BORDER = "#334155"
    SHADOW = "rgba(0, 0, 0, 0.3)"
    
class UIConfig:
    """UI configuration constants."""
    WINDOW_WIDTH = 480
    WINDOW_HEIGHT = 750
    BUTTON_MIN_HEIGHT = 80
    BUTTON_PADDING = 20
    QUESTION_FONT_SIZE = 26
    TITLE_FONT_SIZE = 38
    BUTTON_FONT_SIZE = 18
    BORDER_RADIUS = 12
    CARD_PADDING = 25
    SECTION_SPACING = 20
    BUTTON_MIN_WIDTH = 380
    
class AppConfig:
    """Application configuration."""
    APP_NAME = "Survey App"
    VERSION = "1.0.0"
    ANIMATION_SPEED = 16  # milliseconds
    FEEDBACK_DELAY = 1000  # milliseconds
