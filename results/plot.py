import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np


data = np.genfromtxt('train-loss.csv', delimiter='\t')

line_loss = plt.plot(data[:,2], data[:,0],label="Episode Reward")
style.use('fivethirtyeight')
plt.legend(handles=[line_loss[0]])
plt.xlabel('Examples')
plt.ylabel('Loss')
plt.tight_layout()
plt.savefig('loss.png')
plt.show()
