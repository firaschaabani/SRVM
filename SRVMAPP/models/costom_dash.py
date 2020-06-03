import itertools
import numpy as np
import pandas as pd
from pandas.plotting import lag_plot
#import seaborn as sns
from sklearn.model_selection import TimeSeriesSplit

import statsmodels.formula.api as smf            # statistics and econometrics
import statsmodels.tsa.api as smt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from dateutil.relativedelta import relativedelta # working with dates with style
from scipy.optimize import minimize              # for function minimization
import scipy.stats as scs

from itertools import product                    # some useful functions
#from tqdm import tqdm_notebook
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
import json
from sklearn.metrics import mean_absolute_error
#import matplotlib
#import matplotlib.pyplot as plt

#import warnings

# warnings.filterwarnings("ignore")
#warnings.simplefilter('ignore')
def cost_plot(brand):
    data = pd.read_csv(r'C:\Users\esprit\Documents\flask_app\srvm\SRVMAPP\models\bottles.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    print(data.head())
    dates = pd.date_range(start='2020-01-01', end='2020-05-31', freq='1d')
    ts = {}
    for t in data.Item.unique():
        df = data[data['Item']==t][['Date']].groupby(['Date']).size().reset_index(name='bottles').set_index('Date')
        for d in dates:
            if d not in df.index:
                df.loc[d]=0
        ts[t] = df.sort_index()
    #print(ts[brand])
    mod = sm.tsa.statespace.SARIMAX(ts[brand],
                                    order=(19, 0, 18),
                                    seasonal_order=(1, 0, 1, 30),
                                    enforce_stationarity=False,
                                    enforce_invertibility=False)
    results = mod.fit()
    #print(results.aic)
    #print(results.summary().tables[1])
    #pred = results.get_prediction(start='2020-05-31',end='2020-06-30',dynamic=False)
    #pred_ci = pred.conf_int()
    #print(pred.predicted_mean)
    #print("\n")
    #print(pred_ci)



    predmean = results.get_prediction(start='2020-01-01',end='2020-05-31',dynamic=False).predicted_mean
    prediction = pd.DataFrame(data=predmean,columns=['bottles'])
    mean_absolute_error(ts[brand],prediction)

    tsfinal = {}
    #for i in ts.keys():
    mod = sm.tsa.statespace.SARIMAX(ts[brand],
                                order=(19, 0, 18),
                                seasonal_order=(0, 0, 0, 30),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
    results = mod.fit()
    predmean = results.get_prediction(start=pd.to_datetime('2020-06-01'),end='2020-06-15',dynamic=False).predicted_mean
    prediction = pd.DataFrame(data=predmean,columns=['bottles'])
    tsfinal[brand] = pd.concat([ts[brand],prediction],axis=0)

    #figs = []

    t1=go.Scatter(x=tsfinal[brand].index, y=tsfinal[brand].bottles)
    t2=go.Scatter(x=ts[brand].index, y=ts[brand].bottles)
    tr=[t1,t2]
    graph_json=json.dumps(tr,cls=plotly.utils.PlotlyJSONEncoder)
    return (graph_json)
#fig = go.Figure(data=tr)
    
    
#    figs.append(fig)
#i = 0
#for k in tsfinal.keys():
#    pyo.plot(figs[i], filename=r'C:\Users\esprit\Documents\Plots1'+k, auto_open=False)
#    i=i+1