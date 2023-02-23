import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def run(fn='./v61.csv'):

    experiment_record = {}

    # load data set
    experiment_record['fn'] = fn
    dataset = pd.read_csv(fn)

    x_train, x_test, y_train, y_test = train_test_split(dataset[dataset.columns[0:6]], 
                                                        dataset[dataset.columns[6]], 
                                                        test_size=0.25) 

    # data normalization
    std = StandardScaler()
    # std = PolynomialFeatures(1)
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    # logistic regression binary-classification
    lg = LogisticRegression(solver='saga', C=25, max_iter=200)  # 默认使用L2正则化避免过拟合，C=1.0表示正则力度(超参数，可以调参调优)
    # lg = RandomForestRegressor(n_estimators= best_n_estimator)
    lg.fit(x_train, y_train)
    experiment_record['coefficient'] = lg.coef_

    # accuracy
    experiment_record['score'] = lg.score(x_test, y_test)

    # emunarate all combination of control parameters
    new_data = []
    for i1 in range(900,1201):
        for i2 in np.arange(0.8, 1.3, 0.1):
            for i3 in range (10,20):
                for i4 in range (-2,3):
                    for i5 in range (-15,16):
                        for i6 in np.arange (0.5, 0.79, 0.1):
                            list = [i1,i2,i3,i4,i5,i6]
                            new_data.append(list)
                    
    experiment_record['size of alternative options'] = len(new_data)    
    # normalize and predict 
    new_test = pd.DataFrame(new_data, columns=dataset.columns[0:6])
    new_test = std.transform(new_test)
    new_predict = lg.predict(new_test)

    # add the predict term into data-frame
    for index,data in enumerate(new_data):
        data.append(new_predict[index])

    new_test = pd.DataFrame(new_data, columns=dataset.columns)

    # pick up those do not yield cracks
    parameters_no_crack = new_test[new_test['cracking in the weld metal']==1]

    experiment_record['size of possible options'] = len(parameters_no_crack)

    # pick up the best one
    
    # best_option = parameters_no_crack[parameters_no_crack['power (W)']==parameters_no_crack['power (W)'].min()] [parameters_no_crack['welding speed (m/min)']==parameters_no_crack['welding speed (m/min)'].max()][parameters_no_crack['gas flow rate (l/min)']==parameters_no_crack['gas flow rate (l/min)'].min()]
    best_option = parameters_no_crack[(parameters_no_crack['power (W)']==parameters_no_crack['power (W)'].min())
                                      &(parameters_no_crack['welding speed (m/min)']==parameters_no_crack['welding speed (m/min)'].max())
                                      &(parameters_no_crack['gas flow rate (l/min)']==parameters_no_crack['gas flow rate (l/min)'].min())
                                      &(parameters_no_crack['focal position (mm)']==parameters_no_crack['focal position (mm)'].min())
                                      &(parameters_no_crack['material thickness (mm)']==parameters_no_crack['material thickness (mm)'].min())]

    experiment_record['size of best options'] = len(best_option)
    experiment_record['result'] = best_option
    
    return experiment_record

if __name__ == "__main__":
    run()