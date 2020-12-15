# Description

## **1. Data**

1) Cloned the selected GitHub projects:

	*git clone*

2) Extracted commit comments (both tittles and bodies) of the selected projects:

	*git log --after="2020-02-20" --before="2020-08-20" --pretty=format:"CommitHash: %H AuthorDate: %ai CommitterDate: %ci SubjectTitleLine: %s BodyMessage: %b" > fullCommitMessages.txt*

3) Extracted code logs of the selected projects:

	*git log -p --reverse --after="2020-02-20" --before="2020-08-20"> "$patch_output_path/${arr[-1]}.txt"*



## **2. Calculating Comment Quality Metrics**

### **2.1 Expressiveness of Comment Titles**

	There are five main steps in our process for calculating the expressiveness of the comment titles: 
	1) rating of a sample by human judges; 
	2) calculating inter-rater agreement; 
	3) extracting comment features for different expressiveness categories; 
	4) replacing name entities of the comment titles; 
	5) building a decision tree to measure the expressiveness. 

- **2.1.1 Human Judges**

		To measure the expressiveness of the comment titles, we used human expertise. To do this, 
		we extracted 400 comment titles from the project data set. Then we asked three software 
		experts to rate the expressiveness or usefulness of the selected comment titles.

		Each specific comment title was rated by two different experts. Each comment title had an 
		integer rating score from 0 to 3. 
		
		The 400 rated comment titles are shown in 400RatedCommentTitles.xlsx.

		3 means the comment is very useful and informative;
		2 means the comment is somewhat useful and informative;
		1 means the comment is slightly useful and informative;
		0 means the comment is useless;
		NR means Not Rated;
	
- **2.1.2 Inter-rater Agreement (IRA)**

		Once we had the rated comment titles from all three raters, we scored the agreement 
		score manually as follow: 
		
		a) If the comment title had the same rating from both raters, we marked it 1.0; 
		b) If the comment title had no more than one category difference, we marked it 0.5; 
		   For instance, if one rater gave the comment title a score of 3 and the other rater gave 2; 
		3) Otherwise, we marked it 0.0 (call these the disagreed comment title).

		For each pair of raters, the IRA is calculated as the average agreement score over all 
		the shared comment titles. We calculated the Inter-rater Agreement (IRA) both including 
		and excluding the comment titles marked as 0. 

- **2.1.3 Extracting Comment Features for Each Category**
	
		We examined the comment titles that received identical ratings from at least two judges.

		We defined the following set of dimensions or features for classifying comment expressiveness:
		1) comment length;
		2) number of instances of function/file/variable/constant, etc.
		3) whether comment contains bug number;
		4) whether the comment is for a merge commit;
		5) whether the comment contains some special phrases, 
		   for example, “instead of”, “so that”, “for example”, “when”, “where”, etc.

		The scripts for feature extraction is shown in featureExtraction.ipynb. 
		After extracting features for the comment titles, we coded each comment 
		title according to above dimensions.

- **2.1.4 Name entity replacement**

		We observed that many of the comments, both comment title and comment body, 
		include technical terms and project specific names of variables, function, 
		file, constant, class, modules, etc. 
		
		Before we extracted the features for all comment titles, We defined five 
		standard terms: FILE, VARIABLE, FUNCTION, CONSTANT, and BUG_NUMBER, 
		then we identified the file/function/variable/constant/bug number 
		from the comments and replaced them with above standard terms respectively.

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

- **2.1.5 Decision tree**

		After running our feature extraction scripts, we had a set of features along with 
		their features dimension values. We separated the data into a training set versus 
		a testing set and used the training set to train a decision tree classifier using 
		sklearn module with entropy as splitting criterion.  
		
		The scripts for building the decision tree is shown in buildingDecisionTree.ipynb
		
		Once we had the decision tree, we applied the feature extraction script to all 
		the comment titles of our projects to acquire the features, then turned the 
		features into dimensions values for each comment title of each project. 
		Finally, we used the decision tree to categorize each of the comment 
		titles from the project and get back a category from 1 to 3. 



### **2.2 Length of Comment Titles**

		We counted the total number of words as the length of each comment title 
		and removed the punctuation but kept the stop words for each comment title. 
		We examined the standard deviation (SD) of comment length, as well as the average, 
		to avoid inflation by a few outliers. For the projects that had excessive SD 
		(greater than 5.0), we removed the top 10% and bottom 10% (in length) of the 
		comment titles in those projects, and then recalculated the mean of the lengths. 
		
		The scripts for calculating the comment length is shown in commentLength.ipynb


### **2.3 Uniqueness of Comment Titles**

		We measured precentage of unique commit comment by defining the ratio of number 
		of unique commits to the total number of commits for each project.we exclude the stop words.
		
		The scripts for calculating the comment uniqueness is shown in commentUniqueness.ipynb


### **2.4 Percentage of Commits with Body**

		We simply counted the number of commit comments with a body for each project 
		and divided it by the total number of commits.
		
		Since the logs we extracted from GitHub have some build-in format, 
		expecially for the comment bodies, So, before checking if the commit 
		contains a body message, we first format the comment bodies, for example, 
		removing the empty lines and useless spaces, etc. This is to make it easier 
		to calculate this metric and also the word frequency metrics. The scripts used 
		to format/clean the comment bodies is shown the formatCommentBodies.ipynb		
		
		Finally, we calculated this metric using script commentUniqueness.ipynb


### **2.5 Word Frequency Rank of Comments**

		In this metric, we used the comments that have been formatted/cleaned 
		by using formatCommentBodies.ipynb 
		
		when we measured the percentage of commits with body metric above. 
		We measure the word frequency rank for both comment tiles and comment 
		tiles plus bodies. That is, we have two word frequency rank metrics here.
		
		we referred to a word frequency corpus, which is derived from Google’s N-gram corpus.
		
		a) First, we sorted all the words in the corpus by their frequency, 
		in descending order by frequency. This is done using scripts in 
		WFpart1_sortCorpusByWordFrequency.ipynb;
		
		b) Second, since there are many other informations in the code logs 
		we have extracted, for example the author and date, etc. We now just 
		want the comment tiles and the comment bodies only, so, we extract the
		the comment tiles and the comment titles plus bodies for each project. 
		This is just to make the later calculation easier and cleaner. 
		This step was done in WFpart2_storeTitlesAndBodies.ipynb
		
		c) After we have extracted the comment tiles and the comment titles 
		plus bodies for each project, we found out the English words that now 
		in the corpus, then we went through the word list and did some manual 
		replacement for the following cases:

			-  clearly misspelled words;
			-  derived words, in which case we manually replaced with their "stems", 
			   for instance, plurals, verb forms other than the present, etc.;
			-  very common abbreviations e.g. “mgmt.” will be replaced by “management”; 
			-  words that look like phrases that are missing spaces. such as "quickfix" 
			   will be changed to “quick fix”.

		This step was done with the script WFpart3_findWordsNotInCorpus.ipynb. 
		The "words" that have been replaced were stored in the txt file in the following format:
		
			[the original word] : [the replaced word]
			accomodate : accommodate
			accomodations : accommodations
		
		
		d) After the manual replacement, we calculated the average word frequency rank 
		for both comment titles and comment titles plus bodies. The replaced words were 
		searched in the corpus.
		
		The calculation was done with the scripts WFpart4_wordFrequencyRankCalculation.ipynb





## **3. Code Quality Metrics**

### **3.1 Thrashing Frequency**

		We considered the following three cases as thrashing:
		
		a)	Line removed then added back within N successive commits;
		b)	Line added then removed within N successive commits;
		c)	Repeated modifications to the same region of code within N successive commits;
		
		After the code diff for each project is extracted, the sub-metric a) and b) are calculated 
		using script thrashingFrequencySubMetricab.ipynb, sub-metric c) is calculated using script 
		thrashingFrequencySubMetricc.ipynb.



### **3.2 Average Commit Size**



### **3.3 Percentage of Risky Commits**



### **3.4 Distribution of Modified Code**







