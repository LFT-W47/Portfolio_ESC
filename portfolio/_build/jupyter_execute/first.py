#!/usr/bin/env python
# coding: utf-8

# # Question 1
# 
# 
# ## How do these spheres interact?
# 
# 
# ### What is the (fraction of) mass of each sphere, in which the main interactions in contemporaneous Earth system dynamics takes place?

# In[1]:


hydrosphere_mass = 1.386 * 10**21
atmosphere_mass = 5.14 * 10**18
biosphere_mass = 2 * 10**15
lithosphere_mass = 2.7 * 10**22

# fraction
earth_mass = hydrosphere_mass + atmosphere_mass + biosphere_mass + lithosphere_mass
fraction_hydrosphere = hydrosphere_mass / earth_mass
fraction_atmosphere = atmosphere_mass / earth_mass
fraction_biosphere = biosphere_mass / earth_mass
fraction_lithosphere = lithosphere_mass / earth_mass

# Print results
print("Mass of Hydrosphere: {:.2e} kilograms".format(hydrosphere_mass))
print("Mass of Atmosphere: {:.2e} kilograms".format(atmosphere_mass))
print("Mass of Biosphere: {:.2e} kilograms".format(biosphere_mass))
print("Mass of Lithosphere: {:.2e} kilograms".format(lithosphere_mass))
print("\nHydrosphere fraction: {:.7%}".format(fraction_hydrosphere))
print("Atmosphere fraction: {:.7%}".format(fraction_atmosphere))
print("Biosphere fraction: {:.7%}".format(fraction_biosphere))
print("Lithosphere fraction: {:.7%}".format(fraction_lithosphere))


# ### What is the (fraction of) volume of each sphere, in which the main interactions in contemporaneous Earth system dynamics takes place?

# In[2]:


# Volumes
hydrosphere_volume = 1.332 * 10**9
atmosphere_volume = 52 * 10**9
lithosphere_volume = 25.3 * 10**9

# fraction
earth_volume = hydrosphere_volume + atmosphere_volume + lithosphere_volume
fraction_hydrosphere = hydrosphere_volume / earth_volume
fraction_atmosphere = atmosphere_volume / earth_volume
fraction_lithosphere = lithosphere_volume / earth_volume

print("Volume of Hydrosphere: {:.2e} cubic kilometers".format(hydrosphere_volume))
print("Volume of Atmosphere (100 km boundary): {:.2e} cubic kilometers".format(atmosphere_volume))
print("Volume of Lithosphere (upper 50 km): {:.2e} cubic kilometers".format(lithosphere_volume))
print("Volume of Biosphere is situated inside the other spheres")
print("\nFraction of Earth's total volume occupied by Hydrosphere: {:.2%}".format(fraction_hydrosphere))
print("Fraction of Earth's total volume occupied by Atmosphere: {:.2%}".format(fraction_atmosphere))
print("Fraction of Earth's total volume occupied by Lithosphere (upper 50 km): {:.2%}".format(fraction_lithosphere))

