# -*- coding: utf-8 -*-
"""IPL_2022_Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IiFXGKSgpPymdqrdlncGd6vsfibUOHpK
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("/content/IPL.csv")

data

data.info()

data.describe()

data["date"]=pd.to_datetime

data.info()



"""Number of matches won by each team in IPL 2022"""

fig = px.bar(data, x = data["match_winner"],title="IPL 2022 winner Bar graph")
fig.show()

"""Number of matches won by chasing and Defending in IPL 2022


"""

data['won_by'] = data['won_by'].map({'Wickets':'Chasing', 'Runs':'Defending'})
won_by = data['won_by'].value_counts()
labels = won_by.index
counts = won_by.values
colors=['red','blue']
fig= go.Figure(data=[go.Pie(labels=labels,values=counts)])
fig.update_layout(title_text="Numbers of matches won by chasing and Defending")
fig.update_traces(hoverinfo='label+percent',textinfo='value',
                  marker=dict(colors=colors,line=dict(color="darkgreen",width=3)))
fig.show()

"""
**let’s see what most teams prefer (batting or fielding) after winning the toss**"""

from plotly.graph_objs import Marker
toss = data['toss_decision'].value_counts()
labels= toss.index
counts = toss.values
colors = ["purple",'lightblue']
fig = go.Figure(data=[go.Pie(labels=labels,values=counts)])
fig.update_layout(title_text="Pie chart of Toss Decision")
fig.update_traces(hoverinfo='label+percent',textinfo='value',
                  marker=dict(colors=colors,line=dict(color="black",width=3)))
fig.show()

"""**let’s see the top scorers of most IPL 2022 matches**"""

fig=px.bar(data,x=data['top_scorer'],title="Top scorer in IPL 2022")
fig.show()

"""**Currently, Jos Buttler has been a top scorer in 5 matches. Let’s analyze it deeply by including the runs scored by the top scorers**"""

fig = px.bar(data,x=data['top_scorer'],y=data['highscore'],title="Top Scores with his runs",color=data['highscore'])
fig.show()

"""**Lets have a look who is the best bowler in IPL 2022**"""

fig = px.bar(data,x=data['best_bowling'],title="Best bowler in IPL 2022")
fig.show()

"""Yuzvendra Chahal having the best bowling figures in four matches. So this is a great tournament for Yuzvendra Chahal this year too.

Now let’s have a look at whether most of the wickets fall while setting the target or while chasing the target text
"""

figure = go.Figure()
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["first_ings_wkts"],
    name='First Innings Wickets',
    marker_color='gold'
))
figure.add_trace(go.Bar(
    x=data["venue"],
    y=data["second_ings_wkts"],
    name='Second Innings Wickets',
    marker_color='lightgreen'
))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()

""" Wankhede Stadium in Mumbai and MCA Stadium in Pune, most wickets fall while chasing the target. And in the other two stadiums, most wickets fall while setting the target"""



"""Summary

# So this is how you can perform the task of IPL 2022 analysis using Python. IPL 2022 is going great for Gujrat as a new team this year. Jos Buttler and KL Rahul have been great with the bat, and Yuzvendra Chahal and Kuldeep Yadav have been great with the bowl. I hope you liked this article on IPL 2022 analysis using Python. Feel free to ask valuable questions in the comments section below.
"""

