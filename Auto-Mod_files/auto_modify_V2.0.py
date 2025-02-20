#!/usr/bin/python
import os, re,json
from file_handling import FileHandler


# Variables

data_dict = {
    'Original_File' : [],
    'Is Directory' : 'Y or N',
    'New_File' : [],
    'Final File' : []
    }


# list of things to remove example 'axxo'
remove_text_list = ['appletv','yify','-','\d\d\dp','1080','1080p','bluray','x264','sparks',
    '\s{2,}','ps3', 'publichd','dvdrip','axxo', 'xvid', 'tots','1337x','bdrip','ac3']

# remove later
remove_text_list.append('\.py')

# Use re module to compile the text in re_remove_list to produce
re_compiled = [re.compile(item_to_exclude, re.IGNORECASE) for item_to_exclude in remove_text_list]


# get the folder location to do the automatic name changes


# Functions
def getfilepath(directory):
    if os.path.isdir(directory):

        dir = os.listdir(directory)
        return dir

def add_orig_files_to_dict(d):
    for f in d:
        print(f)
        
        data_dict['Original_File'].append(f)
        
def remove_text(text_to_remove,original_string):
    return original_string.replace(text_to_remove,'')

def remove_periods(original_string):
    dot_count = original_string.count(".")
    original_string = original_string.replace('.', ' ', dot_count - 1)
    return original_string



def create_txt_file(directory_list):
    with open('directory_listing.txt','w') as f:
        for file in directory_list:
            f.writelines(f'{file}\n')

def show_dict():
    for k,v in data_dict.items():
        print(k,v) 

isTesting = False
def main():

    file_path = ""

    if isTesting:
        with open('list_of_movies.txt','r') as f:
            file_list = f.readlines()
    else:
        file_list = getfilepath(os.getcwd())
    
    add_orig_files_to_dict(file_list)
    show_dict()
    
    for file in os.listdir():
        for text_num in range(len(remove_text_list)):
            match = re.search(re_compiled[text_num], file)
            if match:
                # print(re_compiled[text_num])
                # # file = remove_text(re_compiled[text_num],file)
                # print(f'found {file}')
                pass
    


main()
# Whereever there are periods change to spaces except for the last period located in the file name

