import os
from os import walk
import shutil
from promotion import promote

# Write code to rename uploaded file for ease of use
def get_uploadfile_name(num=0): # Get file name / path
    dir = os.listdir("./static/upload")
    if len(dir) > 0:
        filenames = next(walk("./static/upload"), (None, None, []))[2]
        return filenames[num]
    return "Upload folder is empty" 

def get_downloadfile_name(num=0): # Get file name / path
    dir = os.listdir("./static/download")
    if len(dir) > 0:
        filenames = next(walk("./static/download"), (None, None, []))[2]
        return filenames[num]
    return "Download folder is empty"


def rename(file_name):
    src = "./static/upload/" + file_name[0] # In my case file_name is an arry so index needs to be specified
    dst = "./static/upload/data.csv"
    shutil.copy(src, dst)
    return dst

# Write code to clear working directories here
def clear_upload_data(path):
    dir = os.listdir("./static/upload")
    if len(dir) > 0:
        os.remove("./static/upload/" + path)
    return "Upload folder is empty"

def clear_download_data(path):
    dir = os.listdir("./static/download")
    if len(dir) > 0:
        os.remove("./static/download/" + path)
    return "Download folder is empty"

clear_download_data(get_downloadfile_name(0))