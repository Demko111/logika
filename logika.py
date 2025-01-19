from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from random import*

app = QApplication([])

#головне вікно
window = QWidget()
window.setWindowTitle("Обирання переможців")
window.resize(500, 500)
window.move(600, 600)

text = QLabel("Натисніть щоб згенерувати число")
winner = QLabel('?')
button = QPushButton('Натисни мене😏')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
window.setLayout(line)


def show_number():
    number = randint(0, 100)
    winner.setText(str(number))
    text.setText('Загадене число')

button.clicked.connect(show_number)


window.show()
app.exec_()


