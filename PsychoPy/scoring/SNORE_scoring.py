import os
import pandas as pd
from fuzzywuzzy import fuzz
import regex as re

def replace_return(string):
    clean_string = re.sub(r"\n", "", string)
    clean_string = re.sub(r"nan", "", clean_string)
    clean_string = re.sub(r" ", "", clean_string)
    return clean_string

def score_response(response):
    if response > 95:
        return 1
    else:
        return 0

#Here we need to get input

path = input("Enter the path to your SNORE file: ")

#read csv file
df = pd.read_csv(path)

# Create a copy of the DataFrame slice
df_short = df[["Word1","Word2", "Response.text"]].copy()

# Ensure all values are treated as strings, replacing NaNs with empty strings
df_short["Word2"] = df_short["Word2"].astype(str).fillna("")
df_short = df_short[df_short["Word2"] != "nan"]
df_short["Response.text"] = df_short["Response.text"].astype(str).fillna("")
df_short["Response.text"] = df_short["Response.text"].apply(replace_return)

#calculate distance based on Leveinstein algorithm
df_short["distance"] = df_short.apply(lambda row: fuzz.token_sort_ratio(row["Response.text"], row["Word2"]), axis=1)



#Calculate score of the participant
df_short["scoring"] = df_short["distance"].apply(score_response)
result = df_short["scoring"].sum()

print(f"Total score: {result}")

df_short[["Word1", "Word2", "Response.text", "distance"]].head(50)