import flask
from flask import request

from utilies import get_config, get_files_from_folder_with_suffix, decompress

import laser_welding
import self_adapting

'''
Global params
'''
folder_list = []



'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
'''
# 创建一个服务，把当前这个python文件当做一个服务
server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/api/upload', methods=['POST'])
def saveAndDecompressFile():
    '''
    receive: file
    return: list
    '''
    file = request.files['file']
    if not file :
        return 'Receive file failed, please reupload it.'
    
    print('Receive file named: {fileName}'.format(fileName=file.filename))
    
    # 文件写入磁盘
    print('Begin saving file ...')
    file.save(file.filename)
    
    print("Start decompressing file ...")
    global folder_list 
    folder_list = decompress([file.filename, ])
    
    
    print('Begin looking up the folders\' name')
    dataFiles = get_files_from_folder_with_suffix(folder_list,['.txt','.xlsx','.csv','.xls'])

    
    print(dataFiles)
    # return decompressed_folders
    return dataFiles

@server.route('/api/param', methods=['POST'])
def receiveParam():
    params = request.json
    print(params)
    
    for key in params.keys():
        print(key, params[key])
    
    return "receive"

@server.route('/api/getprocesses', methods=['GET'])
def getprocesses():
    '''
    receive: none
    return: dict
    '''
    config = get_config()
    
    if not 'processes' in config.keys():
        print('config file not have processes information, please check!')
        return 'False'
    
    return config['processes']

@server.route('/api/getRecommend', methods=['GET'])
def recommend():
    '''
    receive: str
    return: list
    '''
    print('Receiving GET request on /api/getRecommend ...')
    re = laser_welding.run()
    print('After executing laser_welding.run() ... ')
    params = re['result'].iloc[0].to_dict()
    print('Returning ...')
    return params

@server.route('/api/selfAdapting', methods=['GET'])
def get_self_adapting():
    '''
    receive: str
    return: dict 
    '''
    print('Receiving GET request on /api/selfAdapting ...')
    sine = self_adapting.run('sine')
    step = self_adapting.run('step')
    print('After getting result of sine and step ...')
    return_list = {}
    return_list['sine'] = sine
    return_list['step'] = step
    print('Returning ...')
    return return_list


if __name__ == '__main__':
    '''
    port: The port is going to listen
    host: 0.0.0.0 stand for every ip could access.
    '''
    server.run(debug=True, port=5174, host='0.0.0.0')