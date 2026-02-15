#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This script's purpose is the data download from the Kanripo repository: https://github.com/kanripo
# Output: downloaded data is saved as json-objects with following tags: id == Kanripo internal text number; id_name == Kanripo text name; juan == juan number; title == title of the text; text == chinese text

import re
import glob
import os
import requests
import string
import json


class text_pre:
    
    def __init__(self, cat, sets):
        self.cat = cat
        self.file_name = sets.split(" ")[0]
        self.out_name = sets.split(" ")[1]
        self.text = []
        self.new_text = ""
        
        
    def correct_text(self, tex):
        zwText = ""
        text = re.sub("#.+\n", "", tex)
        text = re.sub("<.+>", "", text)
        text = re.sub("¶", "", text)
        text = re.sub("&.+;", "", text)
        zwText = "".join(x for x in text.split())
        return zwText
         
        
    def json_container(self):
        with open(f"data_KR3_子部/{self.cat}/{self.file_name}.json", encoding="utf-8", mode="w") as out:
            json.dump(self.text, out, ensure_ascii=False, indent=4)
        
        
    def download(self):
        count = 0
        text_dic = dict()
        while True:
            numb = 0
            if len(str(count)) == 1:
                numb = f"00{count}"
            if len(str(count)) == 2:
                numb = f"0{count}"
            url = f"https://raw.githubusercontent.com/kanripo/{self.file_name}/refs/heads/master/{self.file_name}_{numb}.txt"
            t = requests.get(url)
            juan = "".join([x.strip().split(" ")[1] for x in list(set(re.findall("JUAN.+\n",t.text)))])
            title = "".join([x.strip().split(" ")[1] for x in re.findall("TITLE.+\n",t.text)])
            text_dic = {"id": self.file_name,
                        "id_name": self.out_name,
                        "juan": juan,
                        "title": title,
                       "text": self.correct_text(t.text)}
            count += 1
            if t.status_code == 404:
                break
            self.text.append(text_dic)
        return self.json_container()



def container_texts(title):
    url = f"https://raw.githubusercontent.com/kanripo/KR-Catalog/refs/heads/master/KR/{title}"   # url to the Kanripo repository, for the corpus the forcus is on texts belonging to "zibu" 子部
    return [re.sub("\*\*\* ", "", name.strip()) for name in re.findall(r"\*\*\* KR3.+\n", requests.get(url).text)]

liste_alpha = list(string.ascii_lowercase)[0:12]
liste_cont = {"a": "kongzi", "b": "bingjia", "c":"fajia", "d":"nongjia", "e":"yijia",
             "f":"tianwensuanfa", "g":"shushu", "h":"yishu", "i":"pulu", "j":"zajia", "k":"leishu", "l":"xiaoshuo"}


for x in liste_alpha:
    if not os.path.exists(f"{liste_cont.get(x)}/"):
        os.makedirs(f"data_KR3_子部/{liste_cont.get(x)}/")
    for i in container_texts(f"KR3{x}.txt"):
        prep_text = text_pre(liste_cont.get(x),i)
        prep_text.download() # creates a json-object for each category
        
# ===> script added: split tianwensuanfa category into tianwen and suanfa!!!!
        
