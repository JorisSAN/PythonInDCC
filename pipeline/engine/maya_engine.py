import engine
import maya.cmds as cmds

class MayaEngine(engine.Engine) :
    def open(self, path) :
        cmds.file(new = True, force = True)
        cmds.file(path, o = True)
        
    def save(self):
        cmds.file(rename="D:/SANCHEZTD4/test.ma")
        cmds.file(save=True, type="mayaAscii")
        
    def __str__ (self) :
        return 'Maya Engine'