#import plotly
import plotly.express as px
 
#create dataframe 
import pandas as pd
df = pd.read_csv("death.csv")

#use only data labeled Illinois in State column
df.loc[df['State'] == 'Illinois']

#create pie chart
fig = px.pie(df, values='Deaths', names='Cause Name', title = "Leading Causes of Death in Illinois for 2017")

#display graph
fig.show()
