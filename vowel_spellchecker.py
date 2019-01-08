import sys

# https://leetcode.com/problems/vowel-spellchecker/

def spellchecker(wordlist, queries):
	"""
	:type wordlist: List[str]
	:type queries: List[str]
	:rtype: List[str]
	"""
	vowelList = ['a', 'e', 'i', 'o', 'u']
	wd = dict()
	lowerWd = dict()
	noVowelWd = dict()
	for word in wordlist:
		wd[word] = ''
		key = word.lower()
		if key in lowerWd:
			continue
		lowerWd[key] = word
		for vowel in vowelList:
			key = key.replace(vowel, '*')
		if key in noVowelWd:
			continue
		noVowelWd[key] = word
	# print('wd: ', wd)
	# print('lowerWd: ', lowerWd)
	# print('noVowelWd: ', noVowelWd)

	for i in range(len(queries)):
		query = queries[i]
		if query in wd:
			continue
		queryLower = query.lower()
		if queryLower in lowerWd:
			queries[i] = lowerWd[queryLower]
			continue
		queryNoVowel = queryLower
		for vowel in vowelList:
			queryNoVowel = queryNoVowel.replace(vowel, '*')
		if queryNoVowel in noVowelWd:
			queries[i] = noVowelWd[queryNoVowel]
			continue
		queries[i] = ''
	return queries


def main():
	wordlist = input('wordlist: ').split(',')
	queries = input('queries: ').split(',')
	output = spellchecker(wordlist, queries)
	print('output: ', output)


if __name__ == '__main__':
    main()