import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class CreditPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Credit Page')

        # Create a main widget and set it as the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        layout = QVBoxLayout(central_widget)

        # Add labels for each credit item
        credits = [
            'Design, Programming: AmirHusein HedayatPour ToupKanlou',
            'GitHub: https://github.com/YourGitHubUsername'
        ]
        for credit in credits:
            label = QLabel(credit, self)
            layout.addWidget(label)
