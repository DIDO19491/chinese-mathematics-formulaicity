<b>1) Corpus Sampling</b><br>

The corpus for the study is based on the “Masters Branch” (zibu 子部) of the “Complete Library of the Four Treasuries” (Siku quanshu 四庫全書, compiled 1772-1782). The “Masters Branch” contains subcategories corresponding to different genres, including philosophy, arts, and different sciences, among them mathematics (Wilkinson, 2022: 1863-1877). Digital versions of the texts were obtained from the “Kanseki Repository 漢籍リポジトリ” (Wittern, 2016). <br>

In a preprocessing step, pre- and postface chapters (juan 卷) were removed. Two chapters from category shushu (Kanripo No. KR3g0012 "卷四" und "卷五) have been removed due to prepresentation problems (the text contains nearly only counting rods and squares). Counting rods and numerals, both frequent mathematical texts, were replaced with two distinct place-holder characters, since we are interested in exploring formulaic patterns with numbers, e.g. how a multiplication of a number by another number is expressed, but not numbers as formulaic patterns on their own.  <br>

<i>place-holders characters:  </i> <br>
numbers: '鿡' <br>
counting rods: '钅' <br>
failures/squres: '讠' <br>

In terms of the contribution of each subcategory and the lengths of the texts within each subcategory, the corpus is highly unbalanced. Hence, random sampling was used to obtain selections of equal text length (based on the 80% quantile of lengths, 3.654 characters ) and an equal number of chapters for each subcategory (118, the number in “Math”). The final corpus consists of 11 subcategories with 430.110 tokens (modelling each Chinese character as a token) each, giving a total of 4.731.210 tokens. For validation purposes, the sampling was conducted ten times. <br>


<img width="982" height="525" alt="distribution_category_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/size_of_categories.png" />

<img width="982" height="525" alt="distribution_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/distribution_text_length.png" />

<i>Chapter lengt statistics:</i> <br>
        => Median:  7230.5 characters <br>
        => Quantil 0.25:  4175.75 characters <br>
        => Quantil 0.75:  12148.75 characters <br>

<img width="982" height="525" alt="cumulated_distribution_of_juan" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/comulated_text-length.png" />
<img width="982" height="525" alt="box_juan_len_no_num" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/chapter_length_std_numbers.png" />


Based on the median of category 'suanfa' (7216 characters) only two other categories have longer juans, such as 'yijia' and 'leishu'.

On the base of 80% of total chapters - length per chapter > 3645 (characters, with number)




