import os
import re
import glob
from subprocess import run as run

def main() -> None:
    """This function finds and compiles all .tex files into pdf
    """    
    localPath = os.path.abspath(os.getcwd())
    allPdfPaths = []
    allPaths = search([], 0)
    for el in allPaths:
        texFiles = glob.glob(fr"{el}\*.tex")
        if len(texFiles) > 0:
            for tex in texFiles:
                os.system(fr"pdflatex -output-directory {el} {tex}")
                allPdfPaths += texFiles
    for i in range(len(allPdfPaths)):
        allPdfPaths[i] = allPdfPaths[i].replace('.tex', '.pdf')
    print("All paths: \033[33m")
    for el in allPdfPaths:
        print(localPath + '\\' + el)
    print('\033[0m')

def search(paths:list, index:int) -> list:
    """This function recursively maps all directories and subdirectories of a path.

    Args:
        paths (list): List of all paths found (empty list for working directory, provide a single full path otherwise).
        index (int): Index at which all paths in the list have not yet been mapped (0 for initialization).

    Returns:
        list: List containing all the paths to all directories and subdirectories of the input path.
    """      
    if len(paths) != 0:
        newPath = paths.copy()
        for i in range(index, len(paths)):
            el = paths[i]
            subdirs = os.listdir(el)
            for j in range(len(subdirs)):
                subdirs[j] = el + '\\' + subdirs[j]
            subdirs = removeFiles(subdirs)
            for dir in subdirs:
                newPath.append(dir)
        if(len(newPath) == len(paths)):
            return paths
        return search(newPath, len(paths)-1)
    else:
        newPath = []
        subdirs = os.listdir(None)
        subdirs = removeFiles(subdirs)
        for dir in subdirs:
            newPath.append(fr"{dir}")
        if(len(newPath) == len(paths)):
            return paths
        return search(newPath, 0)



def removeFiles(liste:list) -> list:
    """This function aims to keep only directories from the os.listdir() output.
    NOTE: this function also assumes directories with a '.' in the name are to be removed (i.e. .gitignore, .venv, etc)

    Args:
        liste (list): Output from os.listdir()

    Returns:
        list: Cleaned output os.listdir() containing only directories
    """
    removable = []
    for el in liste:
        if os.path.isfile(el):
            removable.append(el)
    for el in removable:
        liste.remove(el)

    return liste


if __name__ == '__main__':
    main()