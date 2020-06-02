import numpy as np


fin = "noise_output.txt"
with open(fin, "r") as f:
    received = np.array(f.read().split('\n'))[:-1].astype("float64")


mean_received = received.sum() / len(received)

print("The estimated channel noise bias is b =", mean_received)