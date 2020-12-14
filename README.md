# Documentation

**1. Data**

We used git clone to clone the GitHub projects and extracted commit comments (both tittles and bodies) from GitHub using following script:

git log --after="2020-02-20" --before="2020-08-20" --pretty=format:"CommitHash: %H AuthorDate: %ai CommitterDate: %ci SubjectTitleLine: %s BodyMessage: %b" > fullCommitMessages.txt

**2. Comment expressiveness measure**

-The 400 rated comment titles are shown in 400RatedCommentTitles.xlsx.

3 means the comment is very useful and informative;

2 means the comment is somewhat useful and informative;

1 means the comment is slightly useful and informative;

0 means the comment is useless.

NR means Not Rated

- The main script for doing the feature extraction manually for the comment titles is shown in featureExtraction.ipynb

- Name entity replacement

We defined five standard terms: FILE, VARIABLE, FUNCTION, CONSTANT, and BUG_NUMBER, then we identified the file/function/variable/constant/bug number and replaced them with above standard terms respectively.

The function names and variable names replacement scripts for each programming group are shown in the following files respectively:

FunVarReplacementForPython.ipynb

FunVarReplacementForC.ipynb

FunVarReplacementForJavaScript.ipynb

FunVarReplacementForJava.ipynb

The file names, constant names and bug numbers replacement scripts for all projects (all four programming language projects) are shown in the following files respectively:

replaceFileNames.ipynb

replaceConstants.ipynb

replaceBugNumbers.ipynb

To do the name entity replacement for each language group, the order to run the scripts should be: FunVarReplacement – replaceFileNames – replaceConstants – replaceBugNumbers

- Decision Tree

We trained a decision tree classifier using sklearn module with entropy as splitting criterion. The main script is shown in buildingDecisionTree.ipynb

