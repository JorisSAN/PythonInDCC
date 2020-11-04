import sys
import hou
import os
print('Starting up Pipeline')

here = os.path.dirname(__file__)

deployment_root = here.split('/pipeline/')[0]

if '//multifct/tools/pipeline/global/packages' not in sys.path:

    sys.path.append(r'/pipeline/global/packages')  # path to Qt package
    sys.path.append(r'/pipeline/engine/houdini/scripts')  # pipeline lib
    sys.path.append(deployment_root)  # ui lib

    from ui import my_window as mw

    win = mw.MyWindow()
    win.show()

print('Done Pipeline config')