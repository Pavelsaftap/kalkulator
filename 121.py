import sys
import keyboard
from math import *
from PyQt5 import QtGui, QtWidgets
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QInputDialog, QPushButton, QColorDialog
from PyQt5.QtWidgets import QCheckBox, QFileDialog
from PyQt5.QtCore import QSize 
import speech_recognition as sr 
import webbrowser
cithri = '1234567890.'
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
        try:         
            with sr.Microphone() as source: 
                audio = r.listen(source)
                result = r.recognize_google(audio,language="ru_RU")
            webbrowser.open_new(ask + result) 
        except sr.UnknownValueError: 
            pass 
        except sr.RequestError as e: 
            pass
        except Exception:
            pass


def fobrabotka(stroka):
    b = stroka
    b = b.replace('^', '**')
    b = b.replace(' ', '')
    b = b.replace('√', 'sqrt')
    b = b.replace(')(', ')*(')
    b = b.replace("округлить", 'ceil')
    if er.checkskobka.isChecked():
        if b.count('(') > b.count(')'):
            b += (b.count('(') - b.count(')')) * ')'
    if len(b) >= 2 and b[0] == '0' and b[1] != '.':
            b = b[1:]
    if er.checsin.isChecked() == False:
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


def cleaner(stroka):
    b = stroka
    while True:
        k = 0
        for i in range(1, len(b) - 1):
            if b[i] == '0':
                if b[i - 1] not in cithri and b[i + 1] in cithri[:-1]:
                    b = b[:i] + b[i+1:]
                    k = 1
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
        self.setWindowTitle('kalkulator') 
        self.label.setText(self.stroka[-80:]) 
        self.initUI()
        
    def initUI(self):
        self.to4ka.clicked.connect(self.to4kaf)
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
        self.del1.clicked.connect(self.del_true)
        self.okrdel.clicked.connect(self.del_floor)
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
        self.ceil1.clicked.connect(self.ceil2)
        
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
        
    def to4kaf(self):
        if self.flag == 0 and self.stroka != '0':
            pass
        else:
            self.flag = 1
            self.stroka += '.'
            self.label.setText(self.stroka[-80:])     
    
    def num(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        if len(self.stroka) >= 2 and self.stroka[0] == '0' \
           and self.stroka[1] in cithri[:-1]:
            self.stroka = self.stroka[1:]
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
            a1 = str(eval(fobrabotka(cleaner(self.stroka))))
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
        
    def del_true(self):
        if self.flag == 0:
            pass
        else:
            self.stroka += str('/')
        self.label.setText(self.stroka[-80:])         
        
    def del_floor (self):
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
    
    def ceil2(self):
        if self.flag == 0:
            pass
        else:
            self.stroka = "округлить" + '(' + self.stroka + ')'
            self.label.setText(self.stroka[-80:])     

    def mm(self):
        try:
            self.memory -= float(self.result1.text())
        except Exception:
            pass
        self.labelmemory.setText(str(self.memory)) 
        
    def mp(self):
        try:
            self.memory += float(self.result1.text()) 
        except Exception:
            pass
        self.labelmemory.setText(str(self.memory)) 
        
    def cmemm(self):
        self.memory = 0
        self.labelmemory.setText(str(self.memory))    
        
    def keyPressEvent(self, e):
        number = int(e.key())
        if number >= 48 and number <= 57:
            number -= 48
            if self.flag == 0:
                self.stroka = ''
                if number != 0:
                    self.flag = 1
            self.stroka += str(number)
            self.label.setText(self.stroka[-80:]) 
        elif number == 16777219:
            self.dele()
        elif number == 61 or number == 16777221 or number == 16777220:
            self.res()
        elif number == 45:
            self.minuss()    
        elif number == 42:
            self.umno()
        elif number == 67:
            self.clea()
        elif number == 80:
            self.pii()
        elif number == 43:
            self.plus()
        elif number == 47:
            self.del_true()  
        elif number == 69:
            self.ee()         
        elif number == 77:
            self.mr()        


class sett(QMainWindow):
    
    def __init__(self): 
        super().__init__()
        uic.loadUi('settings1.ui',self)
        self.x = '#d8d8d8'
        self.b = '#ffffff'
        self.t = '#000000'
        self.initUI()
        
    def initUI(self):  
        self.chngclr.clicked.connect(self.choosecolor)
        self.changecol.clicked.connect(self.choosecol)
        self.changetext.clicked.connect(self.choosetextcolor)
        self.path1.clicked.connect(self.showDialog)
        self.save1.clicked.connect(self.saveset)

    def choosecolor(self):
        if self.sender().text() == 'изменить цвет фона':
            color1 = QColorDialog.getColor()
            if color1.isValid():
                self.b = color1.name()
        self.setStyleSheet("background-color: {}".format(self.b))
        ex.setStyleSheet("background-color: {}".format(self.b))
        ex.label.setStyleSheet("background-color: " + self.b + ';'\
                               + "color: {}".format(self.t))
        ex.label_3.setStyleSheet("background-color: " + self.b + ';' \
                                 + "color: {}".format(self.t))               
        self.checkskobka.setStyleSheet("background-color: " + self.b \
                                       + ';'+ "color: {}".format(self.t))
        self.checsin.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))
        self.label.setStyleSheet("background-color: " + self.b + ';'\
                                 + "color: {}".format(self.t))
        self.label_2.setStyleSheet("background-color: " + self.b \
                                   + ';'+ "color: {}".format(self.t))
        self.label_4.setStyleSheet("background-color: " + self.b \
                                   + ';'+ "color: {}".format(self.t))    
        ex.labelmemory.setStyleSheet("background-color: " + self.b \
                                     + ';'+ "color: {}".format(self.t))
        ex.result1.setStyleSheet("background-color: " + self.b \
                                 + ';'+ "color: {}".format(self.t)) 
        self.label_3.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))
        self.label_5.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))  
        self.labelerror1.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))        
            
    def choosecol(self):
        if self.sender().text() == 'изменить цвет кнопок':
            color = QColorDialog.getColor()
            if color.isValid():
                self.x = color.name()
        ex.num1.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num2.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num3.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num4.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num5.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num6.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num7.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num8.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num9.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.num0.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.ravno.setStyleSheet("background-color: {}".format(self.x) \
                               + ';'+ "color: {}".format(self.t))
        ex.sbros.setStyleSheet("background-color: {}".format(self.x)\
                               + ';'+ "color: {}".format(self.t))
        ex.pi.setStyleSheet("background-color: {}".format(self.x) +\
                            ';'+ "color: {}".format(self.t))
        ex.plus1.setStyleSheet("background-color: {}".format(self.x) \
                               + ';'+ "color: {}".format(self.t))
        ex.umn.setStyleSheet("background-color: {}".format(self.x) +\
                             ';'+ "color: {}".format(self.t))
        ex.del1.setStyleSheet("background-color: {}".format(self.x) +\
                              ';'+ "color: {}".format(self.t))
        ex.okrdel.setStyleSheet("background-color: {}".format(self.x)\
                                + ';'+ "color: {}".format(self.t))
        ex.minus.setStyleSheet("background-color: {}".format(self.x)\
                               + ';'+ "color: {}".format(self.t))
        ex.delete2.setStyleSheet("background-color: {}".\
                                 format(self.x)\
                                 + ';'+ "color: {}".format(self.t))
        ex.mod1.setStyleSheet("background-color: {}".format(self.x)\
                              + ';'+ "color: {}".format(self.t))
        ex.kvadr.setStyleSheet("background-color: {}".format(self.x) \
                               + ';'+ "color: {}".format(self.t))
        ex.kub.setStyleSheet("background-color: {}".format(self.x) \
                             + ';'+ "color: {}".format(self.t))
        ex.stepen.setStyleSheet("background-color: {}".format(self.x)\
                                + ';'+ "color: {}".format(self.t))   
        ex.probel.setStyleSheet("background-color: {}".format(self.x)\
                                + ';'+ "color: {}".format(self.t))
        ex.cos1.setStyleSheet("background-color: {}".format(self.x)\
                              + ';'+ "color: {}".format(self.t))
        ex.sin1.setStyleSheet("background-color: {}".format(self.x)\
                              + ';'+ "color: {}".format(self.t))
        ex.tan1.setStyleSheet("background-color: {}".format(self.x)\
                              + ';'+ "color: {}".format(self.t))
        ex.skobka1.setStyleSheet("background-color: {}".\
                                 format(self.x) + ';'\
                                 + "color: {}".format(self.t))
        ex.skobka2.setStyleSheet("background-color: {}".\
                                 format(self.x) + ';'+ "color: {}".\
                                 format(self.t))
        ex.kor.setStyleSheet("background-color: {}".format(self.x) \
                             + ';'+ "color: {}".format(self.t))
        ex.EEE.setStyleSheet("background-color: {}".format(self.x) \
                             + ';'+ "color: {}".format(self.t))
        ex.Mr.setStyleSheet("background-color: {}".format(self.x) \
                            + ';'+ "color: {}".format(self.t))
        ex.Mminus.setStyleSheet("background-color: {}".format(self.x)\
                                + ';'+ "color: {}".format(self.t))
        ex.Mplus.setStyleSheet("background-color: {}".format(self.x)\
                               + ';'+ "color: {}".format(self.t))
        ex.cmem.setStyleSheet("background-color: {}".format(self.x) \
                              + ';'+ "color: {}".format(self.t))
        ex.yagolos.setStyleSheet("background-color: {}".\
                                 format(self.x) + ';'\
                                 + "color: {}".format(self.t))
        ex.ceil1.setStyleSheet("background-color: {}".format(self.x)\
                               + ';'+ "color: {}".format(self.t))
        self.chngclr.setStyleSheet("background-color: {}".\
                                   format(self.x) + ';'+ "color: {}".\
                                   format(self.t))
        self.changecol.setStyleSheet("background-color: {}".\
                                     format(self.x) + ';' +\
                                     "color: {}".format(self.t)) 
        ex.label_2.setStyleSheet("background-color: {}".\
                                 format(self.x) + ';'+ "color: {}".\
                                 format(self.t))
        ex.to4ka.setStyleSheet("background-color: {}".format(self.x)\
                               + ';'+ "color: {}".format(self.t))
        self.changetext.setStyleSheet("background-color: {}".\
                                      format(self.x) + ';' +\
                                      "color: {}".format(self.t))
        self.save1.setStyleSheet("background-color: {}".\
                                      format(self.x) + ';' +\
                                      "color: {}".format(self.t))
        self.path1.setStyleSheet("background-color: {}".\
                                      format(self.x) + ';' +\
                                      "color: {}".format(self.t))        
        
    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        try:
            f1 = open(fname, 'r')
            f = f1.read()
            self.x = f[:7]
            self.b = f[7:14]
            self.t = f[14:21]  
            f1.close()
            self.choosecolor()
            self.choosecol()
            self.choosetextcolor()   
            self.labelerror1.setText('ok')
        except Exception:
            self.labelerror1.setText('Failed')
        
    def saveset(self): 
        f = open("settings.txt", 'w')
        f.write(self.x)
        f.write(self.b)
        f.write(self.t)    
        f.close()
        
    def choosetextcolor(self):
        if self.sender().text() == 'изменить цвет текста':
            color = QColorDialog.getColor()
            if color.isValid():
                self.t = color.name()  
        ex.num1.setStyleSheet("background-color: " + self.x + ';'+\
                                  "color: {}".format(self.t))
        ex.num2.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num3.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num4.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num5.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num6.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num7.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num8.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num9.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.num0.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.ravno.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.sbros.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.pi.setStyleSheet("background-color: " + self.x + ';'+\
                            "color: {}".format(self.t))
        ex.plus1.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.umn.setStyleSheet("background-color: " + self.x + ';'+\
                             "color: {}".format(self.t))
        ex.del1.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.okrdel.setStyleSheet("background-color: " + self.x + ';'+\
                                "color: {}".format(self.t))
        ex.minus.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.delete2.setStyleSheet("background-color: " + self.x + ';'+\
                                 "color: {}".format(self.t))
        ex.mod1.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.kvadr.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.kub.setStyleSheet("background-color: " + self.x + ';'+\
                             "color: {}".format(self.t))
        ex.stepen.setStyleSheet("background-color: " + self.x + ';'+\
                                "color: {}".format(self.t))   
        ex.probel.setStyleSheet("background-color: " + self.x + ';'+\
                                "color: {}".format(self.t))
        ex.cos1.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.sin1.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.tan1.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.skobka1.setStyleSheet("background-color: " + self.x + ';'+\
                                 "color: {}".format(self.t))
        ex.skobka2.setStyleSheet("background-color: " + self.x +\
                                 ';'+ "color: {}".format(self.t))
        ex.kor.setStyleSheet("background-color: " + self.x + ';'+\
                             "color: {}".format(self.t))
        ex.EEE.setStyleSheet("background-color: " + self.x + ';'+\
                             "color: {}".format(self.t))
        ex.Mr.setStyleSheet("background-color: " + self.x + ';'+\
                            "color: {}".format(self.t))
        ex.Mminus.setStyleSheet("background-color: " + self.x + ';'+\
                                "color: {}".format(self.t))
        ex.Mplus.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        ex.cmem.setStyleSheet("background-color: " + self.x + ';'+\
                              "color: {}".format(self.t))
        ex.ceil1.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))
        self.chngclr.setStyleSheet("background-color: " + self.x + ';'+\
                                   "color: {}".format(self.t))
        self.changecol.setStyleSheet("background-color: " + self.x + ';'+\
                                     "color: {}".format(self.t))     
        ex.label_2.setStyleSheet("background-color: " + self.x + ';'+\
                                 "color: {}".format(self.t))
        ex.to4ka.setStyleSheet("background-color: " + self.x + ';'+\
                               "color: {}".format(self.t))   
        self.changetext.setStyleSheet("background-color: " + self.x + ';'+\
                                      "color: {}".format(self.t))
        ex.labelmemory.setStyleSheet("background-color: " + self.b + ';'+\
                                     "color: {}".format(self.t))
        ex.result1.setStyleSheet("background-color: " + self.b + ';'+\
                                 "color: {}".format(self.t))
        ex.yagolos.setStyleSheet("background-color: " + self.x + ';'+\
                                 "color: {}".format(self.t))
        ex.label.setStyleSheet("background-color: " + self.b + ';'+\
                               "color: {}".format(self.t))
        ex.label_3.setStyleSheet("background-color: " + self.b + ';'+\
                                 "color: {}".format(self.t))
        self.checkskobka.setStyleSheet("background-color: " + self.b + ';'+\
                                       "color: {}".format(self.t))
        self.checsin.setStyleSheet("background-color: " + self.b + ';'+\
                                   "color: {}".format(self.t))
        self.label.setStyleSheet("background-color: " + self.b + ';'+\
                                 "color: {}".format(self.t))
        self.label_2.setStyleSheet("background-color: " + self.b + ';'+\
                                   "color: {}".format(self.t))
        self.label_4.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))
        self.label_3.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))
        self.label_5.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))  
        self.labelerror1.setStyleSheet("background-color: " + self.b + ';'\
                                   + "color: {}".format(self.t))  
        self.save1.setStyleSheet("background-color: {}".\
                                      format(self.x) + ';' +\
                                      "color: {}".format(self.t))
        self.path1.setStyleSheet("background-color: {}".\
                                      format(self.x) + ';' +\
                                      "color: {}".format(self.t))          
            
            
ask = 'https://yandex.ru/search/?lr=6&text='
app = QApplication(sys.argv)
tabs = QtWidgets.QTabWidget()
ex = MyWidget()
eq = AudioTimer()
er = sett()
tabs.setGeometry(200, 200, 600, 670)
tabs.setWindowTitle('kalkulator')
tab1 = ex
tabs.addTab(tab1, "Калькулятор")
tab3 = er
tabs.addTab(tab3, 'settings')
tabs.setMinimumSize(QSize(600, 670)) 
tabs.show()
tabs.setCurrentIndex(0)
app.exec_()
