import matplotlib.pyplot as plt

data = [1,0,1,1,0]

output = [0]

for i in data:
    if i == 1:
        output.append(1)
        output.append(0)
    else:
        output.append(-1)
        output.append(0)

time = [i for i in range(len(output))]

plt.step(time , output)
plt.grid(True)
plt.show()
