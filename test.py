import os
# from pathlib import Path
basepath = '1Rivet/'
# Listing directory using pathlib module
# entries = Path(basepath)
# for entry in entries.iterdir():
#     print(entry.name)

def scanDirectory():
    directory = os.scandir()

with os.scandir(basepath) as directory:
    for entry in directory:
        if entry.is_file():
            print(entry.name)

        if entry.is_dir():
            print(entry.name)


