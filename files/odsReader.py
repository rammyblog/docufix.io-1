
import pandas as pd

def odsFileReader(filename):
    rdr = pd.read_excel(filename, engine='odf')
    return rdr