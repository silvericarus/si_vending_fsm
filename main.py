import sys
from coin_initialization import CoinInitialization
from input_coin_initialization import InputCoinInitialization
from coin_bank import CoinBank
from assortment import Assortment

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (   
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    )

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SI_Vending_FSM")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLabel,
            QLCDNumber,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]
        
        for widget in widgets:
            layout.addWidget(widget())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
coin_initialization = CoinInitialization()
input_coin_initialization = InputCoinInitialization(0, 0, coin_initialization)
coin_bank = CoinBank()
assortment = Assortment(0, 0, 0, 0, 0, 0, 0, 0)
coin_initialization.insert_coin()
print(input_coin_initialization)

app.exec()