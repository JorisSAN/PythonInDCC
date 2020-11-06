import engine
import hou

class HoudiniEngine(engine.Engine) :
    def open(self, path) :
        hou.hipFile.load(path)
        
    def save(self):
        hou.hipFile.save("D:/SANCHEZTD4/testFile.hip")
        
    def __str__ (self) :
        return 'Houdini Engine'
        
    def export(self, path, namespaceString, openFilePath) :
        namespaces = namespaceString.split(" ")
        for namespace in namespaces :
            print("export " + namespace)
        
    def importAbc(self, importFolderPath, namespaceString, destinationFilePath):
        importFolderPath = importFolderPath.replace("\\", "/")
        destinationFilePath = destinationFilePath.replace("\\", "/")
        
        dirname = os.path.dirname(__file__)
        reg = re.compile(r"\\[^\\]+$")
        dirname = reg.sub("", dirname)
        dirname = dirname.replace("\\", "/")

        if not os.path.isfile(destinationFilePath) :
            houdiniAbcInitQuery = "hython \"" + dirname + "/houdiniInit.py\" \"" + destinationFilePath + "\""
            subprocess.Popen(houdiniAbcInitQuery, shell=True).wait()

        houdiniAbcImportQuery = "hython \"" + destinationFilePath + "\" \"" + dirname + "/abc_import_houdini.py\" \"" + importFolderPath + "\" \"" + namespaceString + "\""
        subprocess.Popen(houdiniAbcImportQuery, shell=True)