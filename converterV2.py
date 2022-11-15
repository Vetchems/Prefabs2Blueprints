# Prefabs2Blueprints by Vgr v0.3
# Prefabs2Blueprints modified by WarpZephyr v0.5
# Converts a Space Engineers prefab to a blueprint
# Big thanks to Keen Software House
# P2B does not have any copyright, feel free to re-use and modify
# Please give credit to the original author
# v0.5 - Re-Added Compatibilty for files with old invalid fields

import fileinput
import getpass
import configV2
import sys
import os

path = "C:/Users/%s/AppData/Roaming/SpaceEngineers/Blueprints/local/" % getpass.getuser()

retcodes = (
"Error: %s is not a folder." % configV2.BATCH_PATH,
"All prefabs converted successfully."
)

def main():
    if not os.path.isdir(configV2.BATCH_PATH):
        return 0
    if configV2.BATCH_PATH:
        configV2.BATCH_PATH = configV2.BATCH_PATH.replace("/", "\\")
        if not configV2.BATCH_PATH[-1:] == "\\":
            configV2.BATCH_PATH += "\\"
            
    files = []
    for file in os.listdir(configV2.BATCH_PATH):
        if file[-4:] == ".sbc":
            files.append(file)
    for reader in files:
        if not os.path.exists(path + configV2.PREPEND + reader[:-4] + configV2.APPEND):
            os.mkdir(path + configV2.PREPEND + reader[:-4] + configV2.APPEND)
        try:
            with open(configV2.BATCH_PATH + reader, "r", encoding="utf-8") as old:
                oldlines = old.readlines()
                if not oldlines:
                    continue
        except UnicodeDecodeError:
            continue
        new_file = path+configV2.PREPEND+reader[:-4]+configV2.APPEND+"\\bp.sbc"
        convertPrefabFile(reader, new_file)  
    return 1

def convertPrefabFile(passed_file, new_file):
    print("Converting Prefab '%s' to Blueprint . . ." % passed_file)
    try:
        with open(passed_file, 'r', encoding="utf-8") as file :
            filedata = file.read()
            filedata = filedata.replace('Prefab', 'ShipBlueprint')
            if '<TypeId>ShipBlueprintDefinition</TypeId>' in filedata:
                filedata = filedata.replace('<TypeId>ShipBlueprintDefinition</TypeId>', '<TypeId>MyObjectBuilder_ShipBlueprintDefinition</TypeId>')
            if not('CubeGrids' in filedata):
                filedata = filedata.replace('<CubeGrid>', '<CubeGrids><CubeGrid>')
                filedata = filedata.replace('</CubeGrid>', '</CubeGrid></CubeGrids>')
            if '<RespawnShip>false</RespawnShip>' in filedata:
                filedata = filedata.replace('<RespawnShip>false</RespawnShip>', '')
            if '<RespawnShip>true</RespawnShip>' in filedata:
                filedata = filedata.replace('<RespawnShip>true</RespawnShip>', '')
        with open(new_file, 'w', encoding="utf-8") as file:
            file.write(filedata)
    except IndexError:
        os.remove(new_file)
        print("Could not convert '%s'" % passed_file)
        return

if __name__ == "__main__":
    print(retcodes[main()])
    os.system("pause")
