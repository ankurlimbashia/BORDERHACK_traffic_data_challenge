# importing required packages
import numpy as np
import streamlit as st
import pandas as pd
from datetime import date,datetime,timedelta
import pickle
import plotly.graph_objs as go
import xgboost as xgb


st.title('Predicting the BEST time to Cross') # to create a title
st.sidebar.title('Enter the planned travel details') # to create a sidebar title

# creating selectbox to get the input
intersection = st.sidebar.selectbox(
    'Intersection',
     ["Dorchester Road and Huron Church Road",
     "Totten Street and Huron Church Road",
    "Malden Road and Huron Church Road"])

year = st.sidebar.selectbox(
    'Expected year of crossing',
     [2021,2020])

if year == 2020:
    month = st.sidebar.selectbox(
        'Expected month fo crossing',
        ['August','September','October','November','December'],
        index = 9)
else:
    month = st.sidebar.selectbox(
        'Expected month fo crossing',
        ['January','February','March','April','May','June','July','August','September','October','November','December'],
        index = 9)

if month in ['January','March','May','July','August','October','December']:
    day = st.sidebar.selectbox(
        'Expected day of crossing',
        range(1,32))
elif month in   ['April','June','September','November']:
    day = st.sidebar.selectbox(
        'Expected day of crossing',
        range(1,31))
else:
    day = st.sidebar.selectbox(
        'Expected day of crossing',
        range(1,29))

month_dic = {m:i for i,m in enumerate(['January','February','March','April','May','June','July','August','September','October','November','December'])}
month = month_dic[month] + 1
day_of_the_week = date(year,month,day).weekday()

hour = st.sidebar.selectbox(
    "Expected hour of crossing",
    range(0,24),
    index = 12)

# prediction using the saved model depending on the intersection selected by the user
count = []
time_given  =[]

for i in range(-6,7): # to get the 13 hours of timespan

    # making the test data ready
    test_data = datetime(year, month, day, hour) + timedelta(hours = i)

    time_given.append(test_data)
    y = test_data.year
    m = test_data.month 
    w = test_data.weekday()
    d = test_data.day
    h = test_data.hour

    model_1 = xgb.Booster()
    if intersection == "Dorchester Road and Huron Church Road":   
        model_1.load_model('model/dorchester_1.model')
        model_2 = pickle.load(open('model/dorchester_2.pkl','rb'))

    elif intersection == "Totten Street and Huron Church Road":
        model_1.load_model('model/totten_1.model')
        model_2 = pickle.load(open('model/totten_2.pkl','rb'))

    else:
        model_1.load_model('model/malden_1.model')
        model_2 = pickle.load(open('model/malden_2.pkl','rb'))

    test = np.array([y,m,w,d,h]).reshape(1,-1)
    count.append(int((model_1.predict(xgb.DMatrix(test)) + model_2.predict(test))/2))


title_1 = f'<p style="font-family:sans-serif;  font-size: 16px;">Total number of vehicles (both commercial and non-commercial vehicles) at "{intersection:}" on {time_given[6].date()} at {time_given[6].time()} is expected to be {count[6]}.</p>'
st.write(f'{title_1:}',unsafe_allow_html = True)

title = f'<p style="font-family:sans-serif;  font-size: 22px;">Best time to cross is <b><u> {time_given[np.argmin(count)].date()} at {time_given[np.argmin(count)].time()}</u></b>.</p>'
st.write(f'{title:}',unsafe_allow_html = True)

title_2 = f'<p style="font-family:sans-serif;  font-size: 16px;">Traffic will be minimum at "{intersection:}" on  {time_given[np.argmin(count)].date()} at {time_given[np.argmin(count)].time()}, which is expected to be {min(count)}.</p>'
st.write(f'{title_2:}',unsafe_allow_html = True)


# plotting the line chart of traffic predictions
trace = go.Line(x  = time_given,
                y = count,
                marker = dict(line = dict(width = 2.0,
                                    color = "yellow")),
                line = dict(width = 3),
                opacity = 1.0
                )
data = [trace]
layout = go.Layout(dict(title =f"Traffic Forcast at {intersection}",
                        plot_bgcolor  = "skyblue",
                        paper_bgcolor = "#475d87"))
fig  = go.Figure(data=data,layout=layout)
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Traffic Count")

st.plotly_chart(fig)

# making a note of what data we have used to create the model
st.markdown("We have trained the models using the municipal traffic data from [Windsor's OpenData API](https://opendata.citywindsor.ca/swagger/index.html) dated from 1st August 2020 to 24th September 2021.")