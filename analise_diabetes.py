import pandas as pd
df = pd.read_csv('diabetes.csv')

print(df.head())

import pandas_profiling as pp
pp.ProfileReport(df)
# Visualization Importsimport matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np