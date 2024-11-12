import codecs
import math
from PyQt5 import QtWidgets
from main import Ui_MainWindow
import sys
import math

class Mywindow(QtWidgets.QMainWindow):
    angle_value = ['30', '45', '60']
    D = ['219', '273', '325', '377',
         '426', '480', '530', '630',
         '720', '820', '920', '1020',
         '1120', '1220', '1320', '1420']
    f = ['1', '0.9', '0.8']
    c = ['1', '2']
    temp = ['20', '100', '150', '200', '250', '300', '350', '375',
            '400', '410', '420', '430', '440', '450', '460', '470',
            '480']
    stal = ["Ст3 (до 20 мм)", "Ст3 (свыше 20 мм)", "09Г2Сб 16ГС (до 32 мм)",
            "09Г2Сб 16ГС (свыше 32 мм)", "20, 20К (до 160 мм)", "10",
            "10 Г2, 09 Г2", "17ГС, 17Г1С, 10Г2С1"
            ]
    dannie = [
        {20: 154, 100: 149, 150: 145, 200: 142, 250: 131, 300: 115, 350: 105,
         375: 93, 400: 85, 410: 81, 420: 75, 430: 71},
        {20: 140, 100: 134, 150: 131, 200: 126, 250: 120, 300: 108, 350: 98,
         375: 93, 400: 85, 410: 81, 420: 75, 430: 71},
        {20: 196, 100: 177, 150: 171, 200: 165, 250: 162, 300: 151, 350: 140,
         375: 133, 400: 122, 410: 104, 420: 92, 430: 86, 440: 78, 450: 71,
         460: 64, 470: 56, 480: 53},
        {20: 183, 100: 160, 150: 154, 200: 148, 250: 145, 300: 134, 350: 123,
         375: 116, 400: 105, 410: 104, 420: 92, 430: 86, 440: 78, 450: 71,
         460: 64, 470: 56, 480: 53},
        {20: 147, 100: 142, 150: 139, 200: 136, 250: 132, 300: 119, 350: 106,
         375: 98, 400: 92, 410: 86, 420: 80, 430: 75, 440: 67, 450: 61,
         460: 55, 470: 49, 480: 46},
        {20: 130, 100: 125, 150: 12, 200: 118, 250: 112, 300: 100, 350: 88,
         375: 82, 400: 77, 410: 75, 420: 72, 430: 68, 440: 60, 450: 53,
         460: 47, 470: 42, 480: 37},
        {20: 180, 100: 160, 150: 154, 200: 148, 250: 145, 300: 134, 350: 123,
         375: 108, 400: 92, 410: 86, 420: 80, 430: 75, 440: 67, 450: 61,
         460: 55, 470: 49, 480: 46},
        {20: 183, 100: 160, 150: 154, 200: 148, 250: 145, 300: 134, 350: 123,
         375: 116, 400: 105, 410: 104, 420: 92, 430: 86, 440: 78, 450: 71,
         460: 64, 470: 56, 480: 53}
    ]
    cos = {30: '0.86602540378', 45: '0.70710678118', 60: '0.5'}

    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.angle.addItems(self.angle_value)
        self.ui.endurance.addItems(self.f)
        self.ui.diameter.addItems(self.D)
        self.ui.increase.addItems(self.c)
        self.ui.temperature.addItems(self.temp)
        self.ui.steel.addItems(self.stal)
        self.ui.rachet_btn.clicked.connect(self.raschet)


    def raschet(self):
        stal_snach = self.stal.index(self.ui.steel.currentText())
        temperatura = int(self.ui.temperature.currentText())
        sigm = self.dannie[stal_snach].get(temperatura)
        alfa = self.cos.get(int(self.ui.angle.currentText()))
        pr = int(self.ui.pressure.text())
        Dk = int(self.ui.diameter.currentText())
        Fir = float(self.ui.endurance.currentText())
        c = float(self.ui.increase.currentText())
        sk = pr*Dk/(2 * sigm * Fir - pr)/float(alfa)
        S = sk + c
        self.ui.vivid.setText(f"Вывод: Необходимая толщина стенки {math.ceil(S)} мм")


app = QtWidgets.QApplication([])
application = Mywindow()
application.show()
sys.exit(app.exec_())

