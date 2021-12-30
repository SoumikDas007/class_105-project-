import pandas as pd
import plotly.express as px

dataFrame=pd.read_csv("corona_data.csv")
scatter=px.scatter(dataFrame,x="date",y="cases",color="country",size_max=100)
scatter.show()
