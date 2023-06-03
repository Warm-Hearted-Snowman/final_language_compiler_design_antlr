from PyQt5.QtWidgets import QMainWindow, QTextBrowser, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox

from backend.interpreter import run_code


class ResultWindow(QMainWindow):
    def __init__(self, code):
        super().__init__()
        self.init_ui(code)

    def init_ui(self, code):
        self.setWindowTitle("Code Execute Result")
        # Create the text area widget
        self.text_area = QTextBrowser(self)
        try:
            self.text_area.setPlainText("".join(run_code(code)[0]))
        except Exception as e:
            self.show_error(error="Error in your code", additional_information=e)

        exit_button = QPushButton("Back")
        exit_button.clicked.connect(self.close)

        # Create a vertical layout for the buttons
        button_layout = QVBoxLayout()
        button_layout.addWidget(exit_button)
        button_layout.addStretch()
        button_layout.setContentsMargins(20, 300, 20, 20)  # Set the padding for the buttons

        # Create a horizontal layout to hold the text area and buttons
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.text_area)
        main_layout.addLayout(button_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set the size ratio of the text area and buttons
        main_layout.setStretch(0, 7)
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

    def closeEvent(self, event):
        event.accept()