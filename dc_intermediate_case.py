import numpy as np
import matplotlib.pyplot as plt

# set seed
np.random.seed(123)

all_walks = []
for i in range(500):
    # set random_walk
    random_walk = [0]
    for x in range(100):
        # set step
        step = random_walk[-1]
        # simulate a dice roll
        dice = np.random.randint(1, 7)
        # determine outcome
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)
        # add clumsiness
        if np.random.rand() <= 0.001:
            step = 0
        # add results to random walk
        random_walk.append(step)
    # add result to list of all random walks
    all_walks.append(random_walk)

# create figure showing all walks
np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)
plt.plot(np_aw_t)
plt.show()

# create histogram to show all end heights
ends = np_aw_t[-1, ]
plt.hist(ends)
plt.show()

# calculate probability that you reach 60 steps or higher
prob = len(ends[ends >= 60]) / len(ends)
print(prob)