#!/usr/bin/env python
# coding: utf-8

# generates parapath file (parameter file) from formulib meta-file
# this script is supposed to be in folder p3 and executed after metaget_auto.py
# Input: meta-file from formulib/mets/data_met.txt
# Output: formtest-file in parapath/data_formtest.txt


import glob
import os
import re

path_samples = os.path.dirname(__file__).replace("p3","samples")
path_mets = os.path.dirname(__file__).replace("p3","mets")
path_para = os.path.dirname(__file__).replace("p3","parapath")

for file in glob.glob(f"{path_mets}/*_met.txt"):
	file_name = os.path.basename(re.sub("_met.txt", "",file))
	with open(f"{path_para}/{file_name}_formtest.txt",mode="a", encoding="utf-8") as out:
		out.write("comment\tformulib testing\njobname\tformtest\n")
		out.write(f"metafile\t{file}\n")
		out.write(f"outmeta1\t{re.sub('_met.txt','_training.txt',file)}\n")
		out.write(f"outmeta2\t{re.sub('_met.txt','_testing.txt',file)}\n")
		out.write(f"randfrac\t0.61803398875\n")
		out.write(f"trainmet\t{re.sub('_met.txt','_training.txt',file)}\n")
		out.write(f"testmeta\t{re.sub('_met.txt','_testing.txt',file)}\n")
		out.write(f"metaflic\t{re.sub('_met.txt','_testing.txt',file)}\n")
		out.write(f"wordonly\t1\nmaxtops\t30\ntopgrams\t80\noutforms\t80\nminiglen\t3\nmaxiglen\t8\n##outpath\tc:\\fout\\\ntopkeys\t64\n")

