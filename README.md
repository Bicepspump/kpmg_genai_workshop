# JupyterLite and YData Profiling

This GitHub repository hosts the code required to serve a static webpage with a Python Kernel running in the browser, used for running lightweight analytics in fresh environments without any prior installation requirements (no Python install required).
It has a modified version of YData Profiling, a data profiling tool which has been updated to work with JupyterLite.
Finally, it holds sample notebooks that include code to initialise the environment to run YData Profiling on a DataSet.

## Setup and Usage Guide

The static website is deployed via GitHub pages to https://bicepspump.github.io/jupyterlite_demo and can be accessed by anyone (including clients which is the important part). Opening the URL presents you with a JupyterLab interface with the template Jupyter Notebooks available in the left pane. You can analyse files up to 50MB in this interface, simply dragging and dropping them in the left pane to upload them to the browser memory (this is local browser memory, not a cloud server). You then just need to modify the code slightly ("Changing the pd.read_csv("file_name_here")). Select the top cell and then press Shift+Enter to run the code and move to the next cell. Alternatively, you can press the "Run Cell" button (sidewise triangle at the top) to run each cell. Please find below a reference image with descriptions attached.

1. URL to access the Notebook environment
2. Left pane with Jupyter Notebooks (example_load_and_report)
3. Notebook Cell, you run the code in the cell by selecting it and pressing Shift+Enter
4. Alternatively, select the cell and press the "Run" button.

![alt text](https://github.com/Bicepspump/jupyterlite_demo/blob/main/jupyterlite_tutorial_image1.png)


