# BORDERHACK_traffic_data_challenge

### WEB API [best-time-to-cross](https://best-time-to-cross.herokuapp.com/)

## Inspiration
We are currently pursuing the course of Data Analytics in Business at St. Clair College and this project has given us the opportunity the work on some real world problem to utilize and test the skills that we have gained till now.

## What it does
We have build two models to predict the traffic count at all 3 intersection at the given time and date provided by user. In addition to this, it will also suggest the traffic count within the 12 hours of given time and will tell the user if at time close to the user provided time, traffic will be less or not. 

## How we built it
We have created two machine learning models in Google Colab for all 3 intersection given in the time plus we use VS code to build the web API then deployed it on the Heroku.

## Challenges we ran into
We tried to use only one machine learning algorithm for this problem for any particular intersection but we found that only one algorithm was giving us either the high or low traffic count compared to its true value. Therefore, to counter this we have used two algorithm then taken the average of both the predictions.

## Accomplishments that we're proud of
Here, we have tried to predict the traffic count for the upcoming month of October, November and December-2021 rather than just limiting ourselves in predicting the traffic count and comparing with the actual value.

## What we learned
We have learned few new libraries like "plotly" and "xgboost" in the python for machine learning and a new open source app framework for machine learning and data science named "Streamlit"

## What's next for Traffic Data Challenge
We can give user the idea about which intersection has the less traffic and divert the traffic there to have the same time loss at all the intersection due to heavy traffic.
