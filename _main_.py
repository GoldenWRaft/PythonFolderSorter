from os import listdir
from os.path import isfile, join
import os
import shutil
def sort_files_in_a_folder(mypath):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    for file in files:
        filetype=file.split('.')[-1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name=mypath+'/_'+ filetype + '_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            if os.path.isdir(new_folder_name)==True:  #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    for file in files:
        count = 1
        src_path=mypath+'/'+file
        filetype=file.split('.')[-1]
        if filetype in filetype_folder_dict.keys():
            dest_path=filetype_folder_dict[str(filetype)]
            destination_file = dest_path + '/' + file
            while os.path.exists(destination_file):
                destination_file = os.path.join(dest_path, f"{file.split('.')[0]} ({count}).{file.split('.')[-1]}")
                count += 1
            shutil.move(src_path, destination_file)
            print(src_path + ' >>> ' + destination_file)
if __name__=="__main__":
    path='C:/Users/user-pc/Downloads'
    sort_files_in_a_folder(path)
