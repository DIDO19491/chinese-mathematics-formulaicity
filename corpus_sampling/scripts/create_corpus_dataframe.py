#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The purpose of the script is to create a preprocessed corpus as dataframe.
# Input: json-objects created based on the script "kanripo_data_downloads.py"
# Output: preprocessed/cleaned dataframe in csv-format. 

import re
import string
import json
import pandas as pd
import glob


# juans excluded from analysis
no_cont = ["提要","0","跋","原序","目録","序","後序",] 
# list of categories to be considered for the corpus
liste_cat = ["kongzi","bingjia","fajia","nongjia","yijia","tianwensuanfa","shushu","yishu","pulu","zajia","leishu",
             "xiaoshuo", "tianwen"]                        
                     

def content(c, data):
    return (c, data.get("id"),data.get("id_name"),data.get("juan"),data.get("title"),data.get("text"))

def no_content(i):
    for con in no_cont:
        if con in i.get("juan"):
            return "no"
    return "yes"
    

container = []
for cat in liste_cat:
    for file in glob.glob(f"data_formulib/data_KR3_zibu/{cat}/*.json"):  # path to output from script "kanripo_data_downloads.py"
        with open(file, mode="rb") as js:
            jsi = json.load(js)
            if len(jsi) >= 1:
                if len(jsi) == 1:
                    container.append(content(cat,jsi[0]))
                else:
                    for i in jsi:
                        if no_content(i) == "yes":
                            container.append(content(cat,i))
                                
# create dataframe
df = pd.DataFrame(container)
df = df.rename(columns={0:"category",1:"id",2:"id_name",3:"juan",4:"title",5:"text"})

## text preprocessing steps
# delete chinese punctuation marks for line break, which especially occures in comments
df["text"] = df["text"].str.replace(r'[)）/［(（］]+', '')

# replace "□" with standardized character '讠' , also if there is "丨" around
df["text"] = df["text"].apply(lambda x: re.sub("([□丨]*丨□[□丨]*)|([□丨]*□丨[丨□]*)", "讠", x))
# replace many "丨"  when there is no "□" around
df["text"] = df["text"].apply(lambda x: re.sub("丨+", "丨", x))
# replace many "□" if there is no "丨"  around
df["text"] = df["text"].apply(lambda x: re.sub("□+", "讠", x))

# count number of character per 'juan'
df["length"] = df["text"].apply(lambda x: len(x))
# for easier counting
df["sample"] = 1
        
# represent chinese numbers in text with a standardized character '鿡' 
def no_numbers(te):
    return re.sub('[一二三四五六七八九十百千萬亿万零億○]+','鿡',te)

# count number of character based on standardized chinese numbers
df["length_鿡"] = df.apply(lambda x: len(no_numbers(x.text)),axis=1)
df["text_鿡"] = df.apply(lambda x: no_numbers(x.text), axis=1)

# delete not representational juan
drop_list = [df[(df.id == "KR3g0012") & (df.juan == "卷四")].index[0], df[(df.id == "KR3g0012") & (df.juan == "卷五")].index[0]]
df_neu = df.drop(drop_list,axis=0) # drop rows with axis = 0

# some downloaded juans have no text (empty textfiles in Kanripo repository)
df_neu1 = df_neu[df_neu["length"] > 0]
df_neu1 = df_neu1.reset_index(drop=True)

# return dataframe
def main():
    # check if no nan in any columns
    print("Check for 'nan' in columns: ")
    print(df_neu1.isna().sum())
    return df_neu1

