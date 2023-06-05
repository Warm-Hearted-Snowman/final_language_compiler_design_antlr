import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QHBoxLayout, \
    QMainWindow, QPlainTextEdit, QTextBrowser
import os
from UI.ResultWindow import ResultWindow
# Import necessary modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class CodeAsYourSelf(QMainWindow):
    def __init__(self):
        super().__init__()
        self.result_window = None
        self.sample_source_code = None
        self.main_window = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Compiler Design Project")

        # Create the text area widget
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setFixedSize(700,400)

        # Create a vertical layout for the buttons
        button_layout = QVBoxLayout()
        button_layout.addStretch()
        button_layout.setContentsMargins(20, 100, 20, 20)  # Set the padding for the buttons

        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_code)
        button_layout.addWidget(self.run_button)
        exit_button = QPushButton("Back")
        exit_button.clicked.connect(self.back_button)
        button_layout.addWidget(exit_button)

        # Create a horizontal layout to hold the text area and buttons
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the size ratio of the text area and buttons
        main_layout.setStretch(0, 5)
        main_layout.setStretch(1, 1)

        # Create a central widget to hold the main layout
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def show_error(self, error, additional_information=None):
        # Create a QMessageBox
        msg_box = QMessageBox()

        # Set the icon and the title of the message box
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")

        # Set the text and the detailed text of the message box
        msg_box.setText(f"{error}")
        msg_box.setInformativeText(f"{additional_information}")

        msg_box.exec_()

    def run_code(self):
        code = self.text_edit.toPlainText()
        self.result_window = ResultWindow(code)
        self.result_window.show()
    def back_button(self):
        from UI.mainWindow import CompilerWindow
        if self.main_window is None:
            self.main_window = CompilerWindow()
        self.close()
        self.main_window.showMaximized()
