import sys
from math import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QPushButton
import speech_recognition as sr 
import webbrowser
from PyQt5 import QtGui, QtWidgets
r = sr.Recognizer()


class AudioTimer(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Start', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.doAction)
        self.setGeometry(200, 300, 240, 70)
        self.setWindowTitle('Ask Yandex')

    def doAction(self):     
        self.btn.setText('Speak')
        
        try:         
            with sr.Microphone() as source: 
                audio = r.listen(source)
                result = r.recognize_google(audio,language="ru_RU")
            webbrowser.open_new(ask + result) 
        except sr.UnknownValueError: 
            pass 
        except sr.RequestError as e: 
            pass
        self.btn.setText('Start')
        


def fobrabotka(stroka):
    b = stroka
    b = b.replace('^', '**')
    b = b.replace(' ', '')
    b = b.replace('√', 'sqrt')
    b = b.replace(')(', ')*(')
    while True:
        k = 0
        for i in range(len(b)):
            k1 = 0
            if (b[i:i + 4] == 'sin(' and b[i:i + 7] != 'sin(rad') or \
               (b[i:i + 4] == 'cos(' and b[i:i + 7] != 'cos(rad') or \
               (b[i:i + 4] == 'tan(' and b[i:i + 7] != 'tan(rad'):
                kol = 0
                for j in range(i + 4, len(b)):
                    if b[j] == '(':
                        kol += 1
                    elif b[j] == ')':
                        kol -= 1
                    if kol < 0:
                        b = b[:i + 4] + 'radians(' + b[i + 4:j + 1] \
                                      + ')' + b[j + 1:]
                        k = 1
                        k1 = 1
                        break
            if k1 == 1:
                break
        if k == 0:
            break
    return b


class MyWidget(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('kalkulator.ui',self)
        self.stroka = '_' * 81
        self.flag = 0
        self.memory = 0
        self.label.setText(self.stroka[-80:]) 
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('kalkulator') 
        self.num1.clicked.connect(self.num)
        self.num2.clicked.connect(self.num)
        self.num3.clicked.connect(self.num)
        self.num4.clicked.connect(self.num)
        self.num5.clicked.connect(self.num)
        self.num6.clicked.connect(self.num)
        self.num7.clicked.connect(self.num)
        self.num8.clicked.connect(self.num)
        self.num9.clicked.connect(self.num)
        self.num0.clicked.connect(self.num)
        self.ravno.clicked.connect(self.res)
        self.sbros.clicked.connect(self.clea)
        self.pi.clicked.connect(self.pii)
        self.plus1.clicked.connect(self.plus)
        self.umn.clicked.connect(self.umno)
        self.del1.clicked.connect(self.del11)
        self.okrdel.clicked.connect(self.del22)
        self.minus.clicked.connect(self.minuss)
        self.delete2.clicked.connect(self.dele)
        self.mod1.clicked.connect(self.mod11)
        self.kvadr.clicked.connect(self.kvadr1)
        self.kub.clicked.connect(self.kub1)
        self.stepen.clicked.connect(self.stepen1)      
        self.probel.clicked.connect(self.probell)
        self.cos1.clicked.connect(self.cos11)
        self.sin1.clicked.connect(self.sin11)
        self.tan1.clicked.connect(self.tan11)
        self.skobka1.clicked.connect(self.skobka)
        self.skobka2.clicked.connect(self.skobka)
        self.kor.clicked.connect(self.kore)
        self.EEE.clicked.connect(self.ee)
        self.Mr.clicked.connect(self.mr)
        self.Mminus.clicked.connect(self.mm)
        self.Mplus.clicked.connect(self.mp)
        self.cmem.clicked.connect(self.cmemm)
        self.yagolos.clicked.connect(self.run)
        
    def run(self):
            i, okBtnPressed = QInputDialog.getItem(
                self, 
                "Выберите вариант запроса",
                "Выбирите вариант запроса.",
                ("Микрофон", "Клавиатура"),
                1, False)    
            if okBtnPressed:
                if i == "Клавиатура":
                    j=''
                    j, okBtnPressed = QInputDialog.getItem(self, \
                                        "Запрос", \
                                        "Напишите запрос.", \
                                        ("", ''),\
                                        1,\
                                        True)
                    if okBtnPressed:
                        webbrowser.open_new(ask + j)
                elif i == "Микрофон":
                    eq.show()              
        
    def num(self):
        if self.flag == 0:
            self.stroka = ''
            if self.sender().text() != '0':
                self.flag = 1
        self.stroka += str(self.sender().text())
        self.label.setText(self.stroka[-80:])  
        
    def pii(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += 'pi'
        self.label.setText(self.stroka[-80:])          
    
    def res(self):
        try:
            a1 = str(eval(fobrabotka(self.stroka)))
            self.result1.setText(a1)
            self.stroka = a1
            self.label.setText(self.stroka[-80:]) 
        except Exception:
            self.result1.setText('Хмм... Вы где-то ошиблись')
        
    def clea(self):
        self.stroka = '_' * 81
        self.flag = 0  
        self.label.setText(self.stroka[-80:]) 
        self.result1.setText(str(0))
        
    def plus(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('+')
        self.label.setText(self.stroka[-80:])  
        
    def umno(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('*')
        self.label.setText(self.stroka[-80:]) 
        
    def del11(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('/')
        self.label.setText(self.stroka[-80:])         
        
    def del22(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('//')
        self.label.setText(self.stroka[-80:])     
        
    def minuss(self):
        if self.flag == 0:
            self.flag = 1
            self.stroka = ''
        self.stroka += str('-')
        self.label.setText(self.stroka[-80:])    
        
    def dele(self):
        if self.flag == 0:
            pass
        else:
            self.stroka = self.stroka[:-1]
            if len(self.stroka) == 0:
                self.stroka = '_' * 81
                self.flag = 0
            self.label.setText(self.stroka[-80:])  
            
    def mod11(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('%')
        self.label.setText(self.stroka[-80:])
        
    def kvadr1(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('^2')
        self.label.setText(self.stroka[-80:])
        
    
    def kub1(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('^3')
        self.label.setText(self.stroka[-80:])   
        
    def stepen1(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('^')
        self.label.setText(self.stroka[-80:])    
        
    def probell(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str(' ')
        self.label.setText(self.stroka[-80:])   
        
    def sin11(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str('sin(')
        self.label.setText(self.stroka[-80:])   
    
    def cos11(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str('cos(')
        self.label.setText(self.stroka[-80:])   
        
    def tan11(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str('tan(')
        self.label.setText(self.stroka[-80:])      
        
    def skobka(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(self.sender().text())
        self.label.setText(self.stroka[-80:])    
        
    def kore(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str('√(')
        self.label.setText(self.stroka[-80:])  
    
    def ee(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str('e')
        self.label.setText(self.stroka[-80:]) 
        
    def mr(self):
        if self.flag == 0:
            self.stroka = ''
            if self.memory != 0:
                self.flag = 1
        self.stroka += str(self.memory)
        self.labelmemory.setText(str(self.memory)) 
        self.label.setText(self.stroka[-80:])

    def mm(self):
        try:
            self.memory -= int(self.result1.text())
        except Exception:
            pass
        self.labelmemory.setText(str(self.memory)) 
        
    def mp(self):
        try:
            self.memory += int(self.result1.text()) 
        except Exception:
            pass
        self.labelmemory.setText(str(self.memory)) 
        
    def cmemm(self):
        self.memory = 0
        self.labelmemory.setText(str(self.memory))     


ask = 'https://yandex.ru/search/?lr=6&text='
app = QApplication(sys.argv)
tabs = QtWidgets.QTabWidget()
ex = MyWidget()
eq = AudioTimer()
tabs.setGeometry(200, 200, 600, 670)
tab1 = ex
tabs.addTab(tab1, "Калькулятор")
tab2 = QtWidgets.QWidget()
tabs.addTab(tab2, "Tab 2")
tab3 = QtWidgets.QWidget()
tabs.addTab(tab3, "Tab 3")
tabs.show()
tabs.setCurrentIndex(0)
app.exec_()