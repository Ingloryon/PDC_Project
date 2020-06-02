import numpy as np

def getChannelOutput():
    with open("received.txt", "r") as f:
        bitArray = np.array(f.read().split('\n'))
        return bitArray[:-1];

def decoder( bitArray ):
	binaryResult = []
	size = len(bitArray)
	iterations = int(size / SAMPLES_PER_BIT)

	for i in range(0, iterations):
		bit = bitArray[i*SAMPLES_PER_BIT: (i+1)*SAMPLES_PER_BIT].astype(np.float)
		bitMean = bit.sum() / SAMPLES_PER_BIT

		if bitMean > 0:
			binaryResult.append(1)
		else:
			binaryResult.append(0)

	binaryResult = np.array(binaryResult)

	binary_decoded = np.packbits(binaryResult.reshape(-1, 8)) 

	decoded = []
	for i in range(0, len(binary_decoded)):
		try:
			char = binary_decoded[i].tostring().decode("utf-8")
			decoded.append(char)
		except UnicodeDecodeError:
			decoded.append("0")

	with open("output.txt", "w") as f:
	    f.write("".join(decoded))

SAMPLES_PER_BIT = 78 

decoder( getChannelOutput() )
