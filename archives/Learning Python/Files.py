import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import shutil as sh
from zipfile import ZipFile


def pathUtilities():
    # myFile = open("textfile.txt", "w+")
    # myFile = open("textfile.txt", "a+")
    # myFile = open("textfile.txt", "r")
    # if myFile.mode == 'r':
    #     print(myFile.read())
    # for i in range(10):
    #     myFile.write("This is some Text\n")
    # myFile.close()
    print(os.name)
    print("Item Exists: ", str(path.exists("textfile.txt")))
    print("Item path: ", path.realpath("textfile.txt"))
    print("Item's path & name ", path.split(path.realpath("textfile.txt")))
    print("Modification Time ", time.ctime(path.getmtime("textfile.txt")))
    print("Modification Time ", datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("File Modified ", td.total_seconds(), "secs ago")


def shellUtilities():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        # dst = src + ".bak"
        # sh.copy(src, dst)
        root_dir, tail = path.split(src)
        sh.make_archive("Archive", "zip", root_dir)
        with ZipFile("Archive.zip", "w") as newZip:
            newZip.write("textfile.txt")
            newZip.write("textfile.txt.bak")


if __name__ == "__main__":
    shellUtilities()





