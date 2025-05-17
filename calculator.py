import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout,
                             QPushButton, QLineEdit)
from PyQt5.QtCore import Qt

class Program(QWidget):
    def __init__(self):
        super().__init__()

        self.main_line = QLineEdit("0", self)

        self.button_clear = QPushButton("C", self, clicked=lambda:self.button_click("C"))
        self.button_nine = QPushButton("9", self, clicked=lambda:self.button_click("9"))
        self.button_eight = QPushButton("8", self, clicked=lambda:self.button_click("8"))
        self.button_seven = QPushButton("7", self, clicked=lambda:self.button_click("7"))
        self.button_six = QPushButton("6", self, clicked=lambda:self.button_click("6"))
        self.button_five = QPushButton("5", self, clicked=lambda:self.button_click("5"))
        self.button_four = QPushButton("4", self, clicked=lambda:self.button_click("4"))
        self.button_three = QPushButton("3", self, clicked=lambda:self.button_click("3"))
        self.button_two = QPushButton("2", self, clicked=lambda:self.button_click("2"))
        self.button_one = QPushButton("1", self, clicked=lambda:self.button_click("1"))
        self.button_zero = QPushButton("0", self, clicked=lambda:self.button_click("0"))

        self.button_plus = QPushButton("+", self, clicked=lambda:self.button_click("+"))
        self.button_minus = QPushButton("-", self, clicked=lambda:self.button_click("-"))
        self.button_mult = QPushButton("*", self, clicked=lambda:self.button_click("*"))
        self.button_div = QPushButton("/", self, clicked=lambda:self.button_click("/"))
        self.button_calculate = QPushButton("=", self, clicked=lambda:self.button_click("="))

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(300, 400)

        self.main_line.setReadOnly(True)

        grid = QGridLayout()

        grid.addWidget(self.main_line,          0, 0, 1, 4)

        grid.addWidget(self.button_clear,       1, 0, 1, 3)
        grid.addWidget(self.button_nine,        2, 2, 1, 1)
        grid.addWidget(self.button_eight,       2, 1, 1, 1)
        grid.addWidget(self.button_seven,       2, 0, 1, 1)
        grid.addWidget(self.button_six,         3, 2, 1, 1)
        grid.addWidget(self.button_five,        3, 1, 1, 1)
        grid.addWidget(self.button_four,        3, 0, 1, 1)
        grid.addWidget(self.button_three,       4, 2, 1, 1)
        grid.addWidget(self.button_two,         4, 1, 1, 1)
        grid.addWidget(self.button_one,         4, 0, 1, 1)
        grid.addWidget(self.button_zero,        5, 0, 1, 3)

        grid.addWidget(self.button_calculate,   1, 3, 1, 1)
        grid.addWidget(self.button_plus,        2, 3, 1, 1)
        grid.addWidget(self.button_minus,       3, 3, 1, 1)
        grid.addWidget(self.button_div,         4, 3, 1, 1)
        grid.addWidget(self.button_mult,        5, 3, 1, 1)

        self.setLayout(grid)

        self.main_line.setAlignment(Qt.AlignRight)

        self.setStyleSheet("""
            QPushButton, QTextEdit, QLineEdit, QLabel{
                font-family: bahnschrift;
                padding: 5px;
            }
            QLineEdit{
                font-size: 40px;
            }
            QTextEdit{
                font-size: 16px;
                padding: 0px;
            }
            QPushButton{
                font-size: 40px;
                font-weight: bold;
            }
            QPushButton#history_clear{
                font-size: 20px;
                font-weight: bold; 
            }
            QLabel{
                font-size: 24px;
                font-style: italic;
            }
        """)

    def set_line_text(self, var):
        if type(var) is float:
            self.main_line.setText(f"{var:.2f}")
        else:
            self.main_line.setText(f"{var}")

    def button_click(self, pressed):
        match pressed:
            case "CLR_HSTR": self.history_display.clear()
            case "C": self.main_line.setText("0")
            case _: self.line_logic(pressed)

    def line_logic(self, action):
        operators = "+-*/"

        if action != "=":
            if self.main_line.text() == "0":
                if action in operators:
                    pass
                else:
                    self.main_line.clear()

            if action in operators and self.main_line.text()[-1] in operators:
                pass
            else:
                self.main_line.setText(f"{self.main_line.text()}{action}")
        else:
            if self.main_line.text()[-1] in operators:
                line_contents = self.main_line.text()
                result = eval(str(line_contents[:-1]))

                self.set_line_text(result)
            else:
                line_contents = self.main_line.text()
                result = eval(line_contents)

                self.set_line_text(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    program = Program()

    program.show()
    sys.exit(app.exec_())

