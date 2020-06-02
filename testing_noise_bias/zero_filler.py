import numpy as np

output = []

for i in range(0,70):
	output.append(1)

output = np.ravel(np.array(output)).astype("str") 

with open("noise_input.txt", "w") as f:
	f.write("\n".join(output))
