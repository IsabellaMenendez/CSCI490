#import plotly
import plotly.express as px

#create a data frame from file  
import pandas as pd
df = pd.read_csv("pop.csv")

#set to bar graph
fig = px.bar(df, x=['2018', '2019'], y='Population - Total',
	labels=dict(x="Year"), title = "Population of Illinois 2018-2019")

#display
fig.show()
