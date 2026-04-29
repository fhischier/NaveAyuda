# Survey Application

A clean, professional survey application built with PySide6 that provides an engaging user experience with modern UI design and smooth interactions.

## Features

- **Modern UI Design**: Clean, minimal interface with professional styling
- **Responsive Layout**: Adapts to different screen sizes
- **Screen Orientation Toggle**: Dynamic rotation with smooth animations
- **Question Management**: Structured survey system with multiple choice questions
- **Real-time Feedback**: Immediate visual feedback for correct/incorrect answers
- **Progress Tracking**: Visual progress indicators
- **Results Analysis**: Detailed score display with performance messages
- **Modular Architecture**: Clean separation of concerns for maintainability

## Project Structure

```
NaveAyuda/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── src/
│   ├── app.py             # Main application class
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py    # Configuration and theme settings
│   ├── data/
│   │   ├── __init__.py
│   │   └── questions.py   # Sample survey questions
│   ├── models/
│   │   ├── __init__.py
│   │   └── survey.py      # Data models for questions and sessions
│   ├── ui/
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   ├── buttons.py     # Custom button components
│   │   │   ├── labels.py      # Custom label components
│   │   │   └── orientation_widget.py  # Screen rotation widget
│   │   ├── screens/
│   │   │   ├── __init__.py
│   │   │   ├── welcome.py     # Welcome screen
│   │   │   ├── survey.py      # Main survey screen
│   │   │   └── results.py     # Results screen
│   │   └── __init__.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py     # Utility functions
└── assets/                # Static assets (images, etc.)
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd NaveAyuda
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Controls

- **Start Survey**: Click "COMENZAR" on the welcome screen
- **Answer Questions**: Select an option to submit your answer
- **Rotate Screen**: Use the ↻ button in the top-right corner to toggle orientation
- **Navigate**: Use arrow buttons to go back to previous screens
- **View Results**: After completing all questions, view your score and accuracy

## Architecture

The application follows a clean, modular architecture:

- **Models**: Data structures for questions, surveys, and user sessions
- **Views**: UI screens and components with clear separation of concerns
- **Controllers**: Application logic and screen management
- **Configuration**: Centralized settings and theming
- **Utilities**: Helper functions for common operations

## Customization

### Adding Questions

Edit `src/data/questions.py` to add or modify survey questions:

```python
Question(
    text="Your question here?",
    options=["Option A", "Option B", "Option C"],
    correct_index=0  # Index of correct answer
)
```

### Theme Customization

Modify colors and styling in `src/config/settings.py`:

```python
class Theme:
    BACKGROUND = "#0f172a"
    PRIMARY = "#2563eb"
    # ... other colors
```

## Requirements

- Python 3.8+
- PySide6 6.6.0

## License

This project is provided as-is for educational and demonstration purposes.
