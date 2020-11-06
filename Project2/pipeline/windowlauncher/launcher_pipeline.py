import sys

if r"C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC" not in sys.path:
    sys.path.append(r'C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC')
    sys.path.append(r'C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC/pipeline/Qt')

from pipeline.engine import engine
from Qt import QtWidgets
from pipeline.ui import my_window as mw

app = QtWidgets.QApplication(sys.argv)
win = mw.MyWindow()
win.show()

app.exec_()