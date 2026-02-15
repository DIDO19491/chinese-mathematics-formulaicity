<b>1) Sampling</b><br>

<i>Target of sampling:</i> <br>
    Same size of juan-chunks & same number of chunks per category <br>
    => to get equal size of text samples per category! <br>
    => reference size is category ‚math‘ <br>

<img width="982" height="525" alt="distribution_category_juans" src="https://github.com/user-attachments/assets/c68187c9-256a-467e-a72a-c1149e5ddf79" />

<img width="982" height="525" alt="distribution_juans" src="https://github.com/user-attachments/assets/c98364d0-2188-49d9-bd06-fcaa01fd8c00" />

<i>Verteilung der 'juan'-Längen:</i> <br>
        => Median:  7230.5 characters <br>
        => Quantil 0.25:  4175.75 characters <br>
        => Quantil 0.75:  12148.75 characters <br>

<img width="982" height="525" alt="cumulated_distribution_of_juan" src="https://github.com/user-attachments/assets/19baa659-f523-4869-af73-a426fb2cdb6f" />
<img width="982" height="525" alt="box_juan_len_no_num" src="https://github.com/user-attachments/assets/50f38258-7f65-45ff-a028-bb0c32944c0f" />


Based on the median of category 'math' (7216 characters) only two other categories have longer juans, such as 'yijia' and 'leishu'.

On the base of 80% of total juans - length per 'juan' > 3645 (characters, with number)
<img width="1965" height="574" alt="overview_corpus_data" src="https://github.com/user-attachments/assets/c42b5e8b-6e87-41f7-a34f-ee5703932649" />





<b>FAZIT</b> <br>
Based on the corpus requirements for this task a striktly balanced corpus is needed. The balance is related to the equal numbers of juans per category and equal juan length throughout the corpus. Since the focus of this analysis lies on the category 'math', this category is considered as the base line regarding the number of juans to be considered, but also in terms to a certain min. juan-length. Based on 80% of all juans, we receive a minimum length of 3.645 characters. For the category 'math' there are 118 juans (based on standardized number-characters) with length larger than 3.645 characters, which can be considered. Consequently that leads to following corpus properties:

    => category 'fajia' and 'bingjia' have too less juans to be considered!
    => The baseline of 80% of all juans is fixed, to get a min. juan size of 3.645 for all categories.
    => Based on 80% of math-juans with standarized (no) numbers leads to 118 juans for all categories.
    => All juans longer than 3.645 characters will be cutted by a random text-sampling.
