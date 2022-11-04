#import plotly
import plotly.express as px

#create dataframe file  
import pandas as pd
df = pd.read_csv("pop.csv")

#split the data into category 
fig = px.bar(df, x=['2018', '2019'], y=['Population - Female', 'Population - Male'],
	labels=dict(x="Year"), title = "Population of Illinois 2018-2019")

#display graph
fig.show()