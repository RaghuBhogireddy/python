# Challenge is to create a folder and write all
# the file names to a .txt file
# along with total byte count


import os
from os import path
import shutil as sh


def challenge():
    dirlist = os.listdir()
    totalBytes = 0
    for entry in dirlist:
        if os.path.isfile(entry):
            fileSize = os.path.getsize(entry)
            totalBytes += fileSize

    os.mkdir("results")

    resultsFile =  open("results/result.txt", "w+")
    if resultsFile.mode == "w+":
        resultsFile.write("Total byteCount: " + str(totalBytes) + "\n")
        resultsFile.write("Files List: \n")
        resultsFile.write("-------------------- \n")
        for entry in dirlist:
            if os.path.isfile(entry):
                resultsFile.write(entry + "\n")

        resultsFile.close()


if __name__ == "__main__":
    challenge()
