import sys
import hou
import os
print('Starting up Pipeline')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';') [-1]
deployement_root = here.split('/pipeline/') [0]

sys.path.append(deployement_root)  # import path project
sys.path.append(r'C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC/pipeline/Qt')  # import Qt lib

from ui import my_window as mw

win = mw.MyWindow()
win.show()

print('Done Pipeline config')