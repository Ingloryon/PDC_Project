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
	
# Takes as input the frequency f of the sinusoid, the number of samples and the sampling period.
# Returns the corresponding sinusoid function
def sinusoid(f, sampleNb, samplingPeriod):
    x = np.arange(sampleNb) * samplingPeriod
    return np.sin(2 * np.pi * f * x)
	
# Takes an array of binary UTF-8 characters, returns ??
def waveformFormer( encodedText ):
    waves = []
    
    for bit in encodedText:
        if x == 0:
            waves.append(sinusoid(2000, sampleNb, samplingPeriod))
        else:
            waves.append(sinusoid(4000, sampleNb, samplingPeriod))
            
    return np.ravel(np.array(w))

# Takes a string and writes it in the file corresponding to the channel input
def writeChannelInput( output ):
	with open("files/channel_input.txt", "w") as f:
		f.write(output)

sampleNb = 100 
samplingFrequency = 12000 #nombres déterminés arbitrairement, comment decider des "bonnes valeurs" ?
samplingPeriod = 1 / samplingFrequency
		
encodedText = encodeText( getTextToTransmit() )
writeChannelInput( waveformFormer(encodedText).astype("str") )

# TODO: How do we want to transmit our characters ? 
#-> sampling freq / period
#-> nb of samples per bit
#-> Best techniques to counter AWGN effect



