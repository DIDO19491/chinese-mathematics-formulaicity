<h2>One Genre, Many Formalisms: On Formulaic Language in Pre-Modern Chinese Mathematical Texts</h2>
<p>For some technical genres such as mathematics it is often assumed that their language exhibits formulaic characteristics. 
However, it is notoriously difficult to identify what properties exactly make language “formulaic” (Wray, 2002: 43). 
In order to nevertheless quantitatively assess the formulaicity of a corpus, Richard Forsyth has proposed a suite of computational tools titled formulib, which operates by “compiling a formulexicon from a corpus [...] and then us[es] coverage by elements of that formulexicon as an index of the degree to which a text [...] is pervaded by formulaic sequences” (Forsyth, 2021: 33). 
  In this study, we apply this suite to pre-modern (ca. 1st century CE to 18th century) Chinese mathematical texts. </p>
  <p>These texts are particularly interesting because they were written without modern symbolic notation systems, which could suggest more natural, less formulaic patterns of language use. However, previous analysis by Chemla (2006) of a work from the 13th century has shown that pre-modern Chinese mathematical texts can exhibit patterns of artificial language use, which she characterizes by restrictedness, also a key property of Forsyth's definition of formualic language (Forsyth 2021: 31). 
We extend such work analyzing single texts by taking a corpus-based approach that makes it possible to explore how wide-spread formulaic language was in the genre in general.</p>

<br>
<p>For the corpus creation procedure refer to folder <a href="https://github.com/DIDO19491/chinese-mathematics-formulaicity/tree/main/corpus_sampling">corpus_sampling</a>.</p>
<p>Details about the parameters for the formulib suit are given in folder <a href="https://github.com/DIDO19491/chinese-mathematics-formulaicity/tree/main/formulib_output">formulib_output</a>.</p>

<br>
<h3>Results</h3>

<p>Comparing the coverage in mathematics against other genres in the corpus (see Fig. 1), we can confirm that the mathematical language is more formulaic than the other subcategories. 
However, looking at the mathematical formulexicon not only in terms of the frequency of each item, but also its dispersion, measured with document frequency (see Fig. 3), it turns out that the n‑grams shared between more than a few texts are limited to a few common operations, such as “multiply it, obtaining n” (乗之得n), where n indicates our placeholder for numerals, and expressions for quantities, e.g. “n parts of n” (n分之n). 
Furthermore, running the suite using individual works instead of the entire genre as corpora, we can see that the degree of formulaicity varies drastically between the items (see Fig. 2).</p>
<br>

<img width="700px" height="auto" alt="distribution_category_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/output_analysis/coverage_category.png" />
<p>Figure 1: Coverage per genre, with translations from Wilkinson (2022: 1877)</p>

<br>
<img width="700px" height="auto" alt="distribution_category_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/output_analysis/coverage_math.png" />
<p>Figure 2: Coverage per title (mathematics only)</p>

<br>
<img width="700px" height="auto" alt="distribution_category_juans" src="https://github.com/DIDO19491/chinese-mathematics-formulaicity/blob/main/output_analysis/ngram_title_counts.png" />
<p>Figure 3: Distribution of document frequencies of n-grams in the formulexicon</p>

<br>
<h3>Discussion</h3>
<p>Although the result that the language of - at least some of the - mathematical texts was formulaic might not be very surprising, it serves as a confirmation that even before the advent of modern symbolic notation systems, mathematical knowledge was written down using a distinct type of language. A major limitation of the present study is that formulaicity was only examined through the lens of n-grams.
  These n-grams might in the future serve as starting points for further research into formulaic language in Chinese mathematics, for example by more closely examining the constructions that are used to express arithmetic operations.</p>

<br>
<h4>References</h4>
<p>Chemla, Karine. 2006. „Artificial Languages in the Mathematics of Ancient China“. Journal of Indian philosophy 34 (1/2): 31–56.</p>
<p>Forsyth, Richard. 2021. „Cascading collocations: Collocades as correlates of formulaic language“. In Formulaic language - Theories and methods, herausgegeben von Aleksandar Trklja und Łukasz Grabowski. 
Berlin: Language Science Press.</p>
<p>Wilkinson, Endymion. 2022. Chinese History - A New Manual. Enlarged sixth edition. Cambridge, Massachusetts: Harvard University Asia Center.</p>
<p>Wray, Alison. 2002. Formulaic Language and the Lexicon. Cambridge: Cambridge University Press.</p>
