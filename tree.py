import os
path = "/Users/payel/Python/PythonFundamentals.Exercises.Part8"

def get_filename(file_path:str):
    fileName = []
    for path,directories,files in os.walk(file_path):
        for file in files:
            fileName.append(path + file)
        # print(path,fileName)
        return fileName
list1 = get_filename(path)

def write_file(list):
    with open('/Users/payel/Python/PythonFundamentals.Exercises.Part8/tree.txt','w') as fp:
        for name in list:
            fp.write('%s\n'% name)


write_file(list1)