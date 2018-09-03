import os
import shutil

TxtPath = 'ImageSets/Main/train.txt'
SavePath = 'annotation_train/'

def main():
    file = open(TxtPath, 'r')
    for line in file.readlines():
        line = line.rstrip('\n')
        ImagePath = 'Annotations/' + line + '.xml'
        CopyPath = SavePath + line + '.xml'
        shutil.copyfile(ImagePath, CopyPath)

if __name__ == '__main__':
    main()
