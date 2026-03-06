#!/usr/bin/env python
# coding: utf-8

# generates metafile from formulib samples files with structure: samples/<folders>/<folder>/text-files
# as required the metafile follows the structure: prepath	filename	doctype
# this script is supposed to be in p3 and executed first (this is alternatively to formulib/p3/metaget.py
# Input: files in "samples", that means all samples to be analyzed has to be placed in samples in respective structure
# Output: metafile


import glob
import os
import re

p_samples = os.path.dirname(__file__).replace("p3","samples")
path_mets = os.path.dirname(__file__).replace("p3","mets")

# walk down to the source files
target_file = []
for item in list(os.walk(f'{p_samples}')):
    if item[2]:
        target_file.append(item[0])


with open(f"{path_mets}/data_met.txt", mode="a", encoding="utf-8") as out:
    out.write("prepath\tfilename\tdoctype\n")
    for path in target_file:
        for folder in glob.glob(f"{path}/*.txt"):
            folder_name = os.path.basename(folder)
            out.write(f"{folder}/{folder.split('/')[-2]}/\t{folder.split('/')[-1]}\t{folder.split('/')[-2]}\n")
		
