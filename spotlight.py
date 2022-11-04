import plotly.express as px
  
import pandas as pd
df = pd.read_csv("pop.csv")

fig = px.bar(df, x=['2018', '2019'], y='Population - Total',
labels=dict(x="Year"))
fig.show()import plotly.express as px
  
import pandas as pd
df = pd.read_csv("pop.csv")

fig = px.bar(df, x=['2018', '2019'], y='Population - Total',
labels=dict(x="Year"))
fig.show()import plotly.express as px

import pandas as pd
df = pd.read_csv("pop.csv")

fig1 = px.bar(df, x=['2018', '2019'], y='Population - Total',
labels=dict(x="Year"))
fig1.show()

fig2 = px.bar(df, x=['2018', '2019'], y=['Population - Female', 'Population - Male'],
barmode = 'group',
labels=dict(x="Year"))
fig2.show()
