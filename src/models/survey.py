"""
Data models for survey questions and user responses.
"""

from typing import List, Dict, Any

class Question:
    """Represents a single survey question."""
    
    def __init__(self, text: str, options: List[str], correct_index: int):
        self.text = text
        self.options = options
        self.correct_index = correct_index
    
    def is_correct(self, selected_index: int) -> bool:
        """Check if the selected answer is correct."""
        return selected_index == self.correct_index

class Survey:
    """Manages a collection of survey questions."""
    
    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.current_index = 0
    
    def get_current_question(self) -> Question:
        """Get the current question."""
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        raise IndexError("No more questions available")
    
    def has_next_question(self) -> bool:
        """Check if there are more questions."""
        return self.current_index < len(self.questions) - 1
    
    def next_question(self) -> None:
        """Move to the next question."""
        if self.has_next_question():
            self.current_index += 1
        else:
            raise IndexError("No more questions available")
    
    def reset(self) -> None:
        """Reset survey to first question."""
        self.current_index = 0
    
    @property
    def total_questions(self) -> int:
        """Get total number of questions."""
        return len(self.questions)
    
    @property
    def progress(self) -> float:
        """Get progress as percentage (0.0 to 1.0)."""
        if self.total_questions == 0:
            return 0.0
        return (self.current_index + 1) / self.total_questions

class UserSession:
    """Tracks user's answers and progress."""
    
    def __init__(self):
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.answers: List[Dict[str, Any]] = []
    
    def record_answer(self, question: Question, selected_index: int) -> None:
        """Record user's answer to a question."""
        is_correct = question.is_correct(selected_index)
        
        self.answers.append({
            'question': question.text,
            'selected_option': question.options[selected_index],
            'correct_option': question.options[question.correct_index],
            'is_correct': is_correct
        })
        
        if is_correct:
            self.correct_answers += 1
        else:
            self.incorrect_answers += 1
    
    def reset(self) -> None:
        """Reset session data."""
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.answers.clear()
    
    @property
    def total_answered(self) -> int:
        """Get total number of answered questions."""
        return self.correct_answers + self.incorrect_answers
    
    @property
    def accuracy(self) -> float:
        """Get accuracy percentage (0.0 to 1.0)."""
        if self.total_answered == 0:
            return 0.0
        return self.correct_answers / self.total_answered
