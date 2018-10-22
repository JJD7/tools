import glob
import cv2
import time
import os

def get_latest_image(dirpath):
    """
    Get the latest image file in the given directory
    """
    #generate list of files ending in .png
    list_of_files = (f for f in os.listdir(dirpath) if f.endswith('.' + 'png'))
    #get the file last created
    paths = [os.path.join(dirpath, basename) for basename in list_of_files]
    latest_file = max(paths, key=os.path.getctime)
    #need to pause to avoid read errors
    time.sleep(0.1)
    return latest_file

#dir = str(input("enter Directory: "))
#dir = './MultiCameraImageCapture/build/2018-10-01-09-15-39/cam1'
#dir = './'

dir = './MultiCameraImageCapture/build'
list_of_folders = [dI for dI in os.listdir(dir) if dI.startswith('2018')]
folder_dirs = [os.path.join(dir, basename) for basename in list_of_folders]
latest_folder = max(folder_dirs, key=os.path.getctime)

directory1 = latest_folder + '/cam1'
directory2 = latest_folder + '/cam2'
directory3 = latest_folder + '/cam3'

while(1):
    #cv2.namedWindow('cam1', cv2.WINDOW_NORMAL)
    #cv2.namedWindow('cam2', cv2.WINDOW_NORMAL)
    im = cv2.imread(get_latest_image(directory1))
    cv2.imshow('cam1',im)
    cv2.waitKey(1)
    #im = cv2.imread(get_latest_image(directory2))
    #cv2.imshow('cam2',im)
    #cv2.waitKey(1)
    im = cv2.imread(get_latest_image(directory3))
    cv2.imshow('cam3',im)
    cv2.waitKey(1)
