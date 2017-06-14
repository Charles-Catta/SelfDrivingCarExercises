import numpy as np

# Our activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

summation = 0;
for i in range(len(inputs)):
    summation += weights[i]*inputs[i]
output = sigmoid(summation + bias)

print('Output:')
print(output)
