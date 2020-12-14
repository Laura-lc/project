# Documentation

1.	Data
We used git clone to clone the GitHub projects and extracted commit comments (both tittles and bodies) from GitHub using following script:

git log --after="2020-02-20" --before="2020-08-20" --pretty=format:"CommitHash: %H AuthorDate: %ai CommitterDate: %ci SubjectTitleLine: %s BodyMessage: %b" > fullCommitMessages.txt

