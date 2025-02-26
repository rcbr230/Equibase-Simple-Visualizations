import pandas as pd
from collections import defaultdict
from fractions import Fraction
import matplotlib.pyplot as plt




"""
Assign 1
Create a visual that would show us the average morning line odds
for the race favorite (favorite indicator being Y) by track for 2024. 
Essentially, we are trying to see what odds tracks tend to give their favorites.

"""
def AvgMorningLineOdds(df:pd.DataFrame):
    # use a bar graph, x being each track, y being avg morning line odds for the favoirtes
    
    # only select favoirtes
    df = df.loc[df['favorite_indicator'] == "Y"]
    df = df.reset_index()

    # load all track vals 
    trackVals = defaultdict(float)
    for i in range(len(df)):
        trackVals[df['track_id'][i]] += float(Fraction(df['morning_line_odds'][i]))
    
    # find averages by counting # of appearances track id in DF
    for key, val in trackVals.items():
        numRecords = (df['track_id'] == key).sum()
        trackVals[key] = trackVals[key] / numRecords

    # Use matplotlib to graph out the data on a bar graph
    plt.bar(trackVals.keys(), trackVals.values())
    plt.xlabel('Tracks')
    plt.ylabel('Favorite Morining Line Odds')
    plt.title('Average Morning Line Odds by favorites per track 2024')
    plt.show()




"""
Assign 2
Create a visual with the legend being the two states (NY and KY)
that are present in all the datasets. We are interested in looking 
at any trends that are occurring over the years. Is the avg speed_figure 
or avg class_ratings for NY tracks or KY steady over the years? Or has there 
been any increases/decreases? Which state tends to have higher average speed figures?
"""
def AvgSpeedAndRating(df2022:pd.DataFrame, df2023:pd.DataFrame, df2024:pd.DataFrame):
    # use a line graph with 2 seperate lines for each state. 
    #  GRAPH 1: x is years, y is speed figure
    #  GRAPH 2: x is years, y is class ratings
    pass





"""
Assign 3
We are interested in also looking at posttimeodds for year 2024 
by race_type. Can you create a visual that would present the avg posttimeodds for 
each race type?
"""
def PostTimeOdds_RaceType(file):
    # bar graph. x is race type, y is posttimeodds
    pass
