Empirical logic to find summary
Split the sentence and find the top 3 sentences with mx no. of words among the rest

Document Summarisation
	-preprocessor.py
		Class ProcessDoc
			functions
			-special char
			-token
			-stopword removal
	-summariser.py
		Class SummarizeDoc
		functions
			-readDocs
			-loadConfig
			-splitter
			-firstSentExtractor
			-findNumWords
			-findTop3Sent
			-sentenceCombiner
			