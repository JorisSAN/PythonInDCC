import engine
import maya.cmds as cmds

class MayaEngine(engine.Engine) :
    def open(self, path) :
        cmds.file(new = True, force = True)
        cmds.file(path, o = True)
        
    def __str__ (self) :
        return 'Maya Engine'