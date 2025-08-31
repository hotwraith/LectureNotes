import os
import re
import glob
from subprocess import run as run

def main() -> None:
    allPaths = search([], 0)
    for el in allPaths:
        texFiles = glob.glob(fr"{el}\*.tex")
        if len(texFiles) > 0:
            for tex in texFiles:
                os.system(fr"pdflatex -output-directory {el} {tex}")


def search(paths:list, index:int) -> list:
    if len(paths) != 0:
        newPath = paths.copy()
        for i in range(index, len(paths)):
            el = paths[i]
            subdirs = os.listdir(el)
            subdirs = removeFiles(subdirs)
            for dir in subdirs:
                newPath.append(fr"{el}\{dir}")
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
    removable = []
    for el in liste:
        if len(re.findall(r'\.', el)) > 0:
            removable.append(el)
    for el in removable:
        liste.remove(el)

    return liste


if __name__ == '__main__':
    main()