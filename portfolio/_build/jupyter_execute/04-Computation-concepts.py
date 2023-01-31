#!/usr/bin/env python
# coding: utf-8

# # Computation concepts
# 
# Goal of this exercise will be to provide concepts for computation on global analyses on gridded data. On the one hand weighted means will be explained, on the other how we can calculate an anomaly.
# 
# For further information, see also the Xarray documentation [here](https://tutorial.xarray.dev/overview/xarray-in-45-min.html#concepts-for-computation).

# ## Why do we need to weight grid cells?
# 
# The data in the Earth System Data Cube can be visualized in 2 dimensions when we want to display a variable at a specific moment in time. Each grid cell has the same distance from the adjacent one. But on the sphere as the Earth, these grid cells do not have the same size along the latitude. How can we take this size into account when we want to calculate the global mean of a variable?

# In[1]:


# import modules
import numpy as np
import xarray as xr
import fsspec
import matplotlib.pyplot as plt


# In[2]:


ds = xr.open_zarr(fsspec.get_mapper('/work/users/gy963viny/public/EarthSystemDataCube/v2.1.1/esdc-8d-0.25deg-184x90x90-2.1.1.zarr/'), consolidated=True)


# In[3]:


ds


# In[4]:


ds.air_temperature_2m.isel(time=200).plot()


# We can weight the grid cells by the area of the grid cell. For further calculations, e.g. the global mean of variable, we can then apply the weighted mean, which is defined as:
# 
# $
# \overline{X} = \frac{\sum{w_i \cdot X_i}}{\sum{w_i}}, $
# 
# where $X_i$ are the grid cells and $w_i$ the weights given by the size of each grid cell. 

# ## How do we to calculate the size of a grid cell?
# Sketch of a sphere with grid cells
# ![globe](globe.png)
# 
# 
# $\varphi$ denotes the latitude, and $\delta \varphi$ is the spacing of the point in latitude (e.g., 2.5$^\circ$)
# 
# $\lambda$ denotes longitude, and $\delta \varphi$ is the spacing of the point in longitude (e.g., 2.5$^\circ$) which varies with latitude. They are given in degree and need to be transfered to radians:
# 
# 
# - $\delta lat$ = R $\cdot$ $\delta \varphi$, and 
# - $\delta lon$ = R $\cdot$ $\delta \lambda$ $\cdot$ cos($\varphi$)
# 
# such that the surface element is $\delta A$ = R$^2$ $\cdot$ $\delta \varphi \cdot \delta \lambda$ $\cdot$  cos($\varphi$),
# where $\varphi$ and $\lambda$ are in radians
# 
# 

# For the calculation, we can use the Numpy function `np.deg2rad()` to convert degrees to radians. 

# In[5]:


# Earth's average radius in meter
R = 6.371e6


# In[6]:


# Calculate the arc length between points
dphi = np.deg2rad(2.5)
dlambda = np.deg2rad(2.5)

# Generate two DataArrays with the dimensions as latitude and longitude from the dataset 
dlat = R * dphi * xr.ones_like(ds.air_temperature_2m.lon) #we want to know the length at each longitude
dlon = R * dlambda * np.cos(np.deg2rad(ds.air_temperature_2m.lat)) #we want to know the longitudinal length at each latitude


# In[7]:


dlat


# In[8]:


dlat.plot()


# In[9]:


dlon


# In[10]:


dlon.plot()


# In[11]:


ds.air_temperature_2m.lat.data


# ### Broadcasting
# 
# Numpy and Xarray provide array broadcasting, which is an operation on arrays of unequal shapes. In this case it calculates the outer product of the two DataArrays dlon and dlat.

# In[12]:


cell_area = dlon * dlat


# In[13]:


cell_area.plot()


# **TODO**: Check if the sum is the same as the Earth surface area with summing up the cell areas with `.data.sum()`

# In[14]:


cell_area.data.sum()


# 510.100.000 km² is the actual Earth Surface Area. This would mean that `cell_area.data.sum()` is in dm².
