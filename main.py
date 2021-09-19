# This is an attempt to make a program that adjusts the colors of scatter plots
# such that the values of the output have colors which line up with the colormap.
# For example, if red represents high values and blue represents low values,
# then, the dots near the top of the plot will be redder than the dots at the bottom.
import matplotlib.pyplot as plt
import numpy as np

output_count = 100 # Need this as a global variable to run smoother.
x = np.arange(0, output_count)
y = np.random.randint(100, size=output_count)

# Make a colors array to pull values of the colormap from
# this array needs to have numerical values to represent the
# values of the color map.
colors = np.arange(0, 100)
final_colors = np.array([])

# Much like the colors array, the sizes array is determined by the y-value it receives.
sizes = np.arange(0, 100) # 100 is the max because y's max is also 100.
final_sizes = np.array([])


def color_sorter(num):
    # Value of output = its value on the colormap.
    # This let's us have dynamic coloring.
    # This constrains the y-axis to be 100 at most since the colormap
    # only goes to 100.
    return colors[num]

def size_sorter(num):
    # Literally just scales it to its own value.
    # Allows for dynamic sizing.
    return sizes[num]



# Final_colors is iterated through each iteration. The update is adding a value as
# determined by the color picker function. The current iteration of y's value is
# judged via the logic and returns the proper color.
for element in y:
    final_colors = np.append(final_colors, color_sorter(element))

for element in y:
    final_sizes = np.append(final_sizes, 10 * size_sorter(element))
    # The 10 is a random scalar to make the proportions bigger.

plt.scatter(x, y, s=final_sizes, c=final_colors, cmap='CMRmap', alpha=0.5)

plt.show()
