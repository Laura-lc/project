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
	integer rating score from 0 to 3. The 400 rated comment titles are shown in 400RatedCommentTitles.xlsx.
	
	3 means the comment is very useful and informative;
	2 means the comment is somewhat useful and informative;
	1 means the comment is slightly useful and informative;
	0 means the comment is useless;
	NR means Not Rated;
	
- **2.1.2 Inter-rater Agreement (IRA)**

	Once we had the rated comment titles from all three raters, we scored the agreement score manually as follow: 
	a) If the comment title had the same rating from both raters, we marked it 1.0; 
	b) If the comment title had no more than one category difference, we marked it 0.5; 
	   For instance, if one rater gave the comment title a score of 3 and the other rater gave 2; 
	3) Otherwise, we marked it 0.0 (call these the disagreed comment title).
	
	For each pair of raters, the IRA is calculated as the average agreement score over all the shared comment titles.
	We calculated the Inter-rater Agreement (IRA) both including and excluding the comment titles marked as 0. 

- **2.1.3 Extracting Comment Features for Each Category**
	
	We examined the comment titles that received identical ratings from at least two judges.
	
	We defined the following set of dimensions or features for classifying comment expressiveness:
	1) comment length;
	2) number of instances of function/file/variable/constant, etc.
	3) whether comment contains bug number;
	4) whether the comment is for a merge commit;
	5) whether the comment contains some special phrases, for example, “instead of”, “so that”, “for example”, “when”, “where”, etc.
	
	The scripts for feature extraction is shown in featureExtraction.ipynb. After extracting features for the comment titles, 
	we coded each comment title according to above dimensions.

- **2.1.4 Name entity replacement**

		We observed that many of the comments, both comment title and comment body, include technical 
		terms and project specific names of variables, function, file, constant, class, modules, etc. 
		
		Before we extracted the features for all comment titles, We defined five standard terms: FILE, 
		VARIABLE, FUNCTION, CONSTANT, and BUG_NUMBER, then we identified the file/function/variable/
		constant/bug number from the comments and replaced them with above standard terms respectively.

		The function names and variable names replacement scripts for each programming group are shown 
		in the following files:

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

		After running our feature extraction scripts, we had a set of features along with their features dimension values.
		We separated the data into a training set versus a testing set and used the training set to train a decision tree 
		classifier using sklearn module with entropy as splitting criterion.  
		
		The scripts for building the decision tree classifier is shown in buildingDecisionTree.ipynb
		
		Once we had the decision tree, we applied the feature extraction script to all the comment 
		titles of our projects to acquire the features, then turned the features into dimensions values 
		for each comment title of each project. Finally, we used the decision tree to categorize each of the 
		comment titles from the project and get back a category from 1 to 3. 



### **2.2 Length of Comment Titles**




### **2.3 Uniqueness of Comment Titles**




### **2.4 Percentage of Commits with Body**





### **2.5 Word Frequency Rank of Comments**





## **3. Code Quality Metrics**

### **3.1 Code Thrashing Frequency Measure**

		We considered the following three cases as thrashing:
		
		a)	Line removed then added back within N successive commits;
		b)	Line added then removed within N successive commits;
		c)	Repeated modifications to the same region of code within N successive commits;
		
		After the code diff for each project is extracted, the sub-metric a) and b) are calculated 
		using script thrashingFrequencySubMetricab.ipynb, sub-metric c) is calculated using script 
		thrashingFrequencySubMetricc.ipynb.


### **3.2 Thrashing Frequency**



### **3.3 Average Commit Size**



### **3.4 Percentage of Risky Commits**



### **3.5 Distribution of Modified Code**







