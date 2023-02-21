import rarfile
import yaml
import gzip
import tarfile
import os
import zipfile

'''
global param
'''
config_yaml = './config/config.yaml'


'''
decompressing files
'''
def ungz(filename):
    filename = filename[:-3] # gz文件的单文件解压就是去掉 filename 后面的 .gz
    gz_file = gzip.GzipFile(filename)
    with open(filename, "w+") as file:
        file.write(gz_file.read())
        return filename  # 这个gzip的函数需要返回值以进一步配合untar函数

def untar(filename):
    tar = tarfile.open(filename)
    names = tar.getnames()
    # tar本身是将文件打包，解除打包会产生很多文件，因此需要建立文件夹存放
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    for name in names:
        tar.extract(name, filename + "_dir/")
    tar.close()

def unzip(filename):
    zip_file = zipfile.ZipFile(filename)
    # 类似tar解除打包，建立文件夹存放解压的多个文件
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")  
    for names in zip_file.namelist():
        if not str(names).startswith('__MACOSX/'):
            zip_file.extract(names, filename + "_dir/")
    zip_file.close()
    


def unrar(filename):
    rar = rarfile.RarFile(filename)
    if not os.path.isdir(filename + "_dir"):
        os.mkdir(filename + "_dir")
    os.chdir(filename + "_dir")
    rar.extractall()
    rar.close()

def decompress(filename_list):
    foldername_list = []
    for filename in filename_list:
        if '.' in filename:
            suffix = filename.split('.')[-1]
            if suffix == 'gz':
                new_filename = ungz(filename)
                os.remove(filename)
                if new_filename.split('.')[-1] == 'tar':
                    untar(new_filename)
                    os.remove(new_filename)  
            if suffix == 'tar':
                untar(filename)
                os.remove(filename)
            if suffix == 'zip':
                unzip(filename)
                os.remove(filename)
            if suffix == 'rar':
                unrar(filename)
                os.remove(filename)
        foldername_list.append(filename+'_dir')
    return foldername_list

# 
def get_files_from_folder_with_suffix(folder_list, accept_suffix):
    
    data_files = []
    for folder in folder_list:
        for path, dir_list, file_list in os.walk(folder):
            for file in file_list:
                if os.path.splitext(file)[-1] in accept_suffix:
                    data_files.append(os.path.join(path, file))
    
    return data_files

def get_config():
    f = open(config_yaml, 'r', encoding='utf-8')
    cfg = f.read()
    print(cfg)

    config = yaml.load(cfg,Loader=yaml.FullLoader)  # 用load方法转字典
    print(config)
    return config

