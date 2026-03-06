#!/usr/bin/env python
# coding: utf-8

# The purpose of the file is to add two additional columns to the output of formulib outgrams.py. It will use as base the output file formtest_list.txt and add the columns: count of titles (in how many titles the ngram is occuring) and count of chapters (in how many chapters the ngram is occuring)
# The script is meant to be added to formulib p3 folder and to be executed after the run of outgrams.py.
# Input: the script will use as input the file op/formtest_list.txt
# Output: formtest_list_update.txt with two additional columns for title count and chapter count.



import glob
import os
import re


# place of sample folder
p_samples = os.path.dirname(__file__).replace("p3","samples")

# path to output folder
path_op = os.path.dirname(__file__).replace("p3","op")

# walk down to the source files
target_file = []
category = []
for item in list(os.walk(f'{p_samples}')):
    if item[2]:
        target_file.append(item[0])
        category.append(item[0].split("/")[-1])


def count_in_file(char, cat):
	juan = 0
	for path in target_file:
	    for file in glob.glob(f"{path}/*.txt"):
		    if cat in file:
			    with open(file, mode="r", encoding="utf-8") as output:
			    	text = output.read()
			    	if char in text:
			    		juan += 1
	return juan

	

def count_in_title(char, cat):
	title = []
	count = 0
	for path in target_file:
	    for file in glob.glob(f"{path}/*.txt"):
	    	name = os.path.basename(file).split("_")[0]
	    	if cat in file:
	    		with open(file, mode="r", encoding="utf-8") as output:
	    			text = output.read()
	    			if char in text:
	    				if name not in title:
	    					count += 1
	    					title.append(name)
	return count	

							


categ = ""
start = 0
with open(f"{path_op}/formtest_list_update.txt", mode="a", encoding="utf-8") as out:
	with open(f"{path_op}/formtest_list.txt", mode="r", encoding="utf-8") as ngram:
		for line in ngram.readlines():
			if start == 0:
				if "n-grams by category :" in line:
					start = 1
				else:
					out.write(line)
			if start == 1:
				if line.split(" ")[0].strip() in category:
					categ = line.split(" ")[0].strip()
					out.write(line)
				else:
					if re.search(r"^\d+", line):
						ngram = re.sub(" ","",line.strip())
						ngram = re.sub(r"\d+","",ngram.strip())
						l = line.split(" ")
						out.write(f"{l[0]} {l[1]} {l[2]} {l[3]} {count_in_file(ngram, categ)} {count_in_title(ngram,categ)} {' '.join(s for s in ngram)}\n")
					else:
						out.write(line)
			
		
