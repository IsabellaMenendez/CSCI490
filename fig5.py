#import plotly
import plotly.express as px

#create dataframe
import pandas as pd
df = pd.read_csv("death.csv")

#use only data labeled Illinois in State column
df.loc[df['State'] == 'Illinois']

#create pie chart
fig = px.pie(df, values='Deaths', names='Cause Name', title = "Leading Causes of Death in Illinois for 2017",
	color_discrete_sequence=px.colors.sequential.Blugrn) #specify colors

#add labels
fig.update_traces(textposition='inside', textinfo='percent+label') 

#display graph
fig.show()

