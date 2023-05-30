import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox, QHBoxLayout, \
    QMainWindow, QPlainTextEdit, QTextBrowser
import os
# Import necessary modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle("Compiler Design Project")

        # Create the text area widget
        self.text_edit = QTextBrowser(self)


        # Create a vertical layout for the buttons
        button_layout = QVBoxLayout()
        for i in range(1, 11):
            btn = QPushButton(f"Source Code {i}")
            btn.clicked.connect(lambda _, x=i: self.show_source_code(x))
            button_layout.addWidget(btn)

        button_layout.addStretch()
        button_layout.setContentsMargins(20, 200, 20, 20)  # Set the padding for the buttons

        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run_code)
        button_layout.addWidget(self.run_button)
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        button_layout.addWidget(exit_button)


        # Create a horizontal layout to hold the text area and buttons
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.text_edit)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the size ratio of the text area and buttons
        main_layout.setStretch(0, 6)
        main_layout.setStretch(1, 1)

        # Create a central widget to hold the main layout
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)


    def show_source_code(self, code_num):
        source_code = f"Source Code {code_num} content goes here."
        self.text_edit.setPlainText(source_code)

    def run_code(self):
        result_window = ResultWindow(self.text_edit.toPlainText())
        result_window.show()


class ResultWindow(QWidget):
    def __init__(self, code):
        super().__init__()
        self.initUI(code)

    def initUI(self, code):
        self.setWindowTitle("Code Execution Result")
        self.layout = QVBoxLayout()

        self.result_text_edit = QTextEdit()
        self.layout.addWidget(self.result_text_edit)

        self.run_code(code)

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

        self.setLayout(self.layout)

    def run_code(self, code):
        # Execute the code here and get the result
        result = f"Execution result of code:\n\n{code}"
        self.result_text_edit.setPlainText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())
