"""
You are given a data set called biopics.csv containing information on
biographical movies. your task is to perform some data manipulations on the biopics data

Data overview

The original biopics data are made available by the analytics website
FiveThirtyEight. You will working with a preprocessed version, available for you
at biopics.csv. It contains the following columns:
    - title - the movie's title
    - country - country of production
    - year_release - the year the movie was released
    - box_office - movie's earning at the box office in US$
    - type_of_subject - the occupation of the movie's subject or their reason for recognition
    - lead_actor_actress - the name of the actor or actress who played the subject

Instructions

Write a function named process_data() that takes no arguments. The function should load the biopics data (this has been implemented for you),
perform data manipulations described below and return a pandas data frame with manipulated data.

Clean up the biopics data:
    - Filter out duplicated rows
    - Rename the variable called box_office to earnings
    - Filter out rows for which earnings are missing(i.e they are NaN)
    - Keep only movies released in the year 1990 or later
    - Convert the type of type_of_subject and country to Categorical
    - Create a new variable called lead_actor_actress_known that is False if lead_actor_actress is NaN and True otherwise
    - Update earnings such they they are expressed in millions of dollars, instead of dollars
    - Reorder the columns in the data frame such that they are in the following order
      title, year_release, earnings, country, type_of_subjects, lead_actor_actress, lead_actor_actress_known
    - Sort the rows in descending order by earnings

On top of the Python Standard Library, you can make use of any function from the pandas packages
"""

import pandas as pd
import os

df = pd.read_csv('biopics1.csv')

#Filter out duplicated rows
df = df.drop_duplicates()

#Rename the variable called box_office to earnings
df=df.rename(columns={"box_office":"earnings"})

#Filter out rows for which earnings are missing(i.e they are NaN)
df = df[df['earnings'].notnull()]

#Keep only movies released in the year 1990 or later
df = df[df['year_release'] >= 1990]

#Convert the type of type_of_subject and country to Categorical
df=df.astype({'type_of_subject':'category','country':'category'})
df.dtypes

#Create a new variable called lead_actor_actress_known that is False if lead_actor_actress is NaN and True otherwise
df['lead_actor_actress_known'] = (df.lead_actor_actress.notnull())

#Update earnings such they they are expressed in millions of dollars, instead of dollars
df['earnings']= (df['earnings']/1000000)

#Reorder the columns in the data frame such that they are in the following order
#  title, year_release, earnings, country, type_of_subject, lead_actor_actress, lead_actor_actress_known
df = df[['title','year_release','earnings','country','type_of_subject','lead_actor_actress','lead_actor_actress_known']]

#Sort the rows in descending order by earnings
df = df.sort_values(by='earnings' , ascending = False)
