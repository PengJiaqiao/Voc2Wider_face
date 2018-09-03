import scipy.io as sio
import os
import numpy as np

txt_path_train = 'wider_face_train.txt'
txt_path_val = 'wider_face_val.txt'
mat_path_train = 'wider_face_train.mat'
mat_path_val = 'wider_face_val.mat'


def main():
    convert(txt_path_train, mat_path_train, 315)
    convert(txt_path_val, mat_path_val, 294)

def convert(txt_path, mat_path, num_images):
    # For each type of images
    blur_label = np.zeros((1,1), dtype=np.object)
    event = np.zeros((1,1), dtype=np.object)
    expression_label = np.zeros((1,1), dtype=np.object)
    face_bbx = np.zeros((1,1), dtype=np.object)
    file_list = np.zeros((1,1), dtype=np.object)
    illumination_label = np.zeros((1,1), dtype=np.object)
    invalid_label = np.zeros((1,1), dtype=np.object)
    occlusion_label = np.zeros((1,1), dtype=np.object)
    pose_label = np.zeros((1,1), dtype=np.object)
    linelist = []

    # for each single image
    blur_label_1 = np.zeros((num_images,1), dtype=np.object)
    event_1 = np.zeros((1,1), dtype=np.object)
    expression_label_1 = np.zeros((num_images,1), dtype=np.object)
    face_bbx_1 = np.zeros((num_images,1), dtype=np.object)
    file_list_1 = np.zeros((num_images,1), dtype=np.object)
    illumination_label_1 = np.zeros((num_images,1), dtype=np.object)
    invalid_label_1 = np.zeros((num_images,1), dtype=np.object)
    occlusion_label_1 = np.zeros((num_images,1), dtype=np.object)
    pose_label_1 = np.zeros((num_images,1), dtype=np.object)

    # convert annotation
    with open(txt_path, 'a') as f:
        f.write('for temp use')#temp line for extract information from each bounding box
    f.close()
    with open(txt_path, 'r+') as f:
        jump=0
        buff=0
        count=0 # number of images
        for line in f:
            if jump==0:
                if '.jpg' in line:
                    file_list_2 = np.zeros((1,), dtype=np.object)
                    file_list_2[0] = line
                elif len(line.strip())==1:
                    jump=int(line.strip())
                    buff=jump
                if len(linelist)!=0:
                    # for each bounding box in an image, no need for 'event'
                    blur_label_2 = np.zeros((buff,1), dtype=np.object)
                    expression_label_2 = np.zeros((buff,1), dtype=np.object)
                    face_bbx_2 = np.zeros((buff,4), dtype=np.object)
                    illumination_label_2 = np.zeros((buff,1), dtype=np.object)
                    invalid_label_2 = np.zeros((buff,1), dtype=np.object)
                    occlusion_label_2 = np.zeros((buff,1), dtype=np.object)
                    pose_label_2 = np.zeros((buff,1), dtype=np.object)

                    for i in range(buff):
                        blur_label_2[i] = linelist[i][4]
                        expression_label_2[i] = linelist[i][5]
                        face_bbx_2[i][0], face_bbx_2[i][1], face_bbx_2[i][2], \
                        face_bbx_2[i][3] = linelist[i][0], linelist[i][1], linelist[i][2], \
                        linelist[i][3]
                        illumination_label_2[i] = linelist[i][6]
                        invalid_label_2[i] = linelist[i][7]
                        occlusion_label_2[i] = linelist[i][8]
                        pose_label_2[i] = linelist[i][9]

                    buff=0
                    blur_label_1[count][0] = blur_label_2
                    expression_label_1[count][0] = expression_label_2
                    face_bbx_1[count][0] = face_bbx_2
                    file_list_1[count][0] = file_list_2
                    illumination_label_1[count][0] = illumination_label_2
                    invalid_label_1[count][0] = invalid_label_2
                    occlusion_label_1[count][0] = occlusion_label_2
                    pose_label_1[count][0] = pose_label_2

                    count += 1
                    linelist.clear()
            else:
                jump-=1
                linelist.append(line.split())

    blur_label[0][0] = blur_label_1
    event[0][0] = event_1
    expression_label[0][0] = expression_label_1
    face_bbx[0][0] = face_bbx_1
    file_list[0][0] = file_list_1
    illumination_label[0][0] = illumination_label_1
    invalid_label[0][0] = invalid_label_1
    occlusion_label[0][0] = occlusion_label_1
    pose_label[0][0] = pose_label_1

    os.system('sed -i "$ d" {0}'.format(txt_path))
    f.close()


    sio.savemat(mat_path, {'blur_label_list': blur_label, \
                                  'event_list': event, \
            'expression_label_list': expression_label, \
            'face_bbx_list': face_bbx, \
            'file_list': file_list, \
            'illumination_label_list': illumination_label, \
            'invalid_label_list': invalid_label, \
            'occlusion_label_list': occlusion_label, \
            'pose_label_list': pose_label})

if __name__ == '__main__':
    main()
