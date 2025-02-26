# Load in the 3 xlsx files with Pandas, and run the functions in Visualization.py

from Visualization import *
import pandas as pd

# load in all the files with the data I am using. This takes a long time.
# file2022DF = pd.read_excel("D:\Coding\Equibase\FirstAssignment\data\\2022.xlsx", header=0)
# file2023DF = pd.read_excel("D:\Coding\Equibase\FirstAssignment\data\\2023.xlsx", header=0)
file2024DF = pd.read_excel("D:\Coding\Equibase\FirstAssignment\data\\2024.xlsx", header=0)

# files = [file2022DF, file2023DF, file2024DF]

# AvgMorningLineOdds(file2024DF)
# AvgSpeedAndRating(files)
PostTimeOdds_RaceType(file2024DF)