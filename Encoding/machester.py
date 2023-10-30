import matplotlib.pyplot as plt

data = [0,1,0,0,1,1,1,0]
output = [1]

for i in data:
    if i == 1:
        output.append(1)
        output.append(-1)
    else:
        output.append(-1)
        output.append(1)

time = [i for i in range(len(output))]

plt.step(time , output , marker = "o")
plt.grid(True)
plt.show()
