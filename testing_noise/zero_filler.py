import numpy as np

output = []

for i in range(0,50000):
	output.append(0)

output = np.ravel(np.array(output)).astype("str") 

with open("noise_input.txt", "w") as f:
	f.write("\n".join(output))