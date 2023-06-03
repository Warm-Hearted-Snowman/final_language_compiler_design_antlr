import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPlainTextEdit, QPushButton, QWidget, QScrollArea, \
    QHBoxLayout
from backend.interpreter import run_code


class FinalLanguageTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_layout = None
        self.variables = {}
        self.input_block_counter = 0
        self.result_block_counter = 0
        self.initUI()

    def initUI(self):
        # Create the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create the main layout for the central widget
        self.main_layout = QVBoxLayout(central_widget)

        # Create a scroll area to contain the text editors
        scroll_area = QScrollArea(self)
        self.main_layout.addWidget(scroll_area)

        # Create a widget to hold the blocks vertically
        self.blocks_container = QWidget(self)
        self.blocks_layout = QVBoxLayout(self.blocks_container)
        self.blocks_container.setLayout(self.blocks_layout)

        # Set the widget as the content of the scroll area
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.blocks_container)

        self.input_editor = QPlainTextEdit(self)
        self.input_editor.setStyleSheet("color: green;")
        self.blocks_layout.addWidget(self.input_editor)
        self.input_editor.setFocus()

        # Create the Send Data button
        send_button = QPushButton('Run', self)
        send_button.clicked.connect(self.sendData)
        send_button.setFixedWidth(100)

        close_button = QPushButton('Close', self)
        close_button.clicked.connect(self.closeWindow)
        close_button.setFixedWidth(100)

        # Create a container widget for the Send Data button
        button_widget = QWidget(self)
        button_layout = QHBoxLayout(button_widget)
        button_layout.addWidget(send_button)
        button_layout.addWidget(close_button)
        button_layout.setAlignment(Qt.AlignRight)
        # button_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)

        # Add the button container widget to the main layout
        self.main_layout.addWidget(button_widget)

        # Set the main window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('JupyterLab Text Editor')

        # Initialize the result editor
        self.result_editor = None

    def keyPressEvent(self, event):
        # Handle key press event for Enter key
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.sendData()

    def sendData(self):
        # Retrieve the text from the input editor
        text = self.input_editor.toPlainText()

        if text.strip() == '':
            return
        # Process the data
        processed_data = self.processData(text)

        if isinstance(processed_data, list):
            result = "".join(processed_data)
        else:
            result = "Error: " + str(processed_data)
        # Create a new result editor for the processed data
        self.createResultEditor(result)

        # Create a new input block
        self.input_editor.clear()
        self.input_editor.setFocus()

    def createResultEditor(self, text):
        # Create the result editor widget
        result_block_number = str(self.result_block_counter)
        self.result_block_counter += 1

        self.result_editor = QPlainTextEdit(self)
        self.result_editor.setPlainText(f"[{result_block_number}] {text}")
        self.result_editor.setReadOnly(True)
        self.result_editor.setStyleSheet("color: red; font-weight: bold;")
        self.blocks_layout.addWidget(self.result_editor)

        # Create a new input block
        input_block_number = str(self.input_block_counter)
        self.input_block_counter += 1
        self.input_editor = QPlainTextEdit(self)
        self.input_editor.setPlainText(f"[{input_block_number}] ")
        self.input_editor.setStyleSheet("color: green;")
        self.blocks_layout.addWidget(self.input_editor)

    def closeWindow(self):
        self.close()

    def processData(self, text):
        try:
            run = run_code(text, self.variables)
            self.variables = run[1]
            return run[0]
        except Exception as e:
            return e


def main():
    app = QApplication(sys.argv)
    window = FinalLanguageTextEditor()
    window.show()
    sys.exit(app.exec_())
