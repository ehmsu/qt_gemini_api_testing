from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QTextBrowser, QWidget
import sys

class MainApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        user_label = QLabel("Test")
        self.user_input = QLineEdit()
        self.enter_input_btn = QPushButton("SEND")

        main_widget = QWidget()
        main_layout = QGridLayout()
        main_layout.addWidget(user_label, 0, 0)
        main_layout.addWidget(self.user_input, 0, 1)
        main_layout.addWidget(self.enter_input_btn, 0, 2)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

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
        

    


