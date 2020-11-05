import sys, os
import maya.cmds as cmds
print('Starting up Pipeline')

here = os.path.dirname(__file__)

deployment_root = here.split('/pipeline/')[0]
sys.path.append(deployment_root)  # pipeline path

sys.path.append(r'C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC/pipeline/Qt')  # path to Qt package

from ui import my_window as mw

win = mw.MyWindow()
win.show()

print('Done Pipeline config')