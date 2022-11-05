#import plotly
import plotly.express as px

#create dataframe file
import pandas as pd
df = pd.read_csv("pop.csv")

#split the data into category
fig = px.bar(df, x=['2018', '2019'], y=['Population - Female', 'Population - Male'])

fig.update_layout(
                  title="Population of Chicago 2018-2019",
                  xaxis_title="Year",
                  yaxis_title="Population",
                  legend_title="Key")
#display graph
fig.show()
