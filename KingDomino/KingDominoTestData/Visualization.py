import numpy as np
import matplotlib.pyplot as plt

# Define the color ranges and labels
color_ranges = [
    ((22, 34), (209, 260), (119, 201), "Field"),
    ((29, 63), (85, 201), (36, 84), "Forest"),
    ((74, 110), (192, 260), (105, 192), "Lake"),
    ((31, 50), (161, 237), (73, 162), "Grassland"),
    ((19, 39), (57, 170), (52, 134), "Swamp"),
    ((25, 54), (57, 140), (43, 91), "Mine"),
    ((17, 74), (40, 166), (37, 149), "Home")
]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define the number of points for the gradient
num_points = 100

# Create a gradient plot for each color range
for (h_range, s_range, v_range, label) in color_ranges:
    h_min, h_max = h_range
    s_min, s_max = s_range
    v_min, v_max = v_range

    hue_gradient = np.linspace(h_min, h_max, num_points)
    saturation_gradient = np.linspace(s_min, s_max, num_points)
    value_gradient = np.linspace(v_min, v_max, num_points)

    for i in range(num_points):
        color = (hue_gradient[i] / 360, saturation_gradient[i] / 255, value_gradient[i] / 255)
        ax.scatter(hue_gradient[i], saturation_gradient[i], c=[color], label=label if i == 0 else "")

# Set labels and legend
ax.set_xlabel("Hue")
ax.set_ylabel("Saturation")
ax.set_title("Color Ranges Visualization")
ax.legend()

# Show the plot
plt.show()
