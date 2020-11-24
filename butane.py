# -*- coding: utf-8 -*-
"""Butane.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yucAhlnpn6pgsvqRNoObMb7THFWiaLRL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from google.colab import files 
  
  
uploaded = files.upload()

import io 
  
butane_df = pd.read_csv(io.BytesIO(uploaded['Butane - Sheet1.csv'])) 
print(butane_df)

sns.scatterplot(data=butane_df, x="Dihedral Angles", y="Potential energy")

sns.jointplot(x="Dihedral Angles", y="Potential energy", data=butane_df, kind="scatter")