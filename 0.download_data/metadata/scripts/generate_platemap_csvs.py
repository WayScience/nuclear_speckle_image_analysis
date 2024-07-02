#!/usr/bin/env python
# coding: utf-8

# # Generate platemap files from original position files
# 
# In this notebook, position files are used to generate plate map files to use for saving max projection images and annotating single-cell outputs downstream. 
# Columns are updated to avoid any downstream issues.

# ## Import libraries

# In[1]:


import pathlib
import pandas as pd


# ## Generate platemap files

# In[2]:


# Dir path for output of platemap CSV files
platemap_dir = pathlib.Path("./platemaps")
platemap_dir.mkdir(parents=True, exist_ok=True)

# Find all position txt files in the current directory starting with "slide"
position_files = pathlib.Path().resolve().glob('slide*')

# Instantiate a empty list to append updated plate maps to
position_dfs = []

# Iterate through each file to update "Point Name" and "Image" columns
for file in position_files:
    # Read the CSV file
    df = pd.read_csv(file, delimiter='\t', encoding='utf-16')
    
    # Remove '#' prefix from 'Point Name' column
    df['Point Name'] = df['Point Name'].str.lstrip('#')
    
    # Zero-index the 'Image' column
    df['Image'] = df['Image'] - 1
    
    # Save the processed DataFrame to the platemap directory
    output_file = pathlib.Path(f"{platemap_dir}/{file.stem}.csv")
    df.to_csv(output_file, index=False)
    
    # Append the processed DataFrame to the list
    position_dfs.append(df)

# Print the list of dataframes to verify that the process worked
for df in position_dfs:
    print(df.head())

