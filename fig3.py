#import plotly
import plotly.express as px

#create dataframe
import pandas as pd
df = pd.read_csv("pop.csv")


fig = px.bar(df, x=['2018', '2019'], y=['Population - Female', 'Population - Male'],
             barmode = 'group') #split the data into two bars

fig.update_layout(
                  title="Population of Chicago 2018-2019",
                  xaxis_title="Year",
                  yaxis_title="Population"
                  legend_title="Key")

#display graph
fig.show()
