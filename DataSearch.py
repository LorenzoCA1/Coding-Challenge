import re

def SearchPlaintiffs(processedText):
	plaintiffs = []
	without_empty_strings = []
	plaintiffsearch =[re.compile('.*\w@@ @@(.+)(@@ @@)+Plaintiff'),re.compile('@@ @@+Plaintiff (\w* \w*)')]
	for string in plaintiffsearch:
		match = string.search(processedText)
		if match:
			plaintiffs.append(match.group(1).replace("@@ @@", ''))

	for string in plaintiffs:
		if (string != ""):
			without_empty_strings.append(string)

	return without_empty_strings[0]


def SearchDefendants(processedText):
	defendants = []
	without_empty_strings = []
	defendantsearch = [re.compile('vs.@@ @@(.*)Defendants'), re.compile('@@ @@v(.*) @@Defendants')]
	for string in defendantsearch:
		match = string.search(processedText)
		if match:
			defendants.append(match.group(1).replace("@@ @@", ''))

	for string in defendants:
		if (string != ""):
			without_empty_strings.append(string)


	return without_empty_strings[0]