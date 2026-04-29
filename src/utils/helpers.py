"""
Utility helper functions for the application.
"""

import os
import sys
from typing import Optional

def resource_path(relative_path: str) -> str:
    """
    Get absolute path to resource, works for development and for PyInstaller.
    
    Args:
        relative_path: Relative path to the resource
        
    Returns:
        Absolute path to the resource
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        # In development, use the project root directory
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    
    return os.path.join(base_path, relative_path)

def center_widget(widget, parent_widget=None):
    """
    Center a widget relative to its parent or screen.
    
    Args:
        widget: Widget to center
        parent_widget: Parent widget (if None, centers on screen)
    """
    if parent_widget:
        x = (parent_widget.width() - widget.width()) // 2
        y = (parent_widget.height() - widget.height()) // 2
    else:
        from PySide6.QtWidgets import QApplication
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - widget.width()) // 2
        y = (screen.height() - widget.height()) // 2
    
    widget.move(x, y)

def get_asset_path(filename: str) -> str:
    """
    Get path to asset file.
    
    Args:
        filename: Asset filename
        
    Returns:
        Full path to the asset
    """
    return resource_path(os.path.join("assets", filename))

def validate_question_data(question_data: dict) -> bool:
    """
    Validate question data structure.
    
    Args:
        question_data: Dictionary containing question data
        
    Returns:
        True if valid, False otherwise
    """
    required_fields = ['text', 'options', 'correct_index']
    
    if not all(field in question_data for field in required_fields):
        return False
    
    if not isinstance(question_data['options'], list) or len(question_data['options']) < 2:
        return False
    
    correct_index = question_data['correct_index']
    if not isinstance(correct_index, int) or correct_index < 0 or correct_index >= len(question_data['options']):
        return False
    
    return True
