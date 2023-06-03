from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextBrowser, QPlainTextEdit


class user_input_window(QWidget):
    def __init__(self, variable, type):
        super().__init__()

        self.user_input = None
        layout = QVBoxLayout()

        # Create the line edit widget
        self.line_edit = QPlainTextEdit()
        self.line_edit.setFixedSize(250, 50)
        layout.addWidget(self.line_edit)

        # Create the button widget
        button = QPushButton('Enter')
        button.clicked.connect(self.handle_input)
        button.setFixedSize(250, 50)
        layout.addWidget(button)
        layout.addStretch()
        layout.setContentsMargins(20, 20, 20, 20)  # Set the padding for the buttons


        self.setWindowTitle(f"read({type}, {variable})")
        self.setFixedSize(300, 150)
        self.setLayout(layout)

    def handle_input(self):
        self.user_input = self.line_edit.toPlainText()
        self.close()
        return self.user_input
