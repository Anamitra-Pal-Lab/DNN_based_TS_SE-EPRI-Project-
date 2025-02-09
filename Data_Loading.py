import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from scipy import stats
import numpy as np
import pandas as pd
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from scipy import stats
from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import Dense, Activation, BatchNormalization, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from tensorflow.keras.optimizers import Adam, SGD
from keras.models import load_model
import time  

from scipy.stats import zscore
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import math

# def DeNSE_data_loader_training_data():
#     df_If_mag = pd.read_csv('#Training_From_Bus_Magnitude_Data'), header = None)
#     df_If_ang = pd.read_csv('#Training_From_Bus_PhaseAngle_Data'), header = None)
#     df_It_mag = pd.read_csv('#Training_To_Bus_Magnitude_Data'), header = None)
#     df_It_ang = pd.read_csv('#Training_To_Bus_PhaseAngle_Data'), header = None)
#     df_VDATA_mag = pd.read_csv('#Training_Voltage_Magnitude_Data'), header = None)
#     df_VDATA_ang = pd.read_csv('#Training_Voltage_PhaseAngle_Data'), header = None)
    
#     return(df_If_mag, df_If_ang, df_It_mag,  df_It_ang, df_VDATA_mag, df_VDATA_ang)



def DeNSE_data_loader_training_data():
    df_If_mag = pd.read_csv('If_mag_T1_train_28000.csv', header = None)
    df_If_ang = pd.read_csv('If_ang_T1_train_28000.csv', header = None)
    df_It_mag = pd.read_csv('It_mag_T1_train_28000.csv', header = None)
    df_It_ang = pd.read_csv('It_ang_T1_train_28000.csv', header = None)
    df_VDATA_mag = pd.read_csv('VDATA_mag_T1_train_28000.csv', header = None)
    df_VDATA_ang = pd.read_csv('VDATA_ang_T1_train_28000.csv', header = None)
    
    return(df_If_mag, df_If_ang, df_It_mag,  df_It_ang, df_VDATA_mag, df_VDATA_ang)

def DeNSE_data_loader_testing_data():
    df_If_mag = pd.read_csv('If_mag_T1_28000.csv', header = None)
    df_If_ang = pd.read_csv('If_ang_T1_28000.csv', header = None)
    df_It_mag = pd.read_csv('It_mag_T1_28000.csv', header = None)
    df_It_ang = pd.read_csv('It_ang_T1_28000.csv', header = None)
    df_VDATA_mag = pd.read_csv('VDATA_mag_T1_28000.csv', header = None)
    df_VDATA_ang = pd.read_csv('VDATA_ang_T1_28000.csv', header = None)
    
    return(df_If_mag, df_If_ang, df_It_mag,  df_It_ang, df_VDATA_mag, df_VDATA_ang)

def Load_Training_Data(filepath, n):
    
    # Reading the current and voltage data
    # Reading the voltages and current measurements to pandas daraframes
    # If - from bus current
    # It - to bus current
    # V - voltage
    # mag - magnitude
    # ang - phase angle  

    df_If_ang = pd.read_csv(filepath+('If_ang_train_T'+str(n)+'_12am.csv'), header = None)
    df_If_mag= pd.read_csv(filepath+('If_mag_train_T'+str(n)+'_12am.csv'), header = None)
    df_It_ang= pd.read_csv(filepath+('It_ang_train_T'+str(n)+'_12am.csv'), header = None)
    df_It_mag= pd.read_csv(filepath+('It_mag_train_T'+str(n)+'_12am.csv'), header = None)
    df_VDATA_mag = pd.read_csv(filepath+('VDATA_mag_train_T'+str(n)+'_12am.csv'), header = None)
    df_VDATA_ang = pd.read_csv(filepath+('VDATA_ang_train_T'+str(n)+'_12am.csv'), header = None)
    df_From_To_buses_118 = pd.read_csv(r'From_To_buses_118.csv', header = None)
    return(df_VDATA_mag, df_VDATA_ang, df_If_mag, df_If_ang, df_It_mag, df_It_ang, df_From_To_buses_118)

def Load_Testing_Data(filepath, n):

    df_If_ang = pd.read_csv(filepath+('If_ang_test_T'+str(n)+'_12am.csv'))
    df_If_mag= pd.read_csv(filepath+('If_mag_test_T'+str(n)+'_12am.csv'))
    df_It_ang= pd.read_csv(filepath+('It_ang_test_T'+str(n)+'_12am.csv'))
    df_It_mag= pd.read_csv(filepath+('It_mag_test_T'+str(n)+'_12am.csv'))
    df_VDATA_mag = pd.read_csv(filepath+('VDATA_mag_test_T'+str(n)+'_12am.csv'))
    df_VDATA_ang = pd.read_csv(filepath+('VDATA_ang_test_T'+str(n)+'_12am.csv'))
  
   
    print('Read the test csv files')

    return(df_VDATA_mag, df_VDATA_ang, df_If_mag, df_If_ang, df_It_mag, df_It_ang)
           

def Load_Testing_Transfer_Learning_Data(filepath, n):
    
    # Reading the current and voltage data
    # Reading the voltages and current measurements to pandas daraframes
    # If - from bus current
    # It - to bus current
    # V - voltage
    # mag - magnitude
    # ang - phase angle  

    df_If_ang = pd.read_csv(filepath+('If_ang_test_T'+str(n)+'_12am.csv'))
    df_If_mag= pd.read_csv(filepath+('If_mag_test_T'+str(n)+'_12am.csv'))
    df_It_ang= pd.read_csv(filepath+('It_ang_test_T'+str(n)+'_12am.csv'))
    df_It_mag= pd.read_csv(filepath+('It_mag_test_T'+str(n)+'_12am.csv'))
    df_VDATA_mag = pd.read_csv(filepath+('VDATA_mag_test_T'+str(n)+'_12am.csv'))
    df_VDATA_ang = pd.read_csv(filepath+('VDATA_ang_test_T'+str(n)+'_12am.csv'))
  
   
    print('Read the test csv files')

    return(df_VDATA_mag, df_VDATA_ang, df_If_mag, df_If_ang, df_It_mag, df_It_ang)
    
