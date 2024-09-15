from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit, 
                               QMainWindow, QPushButton, QTextBrowser, QVBoxLayout, QWidget)
import sys
from main_window import Gemini

class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.gemini = Gemini()

        # output area 
        self.ai_output_box = QTextBrowser()

        # enter text widget 
        user_message_widget = QWidget()
        user_message_widget.setContentsMargins(0, 0, 0, 0)
        # user_label = QLabel("Test")
        self.user_input = QLineEdit() # user input 
        self.user_input.returnPressed.connect(lambda: self.give_text_to_gemini(self.user_input.text())) # CONNECT TO API SEND FUNCTION 
        # self.enter_input_btn = QPushButton("SEND")
        user_message_layout = QGridLayout()
        user_message_layout.setContentsMargins(0, 0, 0, 0)
        # user_message_layout.addWidget(user_label, 0, 0)
        user_message_layout.addWidget(self.user_input, 0, 0)
        # user_message_layout.addWidget(self.enter_input_btn, 0, 1)
        user_message_widget.setLayout(user_message_layout)

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.ai_output_box)
        main_layout.addWidget(user_message_widget)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def give_text_to_gemini(self, text):
        text = self.gemini.text_prompt(text)
        self.print_text_to_box(text)

    def print_text_to_box(self, text):
        self.ai_output_box.append(text+"\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet("QLabel{font-size: 11pt;}") # increase font size slightly of QLabels

    main_window = MainApp()
    main_window.setWindowTitle("Interface Testing")
    # tab_dialog.setFixedSize(False)
    # tab_dialog.setMaximumSize()
    # tab_dialog.setFixedSize(700, 500)
    # main_window.resize(800, 600)
    # QTimer.singleShot(1000, self.showMaximized())
    # main_window.showMaximized() # full screen 
    main_window.show()
    
    # tab_dialog.raise_() # look up what this does

    sys.exit(app.exec())
        

    


