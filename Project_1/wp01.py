
# Input:
# Basic.txt : Basic cupcakes, cost $5.
# Deluxe.txt : Deluxe cupcakes, cost $6.
# Total.txt : Total money made for the day.
# Date : The bottom-most row is always 'Today', the row above that is 'Yesterday', and so on.

# Output:
# Yearly Revenue Totals
# Monthly Revenue Totals
# Weekly Revenue Totals

import pandas as pd
import datetime as dt

# Open file and load data
basic = pd.read_csv("Basic.txt")
deluxe = pd.read_csv("Deluxe.txt")
total = pd.read_csv("Total.txt")

# Total basic and deluxe for the day
basic = basic * 5
deluxe = deluxe * 6

# Combine data in one dataframe
cupcake_dataframe = pd.concat([basic, deluxe, total], axis = 1)

# Date for each day
range_day = len(cupcake_dataframe)
start_day = dt.date.today() - dt.timedelta(days=range_day-1)
cupcake_dataframe["Date:"] = pd.date_range(start=start_day, periods=range_day)

# First column for Date
date_column = cupcake_dataframe.columns.tolist()
date_column = date_column[-1:] + date_column[:-1]
cupcake_dataframe = cupcake_dataframe[date_column]

# Yearly Revenue Totals
yearly = pd.DataFrame.groupby(by="2019").sum()
print("Yearly Revenue Totals: %i", yearly)

# Monthly Revenue Totals
#monthly = 
#print("Monthly Revenue Totals: %i", monthly)

# Weekly Revenue Totals
#weekly = 
#print("Weekly Revenue Totals: %i", weekly)

print(cupcake_dataframe)