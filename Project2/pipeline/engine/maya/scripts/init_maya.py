import sys, os
import maya.cmds as cmds

print('Starting up pipeline')

here = os.path.dirname(__file__)
deployment_root = here.split('/pipeline/')[0]

sys.path.append(r'C:\Users\user\Desktop\Projet\Projet-et-prog\PythonInDCC\Project2\lib')
sys.path.append(deployment_root)

print('Done Pipeline Config')