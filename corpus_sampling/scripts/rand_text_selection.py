#!/usr/bin/env python
# coding: utf-8

# The purpose of the script --- to randomize text sample based on minimum text size (juan size) which is depending on the defined percentage of juans of the corpus to be used.
# Input: is created with the call of the script "create_corpus_dataframe.py" (take care that it has the correct path to the downloaded Kanripo files)
# Output: random juans based on their categories


import random
import pandas as pd
from collections import Counter

import argparse
import os

import create_corpus_dataframe


class corpus_selection:

	global seed 
	seed = random.randint(1, 1000)
	random.seed(seed)
	
	def __init__(self, df, juan_size):
		self.df = df
		self.juan_size = juan_size
		self.rand_select_df = pd.DataFrame()
		
	def copus_sized(self):
		"""creates subcorpus based on defined juan number"""
		
		# choose only juans witch are bigger than 'juan_size'
		select_df = self.df[self.df["length_鿡"] >= self.juan_size]
		select_df = select_df.reset_index(drop=True)
		
		# based on max_no of juan of category 'math' choose random juan from each category
		max_no_juan = len(select_df[select_df["category"]=="math"])
		categories = [tuple((x, y)) for x, y in select_df["category"].value_counts().items()]
		select_categories = [x[0] for x in categories if x[1] >= max_no_juan]
		
		# select random number based on max length and a given seed
		rand_no = []
		for i in select_categories:
			sel_no = random.sample(list(select_df[select_df["category"]==i].index),max_no_juan)
			sel_df = select_df[select_df.index.isin(sel_no)]
			self.rand_select_df = pd.concat([self.rand_select_df, sel_df], ignore_index=True)
			self.rand_select_df = self.rand_select_df.reset_index(drop=True)
		return self.rand_select_df


	def text_selection(self, juan):
		"""defines the window for random selection of the text based on upper and lower limits"""
		
		l_delta = len(juan) - self.juan_size
		
		if l_delta == 0:
			return juan
		else:
			# define window with upper and lower limits
			win_u = int((len(juan)/2) + l_delta/2)
			win_l = int((len(juan)/2) - l_delta/2)
			
			# random choice of base point for text selection
			zu = random.randint(win_l,win_u)
			
			# define text window with upper and lower limits based on zu
			zu_u = int(zu + (self.juan_size/2))
			zu_l = int(zu - (self.juan_size/2))
			# extract text chunck based on the text window defined
			return juan[zu_l:zu_u]
			
	def output(self):
		"""creates ouput folder based on category structure"""
		for i in range(0,len(self.rand_select_df)):
			text = self.text_selection(self.rand_select_df.loc[i,"text_鿡"])
			
			newpath = f'data_formulib_rand_noNum_{seed}/{self.rand_select_df.loc[i,"category"]}' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
				
			with open(f'data_formulib_rand_noNum_{seed}/{self.rand_select_df.loc[i,"category"]}/{self.rand_select_df.loc[i,"id"]}_{self.rand_select_df.loc[i,"title"]}_{self.rand_select_df.loc[i,"juan"]}_{i}.txt', mode="w", encoding="utf-8") as out:
				out.write(text)
        


def counting(d):
    lenght_dic = Counter()
    length = d.tolist()

    for i in length:
        lenght_dic[i] += 1

    xi = []
    yi = []
    for x, y in lenght_dic.items():
        xi.append(x)
        yi.append(y)
    return xi, yi


def min_text_size(d, size):
    """cumulated juan-length without numbers"""
    c_frame_鿡 = counting(d["length_鿡"])   
    frame_鿡 = pd.DataFrame(zip(c_frame_鿡[0],c_frame_鿡[1]))
    frame_鿡 = frame_鿡.rename(columns={0:"length_鿡", 1:"counts"})
    frame_鿡 = frame_鿡.sort_values("counts")
    frame_鿡 = frame_鿡.sort_values("length_鿡", ascending=False)
    frame_鿡["cum_counts"] = frame_鿡["counts"].cumsum()
    frame_鿡["cum_%"] = frame_鿡["cum_counts"].apply(lambda x: x/frame_鿡["counts"].sum())
    frame_鿡["series"] = "no"
    return frame_鿡.loc[frame_鿡[frame_鿡['cum_%']>size].index[0],'length_鿡']



# create/load preprocessed dataframe - basis corpus
data = create_corpus_dataframe.main()

# calucate the minimum size of juan to get 80% of the corpus juans
prop = 0.8
min_size = min_text_size(data_s, prop)
print("Minimum of juan-size: ", min_size)

ob = corpus_selection(data_s, min_size)
ob.copus_sized()
ob.output()



