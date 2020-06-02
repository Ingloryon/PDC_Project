import numpy as np

def getChannelOutput():
    with open("received.txt", "r") as f:
        bitArray = np.array(f.read().split('\n'))
        return list(map(lambda x: float(x),bitArray[:-1]))
    #return list(x)
    
def getBitsFromY(Y):
    bias=np.mean(Y[:CALIBRATION_SIZE])
    print("bias =",bias)
    
    #group by bloc of size 38 starting at 1280 -> get 1280 bits
    bits=[np.mean(Y[CALIBRATION_SIZE+j*REPEAT_FACTOR:CALIBRATION_SIZE+(j+1)*REPEAT_FACTOR])-bias for j in range(BITS_ARRAY_SIZE)]
    
    return bits

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

y=getBitsFromY(getChannelOutput())

nb_states=int(len(y)/2)
#attention on ajoute un etat de plus pour
#compter l'état 0
states_scores=np.zeros((nb_states+1,4))

previous_was=np.zeros((nb_states,4),dtype='int')

#To prevent from taking those path on the fist state
states_scores[0][1]=float("-inf")
states_scores[0][2]=float("-inf")
states_scores[0][3]=float("-inf")

#To prevent from taking those path on the second state
states_scores[1][2]=float("-inf")
states_scores[1][3]=float("-inf")

trellis=[]
trellis.append(((0,(1,1)),(2,(-1,-1))))
trellis.append(((0,(-1,-1)),(2,(1,1))))
trellis.append(((1,(1,-1)),(3,(-1,1))))
trellis.append(((1,(-1,1)),(3,(1,-1))))

bit_from_previous=[1,-1,1,-1]

for i in range(1,len(states_scores)):
    for j in range(4):
        a=states_scores[i-1][trellis[j][0][0]]+dot(trellis[j][0][1],y[(i-1)*2:i*2])
        b=states_scores[i-1][trellis[j][1][0]]+dot(trellis[j][1][1],y[(i-1)*2:i*2])
        
        states_scores[i][j]=max(a,b)
        previous_was[i-1][j]= trellis[j][0][0] if a>b else trellis[j][1][0]

j=0
bits=[]
for i in range(len(previous_was))[::-1]:
    prev=previous_was[i][j]
    
    bits=[bit_from_previous[j]]+bits
    
    j=prev

bits=list(map(lambda x:int((x+1)/2),bits))

binaryResult = np.array(bits[:-2])

binary_decoded = np.packbits(binaryResult.reshape(-1, 8)) 

decoded = []
for i in range(0, len(binary_decoded)):
    char = binary_decoded[i].tostring().decode("utf-8")
    decoded.append(char)

with open("output.txt", "w") as f:
    f.write("".join(decoded))