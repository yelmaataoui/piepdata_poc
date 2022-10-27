import pandas as pd
def extract(csv_file):
    '''extract csv to pandas dataframe'''
    dataframe =  pd.read_csv(csv_file, sep=",", encoding = 'utf8')
    return dataframe