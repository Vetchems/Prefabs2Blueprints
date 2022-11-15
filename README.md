## Prefabs2Blueprints Version 0.5b
Is working as of current version: 1.201  
This Python script converts Space Engineers prefabs to Blueprints.

To use P2B, you need [Python][0].  
I'm not sure if my new changes break Python 2 Compatibility, Python 3 would be best for now.

### Requirements
1. [Download and install Python][0]
2. [Download the code][1].

### Using the code
1. Create a new folder anywhere you like.
2. Put all the `.sbc` prefabs that you want to convert in that folder. `sbcB5` files are [not needed][2]
3. Copy the `configV2.py` and `convertV2.py` files into the same folder.
5. Open `config.py` with any text editor.
6. Edit `BATCH_PATH` to the full path of the folder you created in step 1.
7. Replace any singular backward slashes `\` with forward slashes `/` or double-backward slashes `\\` in the path.
8. The name of the `.sbc` files will be the folders' names.
9. You can add something to `APPEND` and `PREPEND`, P2B will respectively append or prepend those to the path.  
   (Explained further in `configV2.py`)

When you're done editing your settings, save `configV2.py` and double-click on `converterV2.py`.  
The files will be converted and you can add the folders with the blueprints to your:  
`C:/Users/%s/AppData/Roaming/SpaceEngineers/Blueprints/local/`
Path where the blueprints are kept

The reason many of the older version's settings are not present is that I couldn't find what they referred to,  
Such as the dampener settings, or I did not know how to add them at the moment, such as the owner settings  
I modified this as a quick solution and it appears to work.

Prefab files are not deleted after conversion at the moment, you will need to delete them yourself,  
Also python leaves a `__pycache__` folder after use of the script, it is not needed so delete it

Please report any issues using the [GitHub issue tracker][3].

Changelog:  
Old Dev Changlog (May not be entirely accurate anymore):  
0.1 - First version

0.2 - Batch mode, pretty much final release

0.3 - Backwards compatibility

0.4 - Add proper UTF-8 handling, and properly handle nonsense

Start of my fork:  
0.5b - Fixed for newest version, simple conversion only for now

[0]: https://www.python.org/downloads/
[1]: https://github.com/WarpZephyr/Prefabs2Blueprints/archive/master.zip
[2]: https://steamcommunity.com/app/244850/discussions/0/1636417554427487220/
[3]: https://github.com/WarpZephyr/Prefabs2Blueprints/issues
