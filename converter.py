# Prefabs2Blueprints by Vgr v0.3
# Prefabs2Blueprints modified by WarpZephyr v0.6
# Converts a Space Engineers prefab to a blueprint
# Big thanks to Keen Software House
# P2B does not have any copyright, feel free to re-use and modify
# Please give credit to the original author
# v0.6 - Added clean up as well as warnings

import config
import fileinput
import getpass
import sys
import shutil
import os

path = "C:/Users/%s/AppData/Roaming/SpaceEngineers/Blueprints/local/" % getpass.getuser()
retcodes = (
"Error: '%s' is not a folder." % config.BATCH_PATH,
"All prefabs converted successfully."
)

def main():
    warning_counter = 0
    if not os.path.isdir(config.BATCH_PATH):
        return 0
    if config.BATCH_PATH:
        config.BATCH_PATH = config.BATCH_PATH.replace("/", "\\")
        if not config.BATCH_PATH[-1:] == "\\":
            config.BATCH_PATH += "\\"
    pycache_folder = config.BATCH_PATH + "__pycache__"
    files = []
    for file in os.listdir(config.BATCH_PATH):
        if file[-4:] == ".sbc":
            files.append(file)
    for reader in files:
        new_path = path + config.PREPEND + reader[:-4] + config.APPEND
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        try:
            with open(config.BATCH_PATH + reader, "r", encoding="utf-8") as old:
                oldlines = old.readlines()
                if not oldlines:
                    continue
        except UnicodeDecodeError:
            os.rmdir(new_path)
            print(f'WARNING: "{reader}" is not a Prefab or the Prefab is encrypted')
            warning_counter += 1
            continue
        new_file = path+config.PREPEND+reader[:-4]+config.APPEND+"\\bp.sbc"
        convertPrefabFile(reader, new_file)
    warning = f'Finished with {warning_counter} warning(s)'
    shutil.rmtree(pycache_folder)
    if warning_counter > 0:
        print(warning)
    return 1

def convertPrefabFile(passed_file, new_file):
    print("Converting Prefab '%s' to Blueprint . . ." % passed_file)
    try:
        with open(passed_file, 'r', encoding="utf-8") as file:
            filedata = file.read()
            filedata = filedata.replace('Prefab', 'ShipBlueprint')
            invalidFields = ('<RespawnShip>false</RespawnShip>', '<RespawnShip>true</RespawnShip>')
            if '<TypeId>ShipBlueprintDefinition</TypeId>' in filedata:
                filedata = filedata.replace('<TypeId>ShipBlueprintDefinition</TypeId>', '<TypeId>MyObjectBuilder_ShipBlueprintDefinition</TypeId>')
            if not('CubeGrids' in filedata):
                filedata = filedata.replace('<CubeGrid>', '<CubeGrids><CubeGrid>')
                filedata = filedata.replace('</CubeGrid>', '</CubeGrid></CubeGrids>')
            if invalidFields[0] in filedata or invalidFields[1] in filedata:
                for invalid in invalidFields:
                    filedata = filedata.replace(invalid, '')
        with open(new_file, 'w', encoding="utf-8") as file:
            file.write(filedata)
        if config.DELETE_OLD_FILES == True:
            os.remove(passed_file)
    except IndexError:
        os.remove(new_file)
        print("Could not convert '%s'" % passed_file)
        return

if __name__ == "__main__":
    print(retcodes[main()])
    os.system("pause")