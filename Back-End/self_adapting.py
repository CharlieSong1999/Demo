import numpy as np
import pandas as pd
import math
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import json


def predict_actual_position(reg, command_position):
    # use the trained linear regression model to predict the following_error
    following_error_prediction = reg.predict(np.array(command_position).reshape(-1, 1))[0]
    # calculate the new_command_position by subtracting the predicted following_error from the input command_position
    new_command_position = command_position - following_error_prediction
    # set the new_actual_position equal to the new_command_position
    new_actual_position = new_command_position
    return new_actual_position

def predict_final_actual_position(reg, command_position, max_iter=100):
    prd_actual_position = predict_actual_position(reg, command_position)
    
    return prd_actual_position

def read_data(name):
    config = get_read_data_config(name)
    data = pd.read_csv(config[0], sep=' ', skiprows=config[1])
    return data

def get_read_data_config(name):
    if name == 'sine':
        return ['sine.txt', 0]
    elif name == 'step':
        return ['Step.txt', 3]
    else:
        print ('Unknown read data config name, please check it out.')
        exit

def run(name):
    
    data = read_data(name)
    return_json = {}
    
    # convert time object to a 2-dimensional array
    time_array = data['Time(ms)'].values.reshape(-1, 1)
    
    
    return_json['Time(ms)'] = time_array.reshape(-1).tolist()
    
    following_error = (data["Command-Position"] - data['Actual-Position']).values.reshape(-1,1)
    
    return_json['Following-Error'] = list(zip(return_json['Time(ms)'],following_error.reshape(-1).tolist()))
    
    reg = LinearRegression().fit(time_array, following_error)
    
    # input new command position value
    command_position = data['Command-Position'].values.reshape(-1,1) 
    
    # call the predict_actual_position function to get the new_actual_position
    new_actual_position = predict_final_actual_position(reg, command_position)   
    
    new_following_error = abs(command_position - new_actual_position)
    
    return_json['Command_Position'] = list(zip(return_json['Time(ms)'],command_position.reshape(-1).tolist()))
    return_json['new_actual_position'] = list(zip(return_json['Time(ms)'],new_actual_position.reshape(-1).tolist()))
    return_json['new_following_error'] = list(zip(return_json['Time(ms)'],new_following_error.reshape(-1).tolist()))
    
    # reduce the size of return list for better demonstration performance.
    for key in return_json.keys():
        return_json[key] = [i for index,i in enumerate(return_json[key]) if index%5==0 ]
    
    return return_json
    
if __name__ == '__main__':
    run()