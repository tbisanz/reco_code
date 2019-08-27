import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

runs = [4008, 4019, 4020, 4023, 4028, 4031, 4032, 4033, 4034, 4035, 4036, 4037, 4038, 4042, 4045, 4049, 4055, 4058, 4062, 4063, 4065, 4066, 4067, 4068, 4070, 4072, 4074, 4075, 4076, 4077, 4078, 4083, 4084, 4085, 4086, 4096, 4097, 4098, 4102, 4103, 4110, 4112, 4113, 4115, 4116, 4117, 4118, 4120, 4121, 4122, 4123, 4126, 4127, 4129, 4132, 4134, 4137, 4139, 4140, 4142, 4143, 4144, 4145, 4149, 4150, 4152, 4153, 4154, 4155, 4157, 4158, 4159]

align_runs = [4031, 4032, 4033, 4034, 4035, 4036, 4037, 4074, 4103]

sensors = [0,1,2,21,22,3,4,5]

x_pos_array = {}
y_pos_array = {}
gamma_array = {}

for sensor in range(0,8):
    x_pos_array[sensor] = []
    y_pos_array[sensor] = []
    gamma_array[sensor] = []

pos_x_file = open("posX.txt","w") 
pos_y_file = open("posY.txt","w") 
gamma_file = open("gamma.txt","w") 
 
for run in runs:
    tree = ET.parse('gear_batch100'+str(run)+'_pre_aligned_second.xml')
    root = tree.getroot()
    layers = root[2][0][3]

    for i in range(0,8):
        layer = layers[i]
        ladder = layer[0]
        attribs = ladder.attrib
        posX = attribs["positionX"]
        posY = attribs["positionY"]
        gamma =attribs["rotationXY"]
            
        if(i==1):
            pos_x_file.write(posX+'\n'); 
            pos_y_file.write(posY+'\n'); 
            gamma_file.write(gamma+'\n'); 

        x_pos_array[i].append(posX)
        y_pos_array[i].append(posY)
        gamma_array[i].append(gamma)


for i in range(0,8):
    plt.subplot(2, 4, i+1)
    array = np.asarray(gamma_array[i]).astype(float)
    print("Average gamma on detector: "+str(i)+" is: "+str(np.average(array)))
    #plt.hist(array, bins=10)
    plt.plot(y_pos_array[i])
plt.show()
