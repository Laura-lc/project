# Description

## **1.  Data**

1.1  Cloned the selected GitHub projects:

	git clone

1.2  Extracted commit comments (both tittles and bodies) of the selected projects:

	git log --after="2020-02-20" --before="2020-08-20" --pretty=format:"CommitHash: %H AuthorDate: %ai CommitterDate: %ci SubjectTitleLine: %s BodyMessage: %b" > fullCommitMessages.txt

1.3  Extracted code logs of the selected projects:

	git log -p --reverse --after="2020-02-20" --before="2020-08-20"> "$patch_output_path/${arr[-1]}.txt"



## **2.  Calculating Comment Quality Metrics**

### **2.1  Expressiveness of Comment Titles**

	There are five main steps in our process for calculating the expressiveness of the comment titles: 
	
	1) rating of a sample by human judges; 
	
	2) calculating inter-rater agreement; 
	
	3) extracting comment features for different expressiveness categories; 
	
	4) replacing name entities of the comment titles; 
	
	5) building a decision tree to measure the expressiveness. 

- **2.1.1  Human Judges**

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
	
- **2.1.2  Inter-rater Agreement (IRA)**

		Once we had the rated comment titles from all three raters, we scored the agreement 
		score manually as follow: 
		
		a) If the comment title had the same rating from both raters, we marked it 1.0; 
		
		b) If the comment title had no more than one category difference, we marked it 0.5; 
		   For instance, if one rater gave the comment title a score of 3 and the other rater gave 2; 
		   
		c) Otherwise, we marked it 0.0 (call these the disagreed comment title).

		For each pair of raters, the IRA is calculated as the average agreement score over all 
		the shared comment titles. We calculated the Inter-rater Agreement (IRA) both including 
		and excluding the comment titles marked as 0. 

- **2.1.3  Extracting Comment Features for Each Category**
	
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

- **2.1.4  Name entity replacement**

		We observed that many of the comments, both comment title and comment body, 
		include technical terms and project specific names of variables, function, 
		file, constant, class, modules, etc. 
		
		Before we extracted the features for all comment titles, We defined five 
		standard terms: FILE, VARIABLE, FUNCTION, CONSTANT, and BUG_NUMBER, 
		then we identified the file/function/variable/constant/bug number 
		from the comments and replaced them with above standard terms respectively.

		The function names and variable names replacement scripts for each programming 
		group are shown in the following files:

			FunVarReplacementForPython.ipynb,  
			FunVarReplacementForC.ipynb
			FunVarReplacementForJavaScript.ipynb,  
			FunVarReplacementForJava.ipynb

		The file names, constant names and bug numbers replacement scripts for all projects 
		(all four programming language projects) are shown in the following files:

			replaceFileNames.ipynb,  
			replaceConstants.ipynb,  
			replaceBugNumbers.ipynb

		To do the name entity replacement for each language group, the order to run the scripts 
		should be: FunVarReplacement – replaceFileNames – replaceConstants – replaceBugNumbers

- **2.1.5  Decision tree**

		After running our feature extraction scripts, we had a set of features along with 
		their features dimension values. 
		
		We separated the data into a training set versus a testing set and used the training 
		set to train a decision tree classifier using sklearn module with entropy as splitting 
		criterion.  
		
		The scripts for building the decision tree is shown in buildingDecisionTree.ipynb
		
		Once we had the decision tree, we applied the feature extraction script to all 
		the comment titles of our projects to acquire the features, then turned the 
		features into dimensions values for each comment title of each project. 
		
		Finally, we used the decision tree to categorize each of the comment titles from 
		the project and get back a category from 1 to 3. 



### **2.2  Length of Comment Titles**

		We counted the total number of words as the length of each comment title 
		and removed the punctuation but kept the stop words for each comment title. 
		
		For the projects that had excessive SD (greater than 5.0), we removed the top 
		10% and bottom 10% (in length) of the comment titles in those projects, and 
		then recalculated the mean of the lengths. 
		
		The scripts for calculating the comment length is shown in commentLength.ipynb


### **2.3  Uniqueness of Comment Titles**

		We measured precentage of unique commit comment by defining the ratio of number 
		of unique commits to the total number of commits for each project.we excluded the stop words.
		
		The scripts for calculating the comment uniqueness is shown in commentUniqueness.ipynb


### **2.4  Percentage of Commits with Body**

		We simply counted the number of commit comments with a body for each project 
		and divided it by the total number of commits.
		
		Since the logs we extracted from GitHub have some build-in format, expecially 
		for the comment bodies, So, before checking if the commit contains a body message,
		we first format the comment bodies, for example, removing the empty lines and 
		useless spaces, etc. 
		
		This is to make it easier to calculate this metric and also the word frequency metrics. 
		The scripts used to format the comment bodies is shown the formatCommentBodies.ipynb		
		
		Finally, we calculated this metric using script commentUniqueness.ipynb


### **2.5  Word Frequency Rank of Comments**

		In this metric, we used the comments that have been formatted/cleaned 
		by using formatCommentBodies.ipynb when we measured the percentage of 
		commits with body metric above. 
		
		We measure the word frequency rank for both comment tiles and comment 
		tiles plus bodies. That is, we have two word frequency rank metrics here.
		
		We referred to a word frequency corpus, someone derived it from Google’s N-gram corpus.
		http://storage.googleapis.com/books/ngrams/books/datasetsv2.html
		https://raw.githubusercontent.com/earonesty/dotfiles/master/frequent.js
		
		a)   First, we sorted all the words in the corpus by their frequency, in descending order 
		     by frequency. This was done using scripts in WFpart1_sortCorpusByWordFrequency.ipynb;
		
		b)   Second, since there are many other informations in the code logs 
		     we have extracted, for example the author and date, etc. Now we just wanted the 
		     comment tiles and the comment bodies only, so, we extracted the comment tiles 
		     and the comment titles plus bodies for each project. 
		
		     This is just to make the later calculation easier and cleaner. This step was 
		     done in WFpart2_storeTitlesAndBodies.ipynb
		
		c)   Next, we found out the English words that not in the corpus, then we went 
		     through the word list and did some manual replacement for the following cases:

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
		
		
		d)   After the manual replacement, we calculated the average word frequency rank 
		for both comment titles and comment titles plus bodies. The replaced words were 
		searched in the corpus.
		
		The calculation was done with the scripts WFpart4_wordFrequencyRankCalculation.ipynb




## **3.  Code Quality Metrics**
		
		We first wrote Python scripts to detect the instances of thrashing, then used an online tool, 
		CommitGuru (CG), to help to calculate the other three code quality metrics: average commit size, 
		percentage of risky commits, and distribution of modified code.
		
		To calculate metrics with CG, you must provide the Git repository URL. Then CG will start 
		processing the repository. When CG has finished processing a repository, a CSV file containing 
		all of the commits for the entire project life cycle and a set of CG metrics values for each 
		commit will be returned. 
		
		The CommitGuru tool is available on: http://commit.guru/
		
		Their papers have detailed descriptions on CG tool.
		
		[1] C. Rosen, B. Grawi, and E. Shihab, "Commit guru: analytics and risk prediction of software 
		commits. " In Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering, 
		New York, pp. 966-969. 2015.
		[2] Y. Kamei, E. Shihab, B. Adams, A. E. Hassan, A. Mockus, A. Sinha, and N. Ubayashi, 
		“A large-scale empirical study of Just-in-time quality assurance”, IEEE Transactions on 
		Software Engineering, vol. 39, no. 6, pp. 757-773, September 2019.


### **3.1  Thrashing Frequency**
		
		We first analyzed the patch output to create a diff output file for each project.
			- removed the unnecessary information
			- transformed all lines into a "canonical" form by removing tabs and spaces 
			- converted everything to lower case
		
		Purpose: making the diff file more clear and easier to analyze. 				
		This was done by using the script TF_cleaningPatch.ipynb
		
		
		Next, we analyzed the code diffs in a moving time window N, and considered the 
		following three cases as thrashing:
		
			a)	Line removed then added back within N successive commits;
			b)	Line added then removed within N successive commits;
			c)	Repeated modifications to the same region of code within N successive commits;
		
		For sub-metric a) and b), 
		
			- matched code lines removed in commit n against lines added in commit n+1 and lines added 
			in commit n against lines removed in commit n+1. 

			- matched code lines removed in commit n against lines added in commit n+2 and lines 
			added in commit n against lines removed in commit n+2. 

			- this would be the process if our window was three successive commits. 
			  The scripts are available in thrashingFrequencySubMetricab.ipynb, with N = 3.
		
		For sub-metric c), 
		
			- looked at the line number ranges in three successive commits (commit n, commit n+1, 
			  and commit n+2). If there is 50% overlap or more in these ranges, we say it is an 
			  evidence of sub-metric c).

			- the scripts are available in thrashingFrequencySubMetricc.ipynb, with N = 3.

		The three submetrics were calculated separately. We calculated normalized the trashing 
		metrics by calculating a ratio between the number of thrashing events and the 
		number of commits. A ceiling value of 1.0 was applied to the normalized sub-metric.
		
		We dropped the sub-metric c), because this measure had very little variability across projects.
		We combined sub-metrics a) and b) by averaging the normalized values, because the two 
		sub-metrics had almost exactly the same patterns of variation.
		
		We also calculated the larger windown sizes for sub-metrics a) and b), which are N=5, N=7.
		The scripts are shown in TF5.ipynb and TF7.ipynb. 
		
		There were not much different between the scripts, just need to change the N size in 
		the compare_adjacent_commit_list() function.
		
		


### **3.2  Average Commit Size**

		we acquired the corresponding metric values for all the commits that made within 
		our six months’ time frame from the CSV file returned by CG. We used three CG 
		metrics which reflect the size of a commit: 
		
			lines of code added (LA), 
			lines of code deleted (LD), 
			and the number of modified files (NF),
		
		These three measures were used as separate indicators of commit size. We calculated
		the mean values for each project as follows；

			SUM(LA) / (#total_commit); 
			SUM(LD) / (#total_commit); 
			SUM(NF) / (#total_commit);
			
		 The calculation was done by using the script code_averageCommitSize.ipynb



### **3.3  Percentage of Risky Commits**

		The final CG CSV file includes a ‘contains_bug’ column, which holds a value of 
		“True” or “False” for each commit of the project. “True” means the commit is 
		identified as risky, while “False” means the commit is non-risky. 
		
		We calculated the percentage of risky commits in a project by dividing the 
		number of risky commits by the total number of commits within our time range.
		
		The calculation was done by using the script code_percentageOfRiskyCommits.ipynb


### **3.4  Distribution of Modified Code**


		CG refers to this metric as entropy. In the CG CSV file, there is a ‘entropy’ column 
		which holds an entropy value for each commit of the project. We calculated the mean 
		value for each project as follows:
		
		SUM(entropy) / (#total_commit)
		
		The calculation was done by using the script code_entropy.ipynb
		
		




