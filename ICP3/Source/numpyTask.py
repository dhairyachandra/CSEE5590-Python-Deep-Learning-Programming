import numpy as np

# generating random vector
num = np.random.randint(1, 20, 15)
print(num)

# reshaping in 3 by 5
num = np.reshape(num, (3, 5))
print(num)

# replace max by 0
print(np.where(num == np.max(num, axis=1).reshape(-1,1), 0, num))