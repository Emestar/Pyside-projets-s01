import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt6.QtGui import QIcon

class MyApp (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hell App')
        self.setWindowIcon(QIcon('maps.ico'))
        self.resize(500, 350) # Width, Height

        layout = QVBoxLayout()
        self.setLayout(layout)

        # widgets
        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello', clicked=self.say_hello)
        # button.clicked.connect(self.say_hello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def say_hello(self):
        inputText = self.inputField.text()
        self.output.setText('Hello, {0}!'.format(inputText.title()))
        

# app = QApplication([])
app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 25px
    }
    QButton {
        font-size: 20px
    }
''')

window = MyApp()
window.show()


app.exec()
