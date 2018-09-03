# Voc2Wider_face
xml(VOC2012) to mat(Wider_face). Convert image dataset annotation format

## Usage
Download [VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/) and unzip data and annotation files to such that:

```zsh
$ ls data
extract.py             txt2mat.py             xml2txt.py
Annotations/           |->ImageSets/          JPEGImages/
                       |    |->Main/
                       |    |    |->train.txt
                       |    |    |->val.txt
```
Use extract.py to extract the images from the datasets based on the filename stored in "ImageSets/".  
```
$ python extract.py
```
Use xml2txt.py to convert these VOC xml annotation files and use txt2mat.py to convert the intermedia txt files to the final Matlab data files.
```
$ python xml2txt.py
$ python txt2mat.py
```
The final output is like that:
```
$ ls data
wider_face_train.mat    wider_face_train.txt    wider_face_val.txt  wider_face_val.mat
WIDER_train/            WIDER_val/
```
