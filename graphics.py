import numpy as np
import matplotlib.pyplot as plt

#Filepath with file to read
filepath = 'blocksTimes.txt'

#Declaration of x
x = []

#Declaration of y
y = []

#Open the file and read the lines adding to the list each line int and their time
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       x.append(cnt)
       y.append(line.strip())
       line = fp.readline()
       cnt += 1


 
#plote of a bar graphic type
yFloat = [float(i) for i in y]

index = np.arange(len(x))
plt.bar(index, yFloat, color="red")
plt.xlabel('Blocos', fontsize=10)
plt.ylabel('Tempo execução (s)', fontsize=10)
plt.title('Proof of Work')
plt.show()
