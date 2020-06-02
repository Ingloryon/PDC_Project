import numpy as np


# Gets the text to be transmitted from the corresponding file and return it as a string
def getTextToTransmit():

	with open("input.txt", "r") as f:
		text_to_transmit = f.read()

	return text_to_transmit;


# Takes a string as input and returns an array of its UTF-8 binary encoding
def encodeText( text ):
	#each character is a vector of 8 bits
	return np.unpackbits(np.fromstring(text, dtype="uint8"))


# Takes an array of binary UTF-8 characters, returns ??
def tupleFormer( encodedText ):
    repeated_bits = []
    
    for bit in encodedText:
        for i in range(0, SAMPLES_PER_BIT):
        	repeated_bits.append(bit);
    
    return np.ravel(np.array(repeated_bits)).astype("str") 


# Takes a string and writes it in the file corresponding to the channel input
def writeChannelInput( output ):
	with open("encoded.txt", "w") as f:
		f.write("\n".join(output))


SAMPLES_PER_BIT = 78 

encodedText = encodeText( getTextToTransmit() )
writeChannelInput( tupleFormer(encodedText) )


