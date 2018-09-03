import sys
import os
from xml.etree.ElementTree import ElementTree

xml_path_train = 'annotation_train/'
txt_path_train = 'wider_face_train.txt'

xml_path_val = 'annotation_val/'
txt_path_val = 'wider_face_val.txt'

def main():
    convert(xml_path_train, txt_path_train)
    convert(xml_path_val, txt_path_val)

def convert(xml_path, txt_path):
    file_list = os.listdir(xml_path)
    file_list.sort()

    file_txt = open(txt_path, 'w')

    for filename in file_list:
        xml = ElementTree()
        xml.parse(xml_path + filename)
        xml_content = [xml.findtext('filename'), str(len(xml.findall('object')))]

        for object in xml.findall('object'):
            str_temp = ''
            x1 = object.findtext('bndbox/xmin')
            y1 = object.findtext('bndbox/ymin')
            x2 = object.findtext('bndbox/xmax')
            y2 = object.findtext('bndbox/ymax')
            w = str(int(x2) - int(x1))
            h = str(int(y2) - int(y1))

            str_temp += x1 + ' '
            str_temp += y1 + ' '
            str_temp += w + ' '
            str_temp += h + ' '
            str_temp += '0' + ' '
            str_temp += '0' + ' '
            str_temp += '0' + ' '
            str_temp += '0' + ' '
            str_temp += object.findtext('truncated') + ' '
            str_temp += '0' + ' '
            xml_content.append(str_temp)

        xml_content.append('')
        file_txt.write('\n'.join(xml_content))

    file_txt.close()

if __name__ == '__main__':
    main()
