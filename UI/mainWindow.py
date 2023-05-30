import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import QFile
import os
from ui import FinalLanguageTextEditor
# Import necessary modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

class CompilerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.final_language_window = None

    def init_ui(self):
        self.setWindowTitle("Compiler Design Project")

        # Create the text area widget
        self.text_area = QTextBrowser(self)
        self.load_markdown_file(f'{BASE_DIR}/README/report.md')

        # Create the buttons
        button1 = QPushButton("Interpreter")
        button1.clicked.connect(self.interpreter_clicked)
        button1.setFixedSize(200, 70)

        button2 = QPushButton("Use sample codes")
        button2.clicked.connect(self.button2_clicked)
        button2.setFixedSize(200, 70)

        button3 = QPushButton("Code as Yourself")
        button3.clicked.connect(self.button3_clicked)
        button3.setFixedSize(200, 70)

        # Create the credit and exit buttons
        credit_button = QPushButton("Credits")
        credit_button.clicked.connect(self.show_credits)
        credit_button.setFixedSize(200, 70)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        exit_button.setFixedSize(200, 70)

        # Create a vertical layout for the buttons
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)
        button_layout.addWidget(credit_button)
        button_layout.addWidget(exit_button)
        button_layout.addStretch()
        button_layout.setContentsMargins(20, 200, 20, 20)  # Set the padding for the buttons

        # Create a horizontal layout to hold the text area and buttons
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.text_area)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the size ratio of the text area and buttons
        main_layout.setStretch(0, 2)
        main_layout.setStretch(1, 1)

        # Create a central widget to hold the main layout
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def load_markdown_file(self, file_path):
        file = QFile(file_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            markdown_text = file.readAll().data().decode('utf-8')
            self.text_area.setMarkdown(markdown_text)
            file.close()

    def interpreter_clicked(self):
        if self.final_language_window is None:
            self.final_language_window = FinalLanguageTextEditor()

        self.final_language_window.show()

    def button2_clicked(self):
        self.text_area.append("Button 2 clicked")

    def button3_clicked(self):
        self.text_area.append("Button 3 clicked")

    def show_credits(self):
        self.text_area.append("Credits: John Doe")

    def closeEvent(self, event):
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CompilerWindow()
    window.showMaximized()
    sys.exit(app.exec_())
