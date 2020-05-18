import numpy as np

# Gets the text to be transmitted from the corresponding file and return it as a string
def getTextToTransmit():

	with open("files/text_to_transmit.txt", "r") as f:
		text_to_transmit = f.read()

	return text_to_transmit;

# Takes a string as input and returns an array of its UTF-8 binary encoding
def encodeText( text ):
	#each character is a vector of 8 bits
	return np.unpackbits(np.fromstring(text, dtype="uint8"))
	
# Takes an array of binary UTF-8 characters, returns ??
def waveformFormer( encodedText ):

	w = []

	# TODO: How do we want to transmit our characters ? 
	#-> sampling freq / period
	#-> nb of samples per bit
	#-> Best techniques to counter AWGN effect

# Takes a string and writes it in the file corresponding to the channel input
def writeChannelInput( output ):
	with open("files/channel_input.txt", "w") as f:
		f.write(output)

		
encodedText = encodeText( getTextToTransmit() )
writeChannelInput( waveformFormer(encodedText) )


