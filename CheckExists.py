#!/usr/bin/python3

import sys
import os

def main():
    """
    This Python code demonstrates the following features:
    
    * checking that a file or directory exists.
    
    """
    try:
        fileExists = "CLIs.py"
        fileNotExists = "xxx.py"
        
        if not os.path.exists(fileExists):
            print("ERROR: file " + fileExists + " does not exist.")
        else:
            print("File " + fileExists + " does exist.")
            
        if not os.path.exists(fileNotExists):
            print("ERROR: file " + fileNotExists + " does not exist.")
        else:
            print("File " + fileNotExists + " does exist.")
            
    except:
        print("ERROR: An error occurred.")
    
if __name__ == "__main__":
    main()