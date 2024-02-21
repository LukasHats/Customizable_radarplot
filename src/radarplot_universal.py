import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.cm import ScalarMappable
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from textwrap import wrap

#Create a list of attributes the user wants to display on the plot
attributes = []
while True:
    attributes.append(input("Please enter a attribute you want to have displayed on the plot. Only enter 1 at the time and a maximum of 12: ").strip())
    while True:
        decider = input("Do you want to enter another attribute? [y/n]: ").strip().lower()
        if decider != "y" and decider != "n":
            continue
        else:
            break
    if decider == "y":
        continue
    elif len(attributes) > 12:
        print("You have added too many attributes to the list, the list will be cleared and you have to start over again. Sorry!")
        attributes = []
        print("Attribute list cleared")
        continue
    else:
        break
# Create a dictionary 
user_knowledge = {}
for attribute in attributes:
    while True:
        skillpoint = int(input(f"On a scale of 0-10, how would you rate your knowledge or skill in {attribute}?: "))
        if 0 <= skillpoint <= 10:
            user_knowledge[attribute] = skillpoint
            break
        else:
            print("Invalid input, please input a valid value between 0 and 10")

# Create dataframe from the dictionary and sort it
df = pd.DataFrame(list(user_knowledge.items()), columns=['attribute', 'skill']).sort_values("skill", ascending=False)

# Inspired by https://python-graph-gallery.com/web-circular-barplot-with-matplotlib/
## Get values for the x-axis
angles = np.linspace(0.05, 2 * np.pi - 0.05, len(df), endpoint = False)

skillpoints = df["skill"].values
attribute_labels = df["attribute"].values

#Customize font
plt.rcParams["text.color"] = "#1f1f1f"

#norm colors and map them onto the cmap using the skillpoints as range, adding a bit space until max. of the viridis palette for better visualization, otherwise yellow is very bright
cmap = plt.get_cmap("viridis")
norm = mpl.colors.Normalize(vmin=skillpoints.min(), vmax=skillpoints.max()+0.2)
colors = cmap(norm(skillpoints))

# get polar projection for circle plot
fig, ax = plt.subplots(figsize=(9, 12.6), subplot_kw={"projection": "polar"})
# background to white
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Set axes ylims and offset (means rotation for approx. 60 degrees in this case)
ax.set_theta_offset(1.2 * np.pi / 2)
ax.set_ylim(-4, 11)

# Create Barplots and vlines on different levels, vlines are only for orientation
ax.bar(angles, skillpoints, color=colors, alpha=0.9, width=0.45, zorder=10)
ax.vlines(angles, 0, 10, color="#1f1f1f", ls=(0, (4, 4)), zorder=11)

# With the wrap function we want to write code over several lines, not breaking words and take min of 5 chars in a word but dont break words longer than 5 chars
attribute_labels = ["\n".join(wrap(r, 5, break_long_words=False)) for r in attribute_labels]

# Set the labels for x_axis
ax.set_xticks(angles)
ax.set_xticklabels(attribute_labels, size=12);

# Enhance the plot by removing unneccassary stuff
ax.xaxis.grid(False)
yheights = [0, 2, 4, 6, 8, 10]
ax.set_yticklabels([])
ax.set_yticks(yheights)

#Remove spines from axes
ax.spines["start"].set_visible(False)
ax.spines["polar"].set_visible(False)

#Add spave around labels of x_axis
xticks = ax.xaxis.get_major_ticks()
for xtick in xticks:
    xtick.set_pad(12)

#Add custom yticklabels and center them, adjust height a bit using pad
pad = 0.15
for y in yheights:
    ax.text(-0.2 * np.pi / 2, y+pad, str(y), ha="center", size=12)

#Save figure
while True:
    filename = input("Please choose a filename, include the output format as this: radarplot.svg \nValid output formats are: .png, .tiff, .pdf, .jpeg, .svg \nFilename: ")
    filename = filename.strip()
    file_format = filename.split(sep=".")[-1].lower()

    valid_extensions = ['svg', 'png', 'pdf', 'jpeg', 'tiff']

    if file_format not in valid_extensions:
        print(f"{file_format} is not a valid format!")

    else:
        # Save the figure with the specified format
        fig.savefig(filename, format=file_format)

        # Break out of the loop since a valid filename was provided
        break



