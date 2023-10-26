from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout, QRadioButton, QButtonGroup)
from random import shuffle, randint


class Questions():
    def __init__(self, quetion, right_answer, wrong1, wrong2, wrong3):
        self.quetion = quetion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


quetion_list = []
quetion_list.append(
    Questions('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский')) 
quetion_list.append(
    Questions('Какого цвета нет в флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
quetion_list.append(
    Questions('Национыльная хижина Якутов?', 'Ураса', 'Хата', 'Иглу', 'Юрта'))


app = QApplication([])

window = QWidget()
window.setWindowTitle('Taro Card')

button = QPushButton('Ответить')
lb_quetion = QLabel('Самый сложный вопрос в мире')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Варивнт 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Правильно')
lb_Correct = QLabel('Ответ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_quetion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(2)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Questions):
    shuffle(answer)
    lb_quetion.setText(q.quetion)
    lb_quetion.setText(q.right_answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def cheak_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика вопросов\n Всего вопросов: ', window.total, '\n Правельных ответов ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:  
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Статистика вопросов\n Всего вопросов: ', window.total, '\n Правельных ответов ', window.score)
    cur_question = randint(0, len(quetion_list) - 1)
    q = quetion_list[cur_question]
    ask(q)


def click_ok():
    if button.text() == 'Ответить':
        cheak_answer()
    else:
        next_question()



window.setLayout(layout_card)

button.clicked.connect(click_ok)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec_()