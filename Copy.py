#!/usr/bin/python3

import sys
import pathlib
import shutil
from datetime import datetime

def main():
    """
    This Python code demonstrates the following features:
    
    * extracting the path component from a full file specification
    * copying a file
    * copying a directory
    
    """
    try:
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
        
        srcFile = "test.txt"
        srcDir = "Test_Folder"
        
        # change this srcLoc = srcDir to test copying a directory
        srcLoc = srcFile
        srcPath = pathlib.PurePath(srcLoc)
        
        dstDir = "backups"
        dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
        
        print("Date time stamp is " + dateTimeStamp) 
        print("Source file is " + srcFile)
        print("Source directory is " + srcDir)
        print("Source location is " + srcLoc)
        print("Destination directory is " + dstDir)
        print("Destination location is " + dstLoc)
        
        if pathlib.Path(srcLoc).is_dir():
            shutil.copytree(srcLoc, dstLoc)
        else:
            shutil.copy2(srcLoc, dstLoc)
    except:
        print("ERROR: An error occurred.")
    
if __name__ == "__main__":
    main()