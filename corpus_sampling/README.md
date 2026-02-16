<h2>Corpus Sampling</h2><br>

The corpus for the study is based on the “Masters Branch” (zibu 子部) of the “Complete Library of the Four Treasuries” (Siku quanshu 四庫全書, compiled 1772-1782). The “Masters Branch” contains subcategories corresponding to different genres, including philosophy, arts, and different sciences, among them mathematics (Wilkinson, 2022: 1863-1877). Digital versions of the texts were obtained from the “Kanseki Repository 漢籍リポジトリ” (Wittern, 2016). <br>

In a preprocessing step, pre- and postface chapters (juan 卷) were removed. Two chapters from category shushu (Kanripo No. KR3g0012 "卷四" und "卷五) have been removed due to prepresentation problems (the text contains nearly only counting rods and squares). Counting rods and numerals, both frequent mathematical texts, were replaced with two distinct place-holder characters, since we are interested in exploring formulaic patterns with numbers, e.g. how a multiplication of a number by another number is expressed, but not numbers as formulaic patterns on their own.  <br>

<h6>place-holders characters:  </h6>
<ul>
    <li>numbers: '鿡'</li>
        <li>counting rods: '钅'</li>
        <li>failures/squres: '讠'</li>  
</ul>

<br>

<img alt="distribution_category_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/size_of_categories.png" />

<img alt="distribution_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/distribution_text_length.png" />

<h6>Chapter lengt statistics:</h6>
<ul>
        <li>Median:  7230.5 characters</li>
        <li>Quantil 0.25:  4175.75 characters</li>
        <li>Quantil 0.75:  12148.75 characters</li>
</ul>

<br>

<img alt="cumulated_distribution_of_juan" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/comulated_text-length.png" />
<img alt="box_juan_len_no_num" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/chapter_length_std_numbers.png" />

<br>
In terms of the contribution of each subcategory and the lengths of the texts within each subcategory, the corpus is highly unbalanced. Hence, random sampling was used to obtain selections of equal text length (based on the 80% quantile of lengths, 3.654 characters ) and an equal number of chapters for each subcategory (118, the number in “Mathematics”). The final corpus consists of 11 subcategories with 430.110 tokens (modelling each Chinese character as a token) each, giving a total of 4.731.210 tokens. For validation purposes, the sampling was conducted ten times. <br>
<br>

<img width="982" height="525" alt="cumulated_distribution_of_juan" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/corpus_sampling/statistics/overview_corpus_statistic.png" />

<h4>References</h4>
<p>Wilkinson, Endymion. 2022. Chinese History - A New Manual. Enlarged sixth edition. Cambridge, Massachusetts: Harvard University Asia Center. </p>
<p>Wittern, Christian. 2016. „Kanseki Repository“. CIEAS Research Report 2015 Special issue: 1–80. </p>
<p>Link to Kanripo repository: https://github.com/kanripo<p>


