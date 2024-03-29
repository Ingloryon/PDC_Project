import numpy as np

def getTextToTransmit():
    with open("input.txt", "r") as f:
        text_to_transmit = f.read()
    return text_to_transmit;

def encodeText( text ):
    #each character is a vector of 8 bits
    return np.unpackbits(bytearray(text,"utf-8"))

def convoluteEncoding(bits):
    b=[1,1]+list(map(lambda x:(x-0.5)*2,bits))+[1,1]
    x=[xi for j in range(2,len(b)) for xi in [b[j]*b[j-2],b[j]*b[j-1]*b[j-2]]]
    return x

def scaleArrayKTimes(k,bits):
    return [b for b in bits for i in range(k)]

def addCalibrationZeros(k,bits):
    return np.concatenate((np.zeros(k),bits))

def writeChannelInput(bits):
    with open("encoded.txt", "w") as f:
        stringToSend = "\n".join(map(lambda bit:str(int(bit)),bits))
        f.write(stringToSend)

MAX_SIZE=51200
NB_BYTES=80
BITS_PER_BYTES=8
ENCODER_FACTOR=2
NB_FINAL_DUMMY_BITS=2
BITS_ARRAY_SIZE=(NB_BYTES*BITS_PER_BYTES+NB_FINAL_DUMMY_BITS)*ENCODER_FACTOR

REPEAT_FACTOR= MAX_SIZE//(BITS_ARRAY_SIZE)-1

CALIBRATION_SIZE=BITS_ARRAY_SIZE

x=addCalibrationZeros(CALIBRATION_SIZE,scaleArrayKTimes(REPEAT_FACTOR,convoluteEncoding(encodeText(getTextToTransmit()))))

writeChannelInput(x)