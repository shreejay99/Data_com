import matplotlib.pyplot as plt

data = [0,1,0,0,1,1,0,0,0,1,1]

output = [1]

c = 0 #counter

m = -1 #stores prev value
n =  1

for i in data:
    if i == 1:
        if c == 0 or c % 2 == 0:
            output.append(1)
            output.append(-1)
            m = 1
            n = -1
            c = c + 1
        else:
            output.append(-1)
            output.append(1)
            m = -1
            n = 1
            c = c + 1
    else:
        output.append(m)
        output.append(n)


time = [i for i in range(len(output))]

plt.step(time , output , marker='o')
plt.grid(True)
plt.show()