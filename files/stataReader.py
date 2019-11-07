import pandas as pd


def readSTATA(filename):
    rdr = pd.read_stata(filename)
    return rdr

