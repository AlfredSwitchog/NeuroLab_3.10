
This dataset contains a collection of paradigmatic relation pairs that
were created in a two-step process, making use of two types of
human-generated data: (1) human suggestions of semantically related
word pairs, and (2) human ratings of semantic relations between word
pairs.

We collected semantically related word pairs for the paradigmatic
relations antonymy, synonymy, and hypernymy for the three word classes
nouns, verbs, and adjectives. For this purpose we implemented two
experiments involving human participants. Starting with a set of
target words, in the first experiment participants were asked to
propose suitable antonyms, synonyms and hypernyms for each of the
targets. For example, for the target verb befehlen (`to command'),
participants proposed antonyms such as gehorchen (`to obey'), synonyms
such as anordnen (`to order'), and hypernyms such as sagen (`to
say'). In the second experiment, participants were asked to rate the
strength of a given semantic relation with respect to a word pair on a
6-point scale. For example, workers would be presented with a pair
"wild-free" and asked to rate the strength of antonymy between the two
words. All word pairs were assessed with respect to all three relation
types.


----- DATA

The folder contains the following files:

- A sub-directory "targets" contains the files with randomly chosen
  GermaNet experiment targets (regarding adjectives, nouns, verbs).

- A file "exp-generation.txt" contains the generated relation pairs
  and their strength. The file is organised in five TAB-separated
  columns, containing the target, the response, the strength of the
  response (i.e., how many participants generated this relation pair),
  the part-of-speech of the target, and the target semantic relation.

- A sub-directory "exp-rating" contains the result files of the rating
  experiment. Each file is specified for a part-of-speech and a target
  relation. The files each contain 10 TAB-separated columns, with the
  target relation, the target word, the generated response, the number
  of ratings for a strength of 0/1/2/3/4/5, and the number of ratings
  indicating the number of "I don't know" cases.


----- REFERENCE (see lg-lp-14.pdf):

Silke Scheible and Sabine Schulte im Walde:
"A Database of Paradigmatic Semantic Relation Pairs for German Nouns, Verbs, and Adjectives."
In: Proceedings of the COLING Workshop on Lexical and Grammatical Resources for Language Processing. Dublin, Ireland, August 2014.

