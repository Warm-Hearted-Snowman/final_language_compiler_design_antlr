import sys
from PyQt5.QtCore import QProcess, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton

class TerminalWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Terminal")

        self.terminal_process = QProcess(self)
        self.terminal_process.readyReadStandardOutput.connect(self.update_terminal)

        self.terminal_output = QTextEdit(self)
        self.terminal_output.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.terminal_output)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.start_terminal()

    def start_terminal(self):
        self.terminal_process.start('konsole', ['-e', 'bash', '-c', 'echo "Hello, Terminal!"; bash'])
        self.terminal_output.clear()

    def update_terminal(self):
        cursor = self.terminal_output.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(self.terminal_process.readAllStandardOutput().data().decode())
        self.terminal_output.ensureCursorVisible()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TerminalWindow()
    window.show()
    sys.exit(app.exec_())
