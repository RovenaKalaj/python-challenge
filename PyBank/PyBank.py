
  #import modules
import pandas as pd
from pathlib import Path

#set path for file
csvpath = Path("Resources/budget_data.csv")

# Read in the CSV as a DataFrame
df = pd.read_csv(csvpath)
print(df.head())

#1The total number of months included in the dataset.
Total_months=df["Profit/Losses"].count()
print(Total_months)


#2 The net total amount of Profit/Losses over the entire period.
NetPnl = df["Profit/Losses"].sum()
print(NetPnl)

#3 The average of the changes in Profit/Losses over the entire period.
df['pnl_changes']=df["Profit/Losses"]- df["Profit/Losses"].shift()
print(df)

Mean_PL= df["pnl_changes"].mean()
print(Mean_PL)


#4 Greatest Increase in Profits: Feb-2012 ($1926159) --) The max is in the row
df["pnl_changes"].max()


max_difference=df.loc[df["pnl_changes"] == df["pnl_changes"].max(),'Date']

print(max_difference)

        
#5 The greatest decrease in losses (date and amount) over the entire period.


min_difference= df["pnl_changes"].min()
print(min_difference)

min_row=df.loc[df["pnl_changes"] == df["pnl_changes"].min(),'Date']
print(min_row)

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${NetPnl}")
print(f"Average Change: ${Mean_PL}")
print(f"Greatest Increase in Profits: Feb-2012 $({max_difference})")
print(f"Greatest Decrease in Profits: Sep-2013 $({min_difference})")