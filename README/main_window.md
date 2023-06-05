## mainWindow.py

This file contains the implementation of the main window for the Compiler Design project. The main window provides a user interface for interacting with the project functionalities.

### Dependencies

- `sys`: Provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
- `PyQt5.QtWidgets`: Contains classes for creating desktop applications.
- `PyQt5.QtCore`: Provides core non-GUI functionality.
- `QFile`: Represents an I/O device for reading and writing text files.
- `os`: Provides a way of using operating system dependent functionality.
- `InterPreter.FinalLanguageTextEditor`: Represents the final language text editor.
- `UI.sample_codes.SampleCodeWindow`: Represents the window for selecting sample codes.
- `UI.CodeAsYourSelf.CodeAsYourSelf`: Represents the window for custom code input.
- `UI.CreditPage.CreditPage`: Represents the window for displaying credits.

### Class: CompilerWindow

- `__init__(self)`: Initializes the CompilerWindow class.
- `init_ui(self)`: Initializes the user interface of the main window.
- `load_markdown_file(self, file_path)`: Loads a markdown file into the text area widget.
- `interpreter_clicked(self)`: Handles the event when the "Interpreter" button is clicked.
- `sample_codes_btn(self)`: Handles the event when the "Use sample codes" button is clicked.
- `custom_code_btn(self)`: Handles the event when the "Code as Yourself" button is clicked.
- `show_credits(self)`: Handles the event when the "Credits" button is clicked.
- `closeEvent(self, event)`: Overrides the close event of the window.

### Main Function

- `if __name__ == "__main__"`: Checks if the current module is being run as the main script.
- `app = QApplication(sys.argv)`: Creates an application object.
- `window = CompilerWindow()`: Creates an instance of the CompilerWindow class.
- `window.showMaximized()`: Maximizes and shows the main window.
- `sys.exit(app.exec_())`: Executes the application event loop.