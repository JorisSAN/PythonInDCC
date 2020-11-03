import sys
import hou
import os
print('Starting up Pipeline')

if '//multifct/tools/pipeline/global/packages' not in sys.path:

    sys.path.append(r'//multifct/tools/pipeline/global/packages')  # path to Qt package
    sys.path.append(r'D:/SANCHEZTD4/0MyDCC/pipeline/engine/houdini/scripts')  # pipeline lib
    sys.path.append(r'D:/SANCHEZTD4/MyDCC/pipeline')  # ui lib

    from ui import my_window as mw

    win = mw.MyWindow()
    win.show()

print('Done Pipeline config')