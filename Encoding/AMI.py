import matplotlib.pyplot as plt

data = [0,1,0,0,1,1,1,0,0,1,1]

output = [0]

c = 0 #counter

for i in data:
    if i == 1:
        if c == 0 or c % 2 == 0:
            output.append(1)
        
            c = c + 1
        else:
            output.append(-1)
           
            c = c + 1
    else:
        output.append(0)


time = [i for i in range(len(output))]

plt.step(time , output , marker = '*')
plt.grid(True)
plt.show()