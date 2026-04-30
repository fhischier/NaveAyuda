"""
Main application class that manages screens and navigation.
"""

from PySide6.QtWidgets import QApplication, QStackedWidget
from PySide6.QtCore import QSize
from src.ui.screens.welcome import WelcomeScreen
from src.ui.screens.survey import SurveyScreen
from src.ui.screens.results import ResultsScreen
from src.models.survey import UserSession
from src.data.questions import create_sample_survey
from src.config.settings import UIConfig, AppConfig

class SurveyApp(QStackedWidget):
    """Main application window managing survey screens."""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(AppConfig.APP_NAME)
        self.setMinimumSize(UIConfig.WINDOW_WIDTH, UIConfig.WINDOW_HEIGHT)
        
        # Initialize data
        self.survey = create_sample_survey()
        self.session = UserSession()
        
        # Setup screens
        self._setup_screens()
        
        # Show welcome screen initially
        self.show_welcome()
        
    def _setup_screens(self):
        """Initialize all screens."""
        # Welcome screen
        self.welcome_screen = WelcomeScreen(self)
        self.addWidget(self.welcome_screen)
        
        # Survey screen
        self.survey_screen = SurveyScreen(self.survey, self.session, self)
        self.addWidget(self.survey_screen)
        
        # Results screen
        self.results_screen = ResultsScreen(self.session, self)
        self.addWidget(self.results_screen)
        
    def show_welcome(self):
        """Show the welcome screen."""
        self.setCurrentWidget(self.welcome_screen)
        
    def show_survey(self):
        """Show the survey screen."""
        # Reset survey and session for new attempt
        self.survey.reset()
        self.session.reset()
        self.survey_screen._load_question()
        self.setCurrentWidget(self.survey_screen)
        
    def show_results(self):
        """Show the results screen with updated data."""
        # Remove old results screen and create new one with current session data
        self.removeWidget(self.results_screen)
        self.results_screen.deleteLater()
        self.results_screen = ResultsScreen(self.session, self)
        self.addWidget(self.results_screen)
        self.setCurrentWidget(self.results_screen)
        
    def retry_survey(self):
        """Restart the same survey."""
        self.survey.reset()
        self.session.reset()
        self.survey_screen._load_question()
        self.setCurrentWidget(self.survey_screen)

def main():
    """Main entry point for the application."""
    import sys
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look
    
    # Create main app
    main_app = SurveyApp()
    
    # Launch in full screen mode
    main_app.showFullScreen()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
