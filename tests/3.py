from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create the line edit widget
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        # Create the button widget
        button = QPushButton('Submit')
        button.clicked.connect(self.handle_input)
        layout.addWidget(button)

        self.setLayout(layout)

    def handle_input(self):
        user_input = self.line_edit.text()
        return user_input

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
