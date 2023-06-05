import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

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
            'GitHub: <a href="https://github.com/Warm-Hearted-Snowman">https://github.com/Warm-Hearted-Snowman</a>'
        ]
        for credit in credits:
            label = QLabel(self)
            label.setOpenExternalLinks(True)  # Enable opening links externally
            label.setTextFormat(Qt.RichText)  # Set text format to support HTML
            label.setText(credit)
            layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreditPage()
    window.show()
    sys.exit(app.exec_())
