import pandas as pd
import plotly.express as px
import statistics
import plotly.graph_objects as go
import csv
import numpy as np
import plotly.figure_factory as pf
import seaborn as sns

#----------------------------------------------------------------------------------


#Plotting the graph
df = pd.read_csv("data.csv")

fig = px.scatter(df, y="quant_saved", color="rem_any")
#fig.show()

#----------------------------------------------------------------------------------


with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  savings_data = list(reader)

savings_data.pop(0)

#Finding total number of people and number of people who were reminded
total_entries = len(savings_data)
total_people_given_reminder = 0

for data in savings_data:
  if int(data[3]) == 1:
    total_people_given_reminder += 1

import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[total_people_given_reminder, (total_entries - total_people_given_reminder)]))

#fig.show()
#----------------------------------------------------------------------------------

#Mean, median and mode of savings

all_savings = []
for data in savings_data:
  all_savings.append(float(data[0]))

#print(f"Mean of savings - {statistics.mean(all_savings)}")
#print(f"Median of savings - {statistics.median(all_savings)}")
#print(f"Mode of savings - {statistics.mode(all_savings)}")



#----------------------------------------------------------------------------------

reminded_savings = []
not_reminded_savings = []
for data in savings_data:
  if int(data[3]) == 1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))

# print("\n\n")
# print("Results for people who were reminded to save")
# print(f"Mean of savings - {statistics.mean(reminded_savings)}")
# print(f"Median of savings - {statistics.median(reminded_savings)}")
# print(f"Mode of savings - {statistics.mode(reminded_savings)}")

# print("\n\n")
# print("Results for people who were not reminded to save")
# print(f"Mean of savings - {statistics.mean(not_reminded_savings)}")
# print(f"Median of savings - {statistics.median(not_reminded_savings)}")
# print(f"Mode of savings - {statistics.mode(not_reminded_savings)}")
# print("\n\n")

#-----------------------------------------Standard Deviation ---------------------------------------------
# print(f"Standard deviation of all the data -> {statistics.stdev(all_savings)}")
# print(f"Standard deviation of people who were reminded -> {statistics.stdev(reminded_savings)}")
# print(f"Standard deviation of people who were not reminded -> {statistics.stdev(not_reminded_savings)}")


#----------------- Finding a correlation ----------------------------------

age = []
savings = []

for data in savings_data:
    if float(data[5]) != 0:
        age.append(float(data[5]))
        savings.append(float(data[0]))

Coorelation = np.corrcoef(age,savings)

# print("\n\n")
# print("Coorelation is --> " ,Coorelation[0,1] )

#------------------------- Displaying the graph --------------------------

# fig = pf.create_distplot(  [ df["quant_saved"].tolist() ] , ["Saving Data"] , show_hist=False)
# fig.show()


# sns.boxplot(data=df , x = df["quant_saved"] )


#------------------------- Removing the Outliers  --------------------------

q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)

iqr = q3-q1

# print("\n\n")
# print("q1 --> " , q1)
# print("q3 --> " , q3)

# print("IQR --> " , iqr)

lowerWhisker = q1 - (1.5*iqr)
upperWhisker = q3 + (1.5*iqr)

# print("\n\n")
# print("lowerWhisker --> " , lowerWhisker)
# print("upperWhisker --> " , upperWhisker)

newData = df[ df["quant_saved"] < upperWhisker ]

newSavings = newData["quant_saved"].tolist()

# print("\n\n")

# print(f"Mean of savings - {statistics.mean(newSavings)}")
# print(f"Median of savings - {statistics.median(newSavings)}")
# print(f"Mode of savings - {statistics.mode(newSavings)}")

# print(f"Stdev of savings - {statistics.stdev(newSavings)}")

# fig = pf.create_distplot(  [ newData["quant_saved"].tolist() ] , ["Saving Data"] , show_hist=False)
# fig.show()

#---------------------------------------------------------------------------------------------------------------

import random 

sampleMean = []

for i in range(1000):
  temp_list = []

  for a in range(100):
    temp_list.append(random.choice(newSavings))

  sampleMean.append(statistics.mean(temp_list))

mean = statistics.mean(sampleMean)

# fig = pf.create_distplot( [sampleMean] , ["Savings (Samples)"] , show_hist=False)
# fig.show()

print(f"Stdev of savings - {statistics.stdev(sampleMean)}")
print(f"Mean of savings - {statistics.mean(sampleMean)}")


temp_df = newData[newData.age != 0]

age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()

correlation = np.corrcoef(age, savings)
print(f"Correlation between the age of the person and their savings is - {correlation[0,1]}")