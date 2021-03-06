import numpy as np 
import matplotlib.pyplot as plt 
import re

fname1 = 'train_logs_6_8.txt'
fname2 = 'train_logs_3456_5678.txt'

step = 100
loss_list_static = []
with open(fname1, 'r') as f:
	for line in f.readlines():
		line = line.strip()
		if 'Iter' in line and 'Loss' in line:
			loss = re.findall('\d+\.\d+', line)[4]
			loss_list_static.append(float(loss))

loss_list_static = np.array(loss_list_static)[::step]

loss_list_prog = []
with open(fname2, 'r') as f:
	for line in f.readlines():
		line = line.strip()
		if 'Iter' in line and 'Loss' in line:
			loss = re.findall('\d+\.\d+', line)[4]
			loss_list_prog.append(float(loss))

loss_list_prog = np.array(loss_list_prog)[::step]

epoch_list = np.arange(1,len(loss_list_static)+1)*step

plt.plot(epoch_list, loss_list_static)
plt.plot(epoch_list, loss_list_prog)
plt.grid()

plt.title('Training Loss - Epoch')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend(['static 6/8', 'progressive 3456_5678'])

plt.savefig('loss-epoch.jpg')
plt.show()