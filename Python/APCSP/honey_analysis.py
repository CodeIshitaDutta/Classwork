"""This program will analyze the honey production in the US to 
display the effects of Colony Collapse Disorder. 
It will get the values of the data from each county in the state
over time, get the value for the entire state, and then 
graph the value over time and show change in production.
this can then be used to analyse how much colony collapse disorder
has effected our crops and how serious the problem is."""

#these are the import statements for this program
import matplotlib.pyplot as plt
import pandas as pd
import math

#this reads the program
df = pd.read_csv("honey.csv", header=0)

#this will clean the data
#first get rid of the commas and quotation marks
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

#and now to drop the NAN values
df['Value'] = df['Value'].replace(-99, math.nan)
df.dropna(subset=['Value'], inplace=True)

#grouping the data

#sort the states
unique_states = df['State'].unique()
all_honey = []
all_states = []

#this sorts the data by state and year
for state in unique_states:
  honey_data = df[df['State'] == state].groupby('Year')['Value']
  honey_sums = honey_data.sum()
  print (state, honey_data.sum())
  all_honey.append(honey_data.sum())
  all_states.append(state)
  
#to get to the graphing of the data
#this gets the year-state-value groups for each value
for i in range(len(unique_states)):
  honey = all_honey[i]
  state = all_states[i]
  years = all_honey[i].keys()
  plt.plot(years, honey, label=state)
  plt.ylabel('Amount of Honey in Pounds')
  plt.xlabel('Year')
  plt.title('Honey Production Over Time By State')
  plt.legend()
  plt.show()


#this actually plots the data with the labels
plt.ylabel('Amount of Honey in Pounds')
plt.xlabel('Year')
plt.title('Honey Production Over Time By State')
plt.legend()
plt.show()
