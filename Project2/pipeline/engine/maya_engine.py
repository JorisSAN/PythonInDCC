import engine
import maya.cmds as cmds
import subprocess as subp

mayabatch = "D:/Maya/Maya2020/bin/mayabatch.exe"
abcExport = "C:/Users/user/Desktop/Projet/Projet-et-prog/PythonInDCC/Project2/pipeline/abc_export.py"

class MayaEngine(engine.Engine) :
    def open(self, path) :
        cmds.file(new = True, force = True)
        cmds.file(path, o = True)
        
    def save(self):
        cmds.file(rename="D:/SANCHEZTD4/test.ma")
        cmds.file(save=True, type="mayaAscii")
        
    def __str__ (self) :
        return 'Maya Engine'
        
    def export(self, path, namespace, openFile):
        if openFile == "" :
            openFile = cmds.file(q=True, sn=True)

        path = path.replace("\\", "/")
        openFile = openFile.replace("\\", "/")

        subp.Popen("\"" + mayabatch + "\" -command \"python(\\\"execfile(\'" + abcExport + "\')\\\");\" \"" + path + "\" \"" + namespace + "\" -file \"" + openFile + "\"", shell=True)