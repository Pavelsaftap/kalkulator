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
        self.num1.clicked.connect(self.num11)
        self.num2.clicked.connect(self.num22)
        self.num3.clicked.connect(self.num33)
        self.num4.clicked.connect(self.num44)
        self.num5.clicked.connect(self.num55)
        self.num6.clicked.connect(self.num66)
        self.num7.clicked.connect(self.num77)
        self.num8.clicked.connect(self.num88)
        self.num9.clicked.connect(self.num99)
        self.num0.clicked.connect(self.num00)
        self.ravno.clicked.connect(self.res)
        self.sbros.clicked.connect(self.clea)
        self.pi.clicked.connect(self.pii)
        self.plus1.clicked.connect(self.plus)
        self.umn.clicked.connect(self.umno)
        self.del1.clicked.connect(self.del11)
        self.okrdel.clicked.connect(self.del22)
        self.minus.clicked.connect(self.minuss)
        self.delete2.clicked.connect(self.dele)
        
    def num11(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(1)
        self.label.setText(self.stroka[-80:])
        
    def num22(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(2)
        self.label.setText(self.stroka[-80:])  
        
    def num33(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(3)
        self.label.setText(self.stroka[-80:])   
        
    def num44(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(4)
        self.label.setText(self.stroka[-80:])    
        
    def num55(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(5)
        self.label.setText(self.stroka[-80:])    
    
    def num66(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(6)
        self.label.setText(self.stroka[-80:])  
        
    def num77(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(7)
        self.label.setText(self.stroka[-80:])     
        
    def num88(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(8)
        self.label.setText(self.stroka[-80:])     
        
    def num99(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(9)
        self.label.setText(self.stroka[-80:])   
        
    def num00(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += str(0)
        self.label.setText(self.stroka[-80:])   
    
    def pii(self):
        if self.flag == 0:
            self.stroka = ''
            self.flag = 1
        self.stroka += 'pi'
        self.label.setText(self.stroka[-80:])          
    
    def res(self):
        try:
            self.result1.setText(str(eval(self.stroka)))
            self.stroka = str(eval(self.stroka))
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
 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())