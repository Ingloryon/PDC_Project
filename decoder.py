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

	print(binaryResult)

	decoded = np.packbits(binaryResult.reshape(-1, 8)).tostring().decode("utf-8")

	with open("output.txt", "w") as f:
	        f.write(decoded)

SAMPLES_PER_BIT = 78 

decoder( getChannelOutput() )





