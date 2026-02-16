<h2>Generating formulib output</h2>

The core metric to determine the degree of formulaicity used by Forsyth is coverage. Coverage is defined as the number of tokens of the text that occur in the text as a part of at least one of the n-grams in the formulexicon, divided by the total number of tokens. 
The formulexicon consists, with our choice of hyperparameters, of the 80 most frequent n-grams, 3 ≤ n ≤ 8, excluding n-grams made up purely of stop words (Forsyth, 2021: 37-40).
<br>

The formulib run was processed based on two corpora:
<ul>
  <li>output over all categories</li>
<li>output based on category "Mathematics" only</li>
</ul>

The formulib suit usually splits the dataset into train and test data.
We did run with and without split into train and test only for the complete corpus (all categories).
<br>
<h4>References</h4>
Forsyth, Richard. 2021. „Cascading collocations: Collocades as correlates of formulaic language“. In Formulaic language - Theories and methods, herausgegeben von Aleksandar Trklja und Łukasz Grabowski. Berlin: Language Science Press.
