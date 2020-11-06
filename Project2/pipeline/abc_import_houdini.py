import sys, hou, os, re

importPath = sys.argv[1]
namespaceString = sys.argv[2]
importContent = os.listdir(importPath)
namespaces = namespaceString.split(" ")

for namespace in namespaces :
    # Create a geometry node
    geometry = hou.node("/obj").createNode("geo")
    merge = geometry.createNode("merge")

    for importFile in importContent :
        reg = re.compile(r"^" + namespace)

        if(reg.match(importFile)):
            alembicRop = geometry.createNode("alembic")
            alembicRop.setName(importFile)
            alembicPath = importPath + "/" + importFile
            alembicRop.parm("fileName").set(alembicPath)
            alembicRop.setDisplayFlag(True)
            alembicRop.setRenderFlag(True)

    geometry.layoutChildren()

hou.hipFile.save()