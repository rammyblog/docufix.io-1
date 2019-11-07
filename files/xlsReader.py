import pandas as pd

def xlsFileReader(filename):
    rdr = pd.read_excel(filename)
    return rdr