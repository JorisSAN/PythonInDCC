import engine
import hou

class HoudiniEngine(engine.Engine) :
    def open(self, path) :
        pass
        
    def __str__ (self) :
        return 'Houdini Engine'