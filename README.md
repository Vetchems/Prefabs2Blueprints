## Prefabs2Blueprints Version 0.6
Is working as of current version: 1.201  
This Python script converts Space Engineers prefabs to Blueprints.

To use P2B, you need [Python][0].  
I'm not sure if my new changes break Python 2 Compatibility, Python 3 would be best for now.

### Requirements
1. [Download and install Python][0]
2. [Download the code][1]

### Using the code
1. Create a new folder anywhere you like.
2. Put all the `.sbc` prefabs that you want to convert in that folder. `sbcB5` files are [not needed][2].
3. Copy the `config.py` and `convert.py` files into the same folder.
5. Open `config.py` with any text editor.
6. Edit `BATCH_PATH` to the full path of the folder you created in step 1.
7. Replace any singular backward slashes `\` with forward slashes `/` or double-backward slashes `\\` in the path.
8. The name of the `.sbc` files will be the folders' names.
9. You can add something to `APPEND` and `PREPEND`, P2B will respectively append or prepend those to the path.  
   (Explained further in `config.py`)

When you're done editing your settings, save `config.py` and double-click on `converter.py`.  
The blueprints will be put directly into your blueprints folder automatically

The reason many of the older version's settings are not present is that I couldn't find what they referred to,  
Such as the dampener settings, or I did not know how to add them at the moment, such as the owner settings  
I modified this as a quick solution and it appears to work.

Please report any issues using the [GitHub issue tracker][3].

[0]: https://www.python.org/downloads/
[1]: https://github.com/WarpZephyr/Prefabs2Blueprints/archive/master.zip
[2]: https://steamcommunity.com/app/244850/discussions/0/1636417554427487220/
[3]: https://github.com/WarpZephyr/Prefabs2Blueprints/issues
