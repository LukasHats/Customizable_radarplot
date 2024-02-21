# Customizable_radarplot

A python script that lets you create a radar plot with customizable options for labels and associated weighting from 0 to 10

## Introduction

This small script was initially created to visualize skills using a radar plot (also known as spider plot). In order to bexpand the application it was changed to take user-specific inputs for attributes and associated skill levels. The work was partially inspired by [The-Python-Graph-Gallery](https://github.com/holtzy/The-Python-Graph-Gallery).

## Usage

When python is installed simpy run python `radarplot_universal-py`. The script will ask the user to prompt attributes. In the current version it is recommended to not exceed more than 12 attributes as otherwise the barplots will overlap. Afterwards the user will be asked for a rating between 0 and 10 for each attribute.

### Possible modifications

The overlap of barplots resulting of exceeding 12 attributes can be solved by adjusting the `width` parameter (default setting is `width = 0.45`) when calling the barplot. Adjusting the rating is more tricky as it requires changing the y-axis and also a `while True` loop. Therefore, if adjustments are needed, please thoroughly check the code including `both while True` loops and all inputs regarding the y-axis.

### Output

For output the user can choose between the following formats: `.png`, `.pdf`, `.tiff`, `.svg` and `.jpeg`. The file is automatically stored with the associated name in the current working directory.
