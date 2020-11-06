import engine
import hou

class HoudiniEngine(engine.Engine) :
    def open(self, path) :
        hou.hipFile.load(path)
        
    def save(self):
        hou.hipFile.save("D:/SANCHEZTD4/testFile.hip")
        
    def __str__ (self) :
        return 'Houdini Engine'