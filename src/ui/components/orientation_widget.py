"""
Widget for managing screen orientation with toggle functionality.
"""

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, QTimer, QRectF
from PySide6.QtGui import QTransform
from src.config.settings import Theme

class OrientationWidget(QGraphicsView):
    """Widget that manages screen orientation and provides toggle functionality."""
    
    def __init__(self, widget: QWidget):
        super().__init__()
        self.original_widget = widget
        self.is_rotated = False
        
        self._setup_view()
        self._setup_scene()
        self._setup_toggle_button()
        
    def _setup_view(self):
        """Configure the graphics view."""
        self.setFrameShape(self.NoFrame)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet(f"background-color: {Theme.BACKGROUND};")
        
    def _setup_scene(self):
        """Setup the graphics scene and proxy widget."""
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        self.proxy = QGraphicsProxyWidget()
        self.proxy.setWidget(self.original_widget)
        self.scene.addItem(self.proxy)
        
    def _setup_toggle_button(self):
        """Create and position the orientation toggle button."""
        self.toggle_button = QPushButton("↻")
        self.toggle_button.setFixedSize(50, 50)
        self.toggle_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {Theme.PRIMARY};
                color: {Theme.TEXT};
                border: none;
                border-radius: 25px;
                font-size: 20px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {Theme.PRIMARY_HOVER};
            }}
        """)
        self.toggle_button.setCursor(Qt.PointingHandCursor)
        self.toggle_button.clicked.connect(self.toggle_orientation)
        
        # Position button in top-right corner
        self.toggle_button.setParent(self)
        self.toggle_button.move(self.width() - 60, 10)
        
    def toggle_orientation(self):
        """Toggle between portrait and landscape orientation."""
        if self.is_rotated:
            self.reset_rotation()
        else:
            self.apply_rotation()
            
    def apply_rotation(self):
        """Apply 90-degree rotation."""
        self.proxy.setTransformOriginPoint(self.proxy.boundingRect().center())
        
        # Animate rotation
        self._animate_rotation(0, 90)
        self.is_rotated = True
        
    def reset_rotation(self):
        """Reset rotation to normal."""
        self.proxy.setTransformOriginPoint(self.proxy.boundingRect().center())
        
        # Animate rotation back
        self._animate_rotation(90, 0)
        self.is_rotated = False
        
    def _animate_rotation(self, start_angle: int, end_angle: int):
        """Animate rotation from start to end angle."""
        steps = 15
        step_delay = 20  # milliseconds
        angle_step = (end_angle - start_angle) / steps
        
        current_angle = start_angle
        for i in range(steps + 1):
            QTimer.singleShot(i * step_delay, lambda a=current_angle: self._set_rotation(a))
            current_angle += angle_step
            
    def _set_rotation(self, angle: float):
        """Set the rotation angle."""
        transform = QTransform()
        transform.rotate(angle)
        self.proxy.setTransform(transform)
        
    def resizeEvent(self, event):
        """Handle resize events and update button position."""
        super().resizeEvent(event)
        self.toggle_button.move(self.width() - 60, 10)
        self.fitInView(self.proxy, Qt.KeepAspectRatio)
        
    def showEvent(self, event):
        """Handle show events."""
        super().showEvent(event)
        self.fitInView(self.proxy, Qt.KeepAspectRatio)
