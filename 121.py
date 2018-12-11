import sys
from math import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
 
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('kalkulator.ui',self)
        self.stroka = '_' * 81
        self.flag = 0
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
            a1 = str(eval(self.stroka.replace('^', '**').replace(' ', '')))
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
            pass
        else:
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
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())