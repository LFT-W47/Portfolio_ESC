#!/usr/bin/env python
# coding: utf-8

# # Introduction to JupyterLab, Python and Conda 
# 
# In this Notebook, we give a brief intoduction to JupyterLab with its different features, to Python and Conda. It is far from complete, but should allow you to easily use this infrastructure to compute and visualize simple processes of the Earth System. You can test your ideas and methods and try different datasets simply in the web interface. You will later on learn how to access a Earth System Data Cube with variables from the biosphere and atmosphere, e.g. temperature or water fluxes.
# 
# You can access this notebook directly in the cluster and copy it to your working directory:
# 
# `cp /work/users/mz197zjio/Earth_System_Components/notebooks/01-Intro.ipynb .`
# 
# The notebook is also uploaded to the Moodle course site (in both, .ipynb and HTML format).
# 
# If you want to download it to your computer without accessing the JupyterLab, please do by `scp` (secure copy). It follows the logic: scp \[souce file\] \[destination file\]:
# 
# `scp mz197zjio@login01.sc.uni-leipzig.de://work/users/mz197zjio/Earth_System_Components/notebooks/01-Intro.ipynb .`, where the the first `mz197zjio` needs to be replaced by your own user-name. 
# **Caution**: Make sure that you do not overwrite your own version of the Intro file when you copy it into your working directory.
# 

# ## JupyterLab
# 
# ### What is Jupyterlab?
# Find more information on JupyterLab on the documentation website: https://jupyterlab.readthedocs.io/en/stable/.
# 
# Short: A combination of interactive coding, text, equations and other outputs. It provides Jupyter Notebooks and text editors, terminals, data file viewer and interactive plottings, etc.
# 
# The Interface: menu bar, left sidebar, and main work area. 
# 
# **Menu bar**: File, Edit, View, Run, Kernel, Tabs, Settings, Help
# 
# **Left Sidebar**: Different tabs where you can browse your files, see which tabs are open, which kernels and terminals are running, table of content, Softwares (Modules that are already installed and can be used at the cluster), extention manager
# 
# **Main work area**: Documents like notebooks, images, consoles and datasets are organised in panels or tabs that can be subdivided or resized depending on your workflow
# 
# TODO: Add an image to your directory, open it in JupyterLab, zoom in/out with ```-``` and ```=```, check other shortcuts
# 
# ### Jupyter Notebooks (.ipynb)
# 
# In a Jupyter Notebook, one can write and execute code, visualise data, and also share this code with others. The special feature of Jupyter Notebook is that the code and the description of the code are written in independent cells, so that individual code blocks can be executed individually. 
# 
# To open a new Notebook, click the ```+``` button in the file browser and select a kernel in the new Launcher tab. Rename it by right-clicking on its name in the file browser and selecting "Rename" from the context menu.
# 
# You can add narrative text in Markdown, equations in LaTeX, images and also interactive visualizations. Thereby you can comment your calculations and figures.
# 

# #### Markdown
# More information on Markdown can be found here: https://www.markdownguide.org/cheat-sheet/.
# 
# You can insert a heading when you start a line with `#`. There are up to 6 levels of heading. 
# 
# *you can write italics*
# 
# **or insert a bold text**
# 
# - give unordered
# - lists
# 
# 1. or show them in an ordered style
# 4. no matter if you count correctly or
# 2. like this one
# 1. not
# 
# > blockquote allows this format
# 
# ---
# 
# Type some `inline code` and you can easily read code it in a rich text.
# 
# Or insert a block of code
# ```
# using three backticks
# and end this block with three more backticks
# ```
# 
# #### LaTeX
# We can easily insert equations with `$`, e.g. Stefan-Boltzmann law: $ P = \sigma \cdot A \cdot T^4 $
# 
# Insert any url: www.rsc4earth.de 
# Or we can customise the link with [Remote Sensing Centre](www.rsc4earth.de)
# 
# 
# TODO: Add another cell, write a headline (starting with ```#```) and a small text, insert an equation with LaTeX, and add an image.
# 
# 

# # This is my first headline in Jupyter Notebook
# $\sqrt[n]{x}$
# 
# ![Hehe](https://www.nasa.gov/sites/default/files/styles/full_width/public/thumbnails/image/1-bluemarble_west.jpg?itok=hRooa_1o)

# ## Python
# You can find detailed tutorials on the official python website: https://docs.python.org/3.9/tutorial/
# 
# Different ways to use Python:
# * Running a Python file in a terminal, e.g. ```python script.py```
# * In an interactive console (IDE (Integrated Development Environment) or iPython shell) 
# * With an interactive notebook, e.g. Jupyter
# 
# In this course, we will use Jupyter Notebooks.

# ### Basic Variables: Numbers and Strings

# In[1]:


# lines starting with a "#" symbol are comments
a = 'hello'
b = 25


# In[2]:


a


# In[3]:


# print(a, b)
print(type(a))
print(type(b))


# You can apply a method on an object by `variable.method`

# In[4]:


# e.g. capitalize a string
a.capitalize()


# ### Basic arithmetics and logic

# In[5]:


x = 592
y = 42


# In[6]:


x-y # + / **


# In[7]:


# AND / OR / not logical statements
True or (not False)


# In[8]:


True and (not False)


# ### Lists
# Lists are used to store multiple items in a single variable. Create a list with different spheres of the Earth system:

# In[9]:


my_list = ['Geosphere', 'Hydrosphere', 'Biosphere']

my_list.sort()
print(my_list)

my_list.append('Atmosphere')
# call an element with 

print(my_list)


# In[10]:


my_list.sort()
print(my_list)

# Python starts counting with 0
print(my_list[0])


# There are more data types like list, e.g. dictionaries or sets, which are very powerful in their function. It is worth checking on all these data types e.g. [here](https://www.w3schools.com/python/python_datatypes.asp).

# ### For Loops
# 

# In[11]:


for i in my_list:
    print(i)


# In[12]:


import numpy as np
np.arange(10)


# In[13]:


for i in np.arange(10):
    print(i)


# ### Functions
# When you face a repeating task, it is useful to write a function. A function takes inputs (named "arguements"), applies a function on it and returns (not always) something. Variables inside a function are local. That means, that you cannot call them outside of the function. To save the outcome, you'd use the `return` statement.
# 
# We want to define a function that translates degrees Celcius into Kelvin.

# In[14]:


def greeting(name):
    print('Hello, ' + name + '!')


# In[15]:


greeting('my_NAME')


# In[16]:


def cel_to_kel(c):
    k = c + 273.15
#    print(k)
    return k


# In[17]:


cel_to_kel(15)


# TODO: Write a function that translates degree Celcius into Fahrenheit.
# 
# Fahrenheit set the zero point of his scale to the lowest temperature he could generate by mixing ice, water and ammonia or sea salt to avoid negative values. The freezing point of this mixture is -17.8°C and thereby correspond to 0°F. Two other fixpoints were the freezing point of pure water and the body temperature. Fahrenheit and Celsius can be converted by these formulas:
# $c = \frac{f - 32}{1.8}$ or $f = c \times 1.8 + 32$

# In[18]:


def cel_to_far(cel):
    far = (cel * 1.8) + 32
    return far

cel_to_far(0)


# ### Packages (modules)
# 
# For many applications there are packages or so called modules that supports your work, they are basically code libraries. If you want to work with numerical functions, linear algebra routines, Fourier transforms etc. it is recommended to use `numpy`. Numpy stands for Numerical Python. And when you want to plot your data, you can use `matplotlib`. See also the documentations: https://numpy.org/ and https://matplotlib.org/.
# 
# You can check on all variables and functions in the module when you call `dir(module)`.
# 
# There are different options how to import packages/modules:

# In[19]:


import numpy


# Usually, you would **alias** numpy by np, to shorten your code:
# 
# `import [long_name] as [short]`

# In[20]:


import numpy as np
import matplotlib.pyplot as plt


# In[21]:


dir(np)


# #### NumPy

# In[22]:


# We mainly use arrays when we work with numpy, hte class is called numpy adarray (n-dimensional array)
a = np.array([2, 52, 352, 53, 5, 10])

print(type(a))


# In[23]:


# Try and interprete the different methods
print(a.dtype)
print(a.shape)
print(a.ndim)
print(type(a))


# In[24]:


# You can also create ranges with np.arange(start, end, step)
np.arange(0, 100, 2)


# In[25]:


# Or linearly spaced 
np.linspace(3, 6, 15)


# In[26]:


# Indexing

print(a[1])
#print(a[-1])


# #### Matplotlib
# Matplotlib is a the module to plot your data. Find examples of different plots here in the matplotlib gallery: https://matplotlib.org/stable/gallery/index.html

# In[27]:


x = np.arange(0, 10, 0.2)
y = np.sin(x)


# In[28]:


plt.plot(x,y)
plt.show()


# In[29]:


# Add a title and labeles
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title('My first graph!!! o.O')
plt.plot(x,y)


# In[30]:


# Add a title and labeles
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title('My first graph!!! o.O')
plt.plot(x,y)


# In[31]:


# Add the cosine to the plot
z = np.cos(x)

plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('My first graph')
plt.plot(x, y, label = 'sin(x)')
plt.plot(x, z, label = 'cos(x)')

plt.legend()


# To choose different markers and colors, you find an overview here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# In[32]:


# Add the cosine to the plot and choose different markers and colors
z = np.cos(x)

plt.xlabel('x')
plt.ylabel('f(x)')

plt.title('My first graph')
plt.plot(x, y, 'b--',label = 'sin(x)')
plt.plot(x, z, 'r-', label = 'cos(x)')

plt.legend()


# In[33]:


# generate a scatter plot
x = np.arange(0, 20, 1)
y = np.sin(np.arange(0, 10, 0.5))

plt.scatter(x, y)


# ## Conda
# Packages we are going to use are: matplotlib, xarray, pandas, geopandas or cartopy. Most of these libraries are constantly improved and developped. Not all of the versions of libraries are compatible with each other. Therefore it is useful to initiate conda to manage all libraries/packages which are used in a project. It helps to make your scripts reproducible for other people who do not have the same setting.
# 
# More information on how to use the package manager conda: https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html.
# 
# Link from SC: https://www.sc.uni-leipzig.de/user-doc/quickstart/jupyter/#access-to-jupyterhub
# 
# Open a terminal in jupyterlab or access the cluster from your local computer terminal by ```ssh user@login01.sc.uni-leipzig.de```, in case you have a windows computer, you may use e.g. mobaXterm.
# Make sure you are in your home folder with ```cd ~```.
# 
# 1. Load Anaconda, and initialize conda 
# 
# ```
# module load Anaconda3 
# conda init bash 
# ```
# 
# 2. Create a new conda environment with python (version 3.9), after -n follows the name of the environment, after that all the packages that you want to install, either install them in the moment the conda is created or afterwards
# 
# ```
# conda create -n esc python=3.9
# ```
# 
# 3. Activate the environment and install the following packages
# 
# ```
# conda activate esc
# conda install xarray matplotlib fsspec aiohttp requests zarr cartopy ipykernel
# ```
# 
# 4. Connect the kernel (after --name follows the name of your environment, --display-name gives the displayed name of your kernel)
# 
# ```
# python -m ipykernel install --user --name 'esc' --display-name "ESC python=3.9"
# ```
# 
# 5. Deactivate conda and log out, with the next login, the kernel should be visible in your Jupyter launcher
# 
# ```
# conda deactivate
# ```
# 

# If you log out and in, the kernel should be visible in your Jupyter launcher

# ## Outlook: Example with Xarray

# In[34]:


import xarray as xr
import fsspec
ds = xr.open_zarr(fsspec.get_mapper('http://data.rsc4earth.de/EarthSystemDataCube/v2.1.1/esdc-8d-0.25deg-1x720x1440-2.1.1.zarr/'), consolidated=True)


# In[36]:


ds


# In[37]:


ds.air_temperature_2m.isel(time=1000).plot(x="lon")

