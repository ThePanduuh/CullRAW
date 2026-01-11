import glob
import os
import shutil
import sys
from pathlib import Path
import send2trash

cull_file = sys.argv[1]
file_dir = Path(cull_file)
jpg_dir = Path(cull_file).parent.parent / "JPG/"
raw_dir = Path(cull_file).parent.parent / "RAW/"
del_dir = Path(cull_file).parent.parent / "DEL/"

os.chdir(jpg_dir)
jpg_list = glob.glob("*.JPG")
jpg_list = [os.path.splitext(val)[0] for val in jpg_list]

os.chdir(raw_dir)
for file in [os.path.splitext(val)[0] for val in glob.glob("*.RAF")]:
    if file not in jpg_list:
        if not os.path.exists(del_dir):
            os.mkdir(del_dir)
        source = os.path.join(raw_dir, file + ".RAF")
        dest = os.path.join(del_dir, file + ".RAF")
        shutil.move(source, dest)

if os.path.exists(del_dir):
    send2trash.send2trash(del_dir)
