# Description

## **1. Data**

We used *git clone* to clone the GitHub projects and extracted commit comments (both tittles and bodies) and code log from GitHub using following scripts respectively:

*git log --after="2020-02-20" --before="2020-08-20" --pretty=format:"CommitHash: %H AuthorDate: %ai CommitterDate: %ci SubjectTitleLine: %s BodyMessage: %b" > fullCommitMessages.txt*

*git log -p --reverse --after="2020-02-20" --before="2020-08-20"> "$patch_output_path/${arr[-1]}.txt"*

## **2. Comment Expressiveness Measure**

- **The 400 rated comment titles are shown in 400RatedCommentTitles.xlsx.**

		3 means the comment is very useful and informative;
		2 means the comment is somewhat useful and informative;
		1 means the comment is slightly useful and informative;
		0 means the comment is useless.
		NR means Not Rated

- **The main script for doing the feature extraction manually for the comment titles is shown in featureExtraction.ipynb**

- **Name entity replacement**

		We defined five standard terms: FILE, VARIABLE, FUNCTION, CONSTANT, and 
		BUG_NUMBER, then we identified the file/function/variable/constant/bug number 
		and replaced them with above standard terms respectively.

		The function names and variable names replacement scripts for each programming 
		group are shown in the following files:

			a) FunVarReplacementForPython.ipynb
			b) FunVarReplacementForC.ipynb
			c) FunVarReplacementForJavaScript.ipynb
			d) FunVarReplacementForJava.ipynb

		The file names, constant names and bug numbers replacement scripts for all projects 
		(all four programming language projects) are shown in the following files:

			a) replaceFileNames.ipynb
			b) replaceConstants.ipynb
			c) replaceBugNumbers.ipynb

		To do the name entity replacement for each language group, the order to run the scripts 
		should be: FunVarReplacement – replaceFileNames – replaceConstants – replaceBugNumbers

- **Decision tree**

		We trained a decision tree classifier using sklearn module with entropy as splitting criterion. 
		The main script is shown in buildingDecisionTree.ipynb
		
## **3. Thrashing Frequency Measure**

		We considered the following three cases as thrashing:
		
		a)	Line removed then added back within N successive commits;
		b)	Line added then removed within N successive commits;
		c)	Repeated modifications to the same region of code within N successive commits;
		
		After the code diff for each project is extracted, the sub-metric a) and b) are calculated 
		in script thrashingFrequencySubMetricab.ipynb, sub-metric c) is calculated in script 
		thrashingFrequencySubMetricc.ipynb.


		

