import os
import random
from IPython.display import display
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

from rich.console import Console
from rich.table import Table

import plotly.express as px
import webbrowser as wb

console = Console()

installation = "a037a00000pwUFlAAM"
base_path = os.path.dirname(__file__)
read_filepath = base_path + "/dotw_pres_by_installation/" + installation + ".csv"
df = pd.read_csv(read_filepath).drop("Unnamed: 0", axis=1)
# console.print(df.head(25))

df_bins = pd.DataFrame({'BinNo' : df['BinNo']}).drop_duplicates()
# console.print(df_bins.head(25))

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_days = pd.DataFrame({'dotw' : day_order})

df_all = df_days.merge(df_bins, how='cross')
# console.print(df_bins.head(25))

df = df_all.merge(df, on=['dotw', 'BinNo'], how='left').fillna(0)
df['count'] = df['count'].astype(int)


df['dotw'] = pd.Categorical(df['dotw'], categories=day_order, ordered=True)
df = df.sort_values(['dotw','count'], ascending=[True, False])

rand = random.randint(0, len(df_bins['BinNo']) - 10)
df_test = df[df['BinNo'].isin(df_bins['BinNo'][rand:rand+10])].copy()

# console.print(df_test.to_string(index=False))
# console.print(df.head(25))

df_mon = df[df['dotw'] == 'Monday'].rename(columns={'count':'count_mon'}).drop('dotw', axis=1).copy()
df_tues = df[df['dotw'] == 'Tuesday'].rename(columns={'count':'count_tues'}).drop('dotw', axis=1).copy()
df_wed = df[df['dotw'] == 'Wednesday'].rename(columns={'count':'count_wed'}).drop('dotw', axis=1).copy()
df_thurs = df[df['dotw'] == 'Thursday'].rename(columns={'count':'count_thurs'}).drop('dotw', axis=1).copy()
df_fri = df[df['dotw'] == 'Friday'].rename(columns={'count':'count_fri'}).drop('dotw', axis=1).copy()
df_sat = df[df['dotw'] == 'Saturday'].rename(columns={'count':'count_sat'}).drop('dotw', axis=1).copy()
df_sun= df[df['dotw'] == 'Sunday'].rename(columns={'count':'count_sun'}).drop('dotw', axis=1).copy()

df_join = pd.merge(df_mon, df_tues, on='BinNo', how='outer') \
            .merge(df_wed, on='BinNo', how='outer') \
            .merge(df_thurs, on='BinNo', how='outer') \
            .merge(df_fri, on='BinNo', how='outer') \
            .merge(df_sat, on='BinNo', how='outer') \
            .merge(df_sun, on='BinNo', how='outer') \
            .sort_values(
                by=['count_mon', 'count_tues', 'count_wed', 'count_thurs', 'count_fri', 'count_sat', 'count_sun'],
                ascending=False)


# console.print(df_mon.head(20))
console.print(df_join.head(20))

# sns.lineplot(data=df_test, x='dotw', y='count', hue='BinNo', marker='s', palette=sns.color_palette("husl", 30))
# plt.legend(loc='best', ncol=6)
# # plt.tight_layout()
# plt.show()


# fig = px.line(df, x='dotw', y='count', color='BinNo', markers=True)
# fig.write_html(base_path + '/dotw_analysis.html', auto_open=True)