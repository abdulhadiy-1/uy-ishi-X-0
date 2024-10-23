from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(220, 300)

        self.v_main_lay = QVBoxLayout()
        self.grid_lay = QGridLayout()
        self.h_btn_lay = QHBoxLayout()
        self.count = 1
        self.btn1 = QPushButton("", clicked=lambda: self.Btn(self.btn1))
        self.btn2 = QPushButton("", clicked=lambda: self.Btn(self.btn2))
        self.btn3 = QPushButton("", clicked=lambda: self.Btn(self.btn3))
        self.btn4 = QPushButton("", clicked=lambda: self.Btn(self.btn4))
        self.btn5 = QPushButton("", clicked=lambda: self.Btn(self.btn5))
        self.btn6 = QPushButton("", clicked=lambda: self.Btn(self.btn6))
        self.btn7 = QPushButton("", clicked=lambda: self.Btn(self.btn7))
        self.btn8 = QPushButton("", clicked=lambda: self.Btn(self.btn8))
        self.btn9 = QPushButton("", clicked=lambda: self.Btn(self.btn9))

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6,
                    self.btn7, self.btn8, self.btn9]

        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.Start)

        self.finish_btn = QPushButton("Finish")
        self.finish_btn.hide()
        self.finish_btn.clicked.connect(self.Finish)

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(exit)

        index = 0

        for i in range(3):
            for j in range(3):
                self.lst[index].setFixedSize(50, 50)
                self.lst[index].setStyleSheet("font-size:40px; padding: 0px")
                self.lst[index].setEnabled(False)
                self.grid_lay.addWidget(self.lst[index], i, j)
                index += 1

        self.h_btn_lay.addWidget(self.start_btn)
        self.h_btn_lay.addWidget(self.finish_btn)
        self.h_btn_lay.addWidget(self.exit_btn)
        self.lbl = QLabel("")
        self.lbl.setStyleSheet("font-size: 20px")
        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Start(self):
        self.start_btn.hide()
        self.finish_btn.show()
        for i in self.lst:
            i.setEnabled(True)
            i.setText("")
        self.count = 1
        self.lbl.setText("")

    def Finish(self):
        self.finish_btn.hide()
        self.start_btn.show()
        for i in self.lst:
            i.setEnabled(False)

        for i in range(9):
            self.lst[i].setText("")

    def Btn(self, btn):
        if btn.text() == "" and self.count % 2 == 0:
            btn.setText("o")
        elif btn.text() == "" and self.count % 2 != 0:
            btn.setText("x")
        self.count += 1

        self.Check()

    def Check(self):
        board = [btn.text() for btn in self.lst]

        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                          (0, 4, 8), (2, 4, 6)]             

        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "":
                self.lbl.setText(f"{board[condition[0]]} -> Win")
                for btn in self.lst:
                    btn.setEnabled(False)
                return

        if all(btn.text() != "" for btn in self.lst):
            self.lbl.setText("Draw")
            for btn in self.lst:
                btn.setEnabled(False)


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
