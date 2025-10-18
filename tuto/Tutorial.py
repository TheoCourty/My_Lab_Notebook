from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


#Ici je vais personnaliser une instance de ma fenêtre.
#En gros QMainWindow = classe qui permet de faire une fenêtre
#J'en fait une classe, afin que les éléments que je vais mettre 
#dedans fassent partie intégrante de la fenêtre, et soient
#tous liés ! 
class MyWindow(QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        
        xpos = 200
        ypos = 200
        width = 500
        height = 500
        
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("First window")
        
    def update(self):
        self.label.adjustSize()
    
    def clicked(self):
        self.label.setText("Nice :)")
        self.update()
        

        
    def initUI(self):
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label !")
        self.label.move(50,50)

        
        self.button_1 = QtWidgets.QPushButton(self)
        self.button_1.setText("Clique :)")
        self.button_1.move(50,100)
        self.button_1.clicked.connect(self.clicked)
        
        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.move(0,200)
        self.calendar.setFixedSize(400, 300)

    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()