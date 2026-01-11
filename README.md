# CullRAW

This is a python script I wrote to aid with culling (sorting good and bad photos) using a basic photo viewer in Windows. Delete files in the JPG folder, run the script, and the deleted JPG files will have the corresponding RAW files deleted. "Automate the boring things" they say...

## Requirements

This script was written using Python 3. Install Python 3 from https://www.python.org

This script requires Send2Trash. Install via pip: `pip install send2trash`

This script requires compilation into a `.exe` for use as a Send To shortcut in Windows.

I used PyInstaller, which can be installed via pip: `pip install pyinstaller`.

This was built and tested on Windows. No guarantees this will be useful on other operating systems.

## How to run

**IMPORTANT:** The folder that the file comes from must have the folder structure output by the [PhotoSorter](https://github.com/thepanduuh/PhotoSorter) script.

This script is designed to run via "Send To" on Windows. Select either a JPG or RAW photo, right click, Show more options (Win11), Send To, Cull RAWs (or whatever custom name you make for the shortcut).

Instructions on adding to the Send To menu can be found [here.](#Add-to-Send-To-menu-Windows)


## Theory of Operation/nitty-gritty

The Fujifilm X-T5 outputs two file types when saving RAW and JPEG files. The files end with .RAF for RAW files, and .JPG for JPG files. If your camera uses different file types, the file types can be edited in the `main.py` script on lines 15 (JPG) and 19, 23, and 24 (RAW).

This script uses `sys.argv[1]` which means that the script will only run if a file is sent to it via drag and drop, or via "Send To" menu on Windows. [Add to Send To on Windows](#Add-to-Send-To-menu-Windows)

The file structure below is the INPUT for the script. Note the `filename2.JPG` file was deleted from the JPG directory of the INPUT.

```
Photo_folder
├── JPG
│   ├── filename1.JPG
│   ├── filename3.JPG
│   └── ...
├── RAW
│   ├── filename1.RAF
│   ├── filename2.RAF
│   ├── filename3.RAF
│   └── ...
└── ...
```

After running the script, the RAW directory will have the appropriate files deleted to match the JPG directory.

```
Photo_folder
├── JPG
│   ├── filename1.JPG
│   ├── filename3.JPG
│   └── ...
├── RAW
│   ├── filename1.RAF
│   ├── filename3.RAF
│   └── ...
└── ...
```

All files that do not end in .RAF or .JPEG/.JPG will not be affected.

## Add to Send To menu Windows

Note: I wrote these instructions before I realized Windows silently shuttered python scripts from being able to be added to the Send To menu. To run these via Send To menu, they need to be made into .exe files.

The easiest way I found was to install PyInstaller via pip. `pip install pyinstaller`

Navigate to the folder via Command Line.

Run `pyinstaller Cull_RAWs.py`

The .exe file will be created and placed in the following path: `../CullRAW/dist/Cull_RAWs/Cull_RAWs.exe`

To add to the Send To menu on Windows:
* Download the GitHub repository
* Extract the files and place the CullRAW folder in a known location
	* The folder can be placed on a NAS if you are connected to the server when trying to run the script!
	* If using the NAS for hosting the script folder, Python will still need to be installed on the computer trying to run the script
* Run pyinstaller command above
* Find compiled .exe file in the location above
* Select .exe file
* Right-click, Show more options (Win11), Create Shortcut
* Rename the shortcut to a friendlier name, ex: "Cull RAWs"
* Cut the shortcut to the clipboard
* Press `Win+R` to open the Run menu
* Type `shell:sendto` and press Enter
* Paste the shortcut in the folder that opens

[Test the script out!](#How-to-run)

