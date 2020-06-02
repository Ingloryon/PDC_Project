import numpy as np

def getChannelOutput():
    with open("files/channel_output.txt", "r") as f:
        return np.array(f.read().split('\n'))  

def nTupleFormer( received ):


def decoder( text ):


sampleNb = 100 
samplingFrequency = 12000
samplingPeriod = 1 / samplingFrequency

decoder( nTupleFormer( getChannelOutput() ) )