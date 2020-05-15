import numpy as np

def getTextToTransmit():

	with open("files/text_to_transmit.txt", "r") as f:
		text_to_transmit = f.read()

	return text_to_transmit;

def encodeText():
	return np.unpackbits(np.fromstring(getTextToTransmit(), dtype="uint8"))

def waveformFormer( encodedText ):

	w = []

	# TODO: How do we want to transmite our characters ?

def writeChannelOutput():
	encodedText = encodeText()
	output = waveformFormer(encodedText)

	with open("files/bytes_to_transmit.txt", "w") as f:
		f.write(output)


writeChannelOutput()


