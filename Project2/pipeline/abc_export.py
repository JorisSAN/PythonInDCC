import sys, os
import maya.cmds as cmds

cmds.loadPlugin( 'AbcExport.mll' )
cmds.loadPlugin( 'AbcImport.mll' )
print('Start export')

file = sys.argv[3]
directory = sys.argv[4]
namespace = sys.argv[5]
cmds.file(new=True, force=True)
cmds.file(file, open=True)
namespace_obj = []
namespaces = namespace.split(' ')

for n in namespaces:
    print("namespace : " + n )
    cmds.ls(n)
    n = n.split(":")
    if n[1] == "model":
        namespace_obj.append(n[0])

for abc_obj in namespace_obj:
    command ="-frameRange 1 120 -uvWrite -dataFormat ogawa -root {0}:model -file {1}/{2}.abc".format(abc_obj, directory, abc_obj)
    print("command : " + command)
    cmds.AbcExport(j=command, verbose=True)