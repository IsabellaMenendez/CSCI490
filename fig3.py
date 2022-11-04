#import plotly
import plotly.express as px

#create dataframe
import pandas as pd
df = pd.read_csv("pop.csv")


fig = px.bar(df, x=['2018', '2019'], y=['Population - Female', 'Population - Male'],
	barmode = 'group', #split the data into two bars
	labels=dict(x="Year"), title = "Population of Illinois 2018-2019")

#display graph
fig.show()

