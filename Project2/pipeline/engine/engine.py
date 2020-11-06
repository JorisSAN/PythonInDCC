import sys

class Engine(object) :
    def open() :
        pass
        
    def save() :
        pass

def get_current():
    engine = Engine()

    if 'maya' in sys.executable :
        import maya_engine
        reload(maya_engine)
        engine = maya_engine.MayaEngine()
        
    if 'houdini' in sys.executable :
        import houdini_engine
        reload(houdini_engine)
        engine = houdini_engine.HoudiniEngine()
    
    return engine