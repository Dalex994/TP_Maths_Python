import matplotlib.pyplot as plt

# define the range
xmin, xmax = 0, 10

# create the plot
fig, ax = plt.subplots()
x_coords, y_coords = ax.plot(xmin, xmax)

print('x coordinates:', x_coords)
print('y coordinates:', y_coords)

# show the plot
plt.show()
