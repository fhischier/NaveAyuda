"""
Sample survey questions data.
"""

from src.models.survey import Question, Survey

def create_sample_survey() -> Survey:
    """Create a sample survey with questions."""
    questions = [
        Question(
            text="¿Quién es el dueño de Clamers?",
            options=["German", "Ioio", "Nari"],
            correct_index=0
        ),
        Question(
            text="¿Cuánto paga Clamers?",
            options=["Bien", "Poco", "Mucho"],
            correct_index=1
        ),
        Question(
            text="¿Quién es el más gordo?",
            options=["German", "Ioio", "Nari"],
            correct_index=0
        ),
        Question(
            text="¿Cuál es el mejor lenguaje de programación?",
            options=["Python", "JavaScript", "C++"],
            correct_index=0
        ),
        Question(
            text="¿Qué framework es mejor para aplicaciones de escritorio?",
            options=["PyQt", "Tkinter", "PySide"],
            correct_index=2
        )
    ]
    
    return Survey(questions)
