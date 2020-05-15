import numpy as np

def getTextToTransmit():

	with open("files/text_to_transmit.txt", "r") as f:
		text_to_transmit = f.read()

	return text_to_transmit;

def encodeText():
	return np.unpackbits(np.fromstring(getTextToTransmit(), dtype="uint8"))
