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
    plt.clf()
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

    # Load all data into 1 DF

    # calc averages of speed figures
    kySpeedFigure = [0,0,0]
    kyRaces = [0,0,0]
    nySpeedFigure = [0,0,0]
    nyRaces = [0,0,0]


    for i in range(max(max(len(df2022), len(df2023)), len(df2024))):
        if i < len(df2022):
            if str(df2022['state'][i]).strip().upper() == 'KY':
                kySpeedFigure[0] += df2022['speed_figure'][i]
                kyRaces[0] += 1
            elif str(df2022['state'][i]).strip().upper() == 'NY':
                nySpeedFigure[0] += df2022['speed_figure'][i]
                nyRaces[0] += 1

        if i < len(df2023):
            if str(df2023['state'][i]).strip().upper() == 'KY':
                kySpeedFigure[1] += df2023['speed_figure'][i]
                kyRaces[1] += 1
            elif str(df2023['state'][i]).strip().upper() == 'NY':
                nySpeedFigure[1] += df2023['speed_figure'][i]
                nyRaces[1] += 1

        if i < len(df2024):
            if str(df2024['state'][i]).strip().upper() == 'KY':
                kySpeedFigure[2] += df2024['speed_figure'][i]
                kyRaces[2] += 1
            elif str(df2024['state'][i]).strip().upper() == 'NY':
                nySpeedFigure[2] += df2024['speed_figure'][i]
                nyRaces[2] += 1


    kySpeedFigure = [kySpeedFigure[0]/kyRaces[0], kySpeedFigure[1]/kyRaces[1], kySpeedFigure[2]/kyRaces[2]]
    nySpeedFigure = [nySpeedFigure[0]/nyRaces[0], nySpeedFigure[1]/nyRaces[1], nySpeedFigure[2]/nyRaces[2]]

    x = [2022, 2023, 2024]
    plt.clf()
    plt.plot(x, kySpeedFigure, label="Kentucky")
    plt.plot(x, nySpeedFigure, label="New York")
    plt.xticks([2022, 2023, 2024])
    plt.tight_layout()
    plt.xlabel('Year')
    plt.ylabel('Avg Speed Figure')
    plt.title('Average Speed figure by year')

    plt.legend()

    plt.show()






"""
Assign 3
We are interested in also looking at posttimeodds for year 2024 
by race_type. Can you create a visual that would present the avg posttimeodds for 
each race type?
"""
def PostTimeOdds_RaceType(df:pd.DataFrame):
    # bar graph. x is race type, y is posttimeodds
    # only select favoirtes

    # load all track vals 
    posttimeoddsVals = defaultdict(float)
    for i in range(len(df)):
        posttimeoddsVals[df['race_type'][i]] += float(df['Posttimeodds'][i])
    
    # find averages by counting # of appearances track id in DF
    for key, val in posttimeoddsVals.items():
        numRecords = (df['race_type'] == key).sum()
        posttimeoddsVals[key] = posttimeoddsVals[key] / numRecords

    # Use matplotlib to graph out the data on a bar graph
    plt.clf()
    plt.bar(posttimeoddsVals.keys(), posttimeoddsVals.values())
    plt.xlabel('Race Type')
    plt.ylabel('Post Time Odds')
    plt.title('Average Post Time Odds value by Race Type 2024')
    plt.show()
