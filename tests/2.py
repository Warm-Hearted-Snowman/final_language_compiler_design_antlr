import sys
import subprocess
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Terminal")

        self.terminal_output = QTextEdit(self)
        self.terminal_output.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.terminal_output)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.start_terminal()

    def start_terminal(self):
        command = "echo 'Hello, Terminal!'"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        output = output.decode().strip()
        self.terminal_output.setPlainText(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec_())
