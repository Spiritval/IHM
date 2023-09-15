import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton

#Créer la fenetre

app=QApplication(sys.argv)
base=QWidget()
base.resize(320,240)
base.setWindowTitle('IHM')





# affiche
base.show()
app.exec_()
