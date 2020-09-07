"""
Sample Input

string  aefoaefcdaefcdaed

substring ="aefcdaed

 Sample Output

 true

Knuth-morris-pratt算法的工作原理是识别潜在子串中的模式，并利用它们来避免在搜索主字符串中的子串时进行不必要的字符比较。
例如，以字符串ababac为例，比较这些字符串的子字符串abac将在第四个字符处失败，其中“b”不等于“c”，而不必在主字符串的第二个字符处重新开始比较，
但是，我们注意到子字符串“ab”刚刚出现，它位于潜在子字符串的开头在主弦的失效点附近。我们如何利用这一优势？
The Knuth-morris-pratt algorithm works by identifying patterns  in the potential substring and exploiting them to avoid doing  needless character comparisons when searching for the substring  in the main string.
For instance, take the string ababac and the  substring abac comparing these strings will fail at the fourth  character, where"b"is not equal to"c Instead of having to restart  our comparisons at the second character of the main string,
 however, we notice that the substring"ab", Which is at the  beginning of our potential substring,
just appeared near our point  of failure in the main string. How can we use this to our advantage?

首先遍历潜在的子串并构建一个模式表。对于子串中的每一个位置，这个一维数组都应该存储一个匹配模式出现的最后一个索引；更具体地说，这个索引应该是子串中前缀的结束索引，该前缀也是给定位置的后缀。
例如，字符串“abcabacd”应生成以下模式表：[-1，-1，-1，0，1，0，1，2，-1]
Start by traversing the potential substring and building out a  pattern table. This 1-dimensional array should store, for every  position in the substring, the last index at which a matching pattern  has been seen; more specifically, this index should be the ending  index of a prefix in the substring that is also a suffix at the given  position. For example,
the string"abcababcd"should yield the  following pattern table:  [-1, -1, -1, 0, 1, 0, 1, 2, -1]

在建立了Hint*#2中提到的模式表之后，当字符匹配时，用两个单独的指针遍历主字符串和潜在子字符串，然后向前移动指针。当字符不匹配时，检查子字符串中的指针是否在子字符串的最开始；如果是，则不匹配，可以将主字符串的指针向前移动，直到有匹配为止；如果不匹配，然后将它移到模式表中存储在前一个ndex中的最后一个看到的模式之后的位置
After the pattern table mentioned in Hint *#2 has been built,  traverse the main string and the potential substring with two  separate pointers When characters match, move the pointers  forward. When characters dont match, check if the pointer in the  substring is at the very beginning of the substring; if it is, then there  is no match and you can move the pointer of the main string  forward until there is a match; if it isnt, then move it to the position  that comes right after the last seen pattern stored at the previous  ndex in the pattern table

O（n+m）时间O（m）空间，其中n是主串的长度，m是潜在子串的长度
O (n +m) time O (m) Space-where n is the length of the main  string and m is the length of the potential substring
"""

#O (n +m) time O (m) Space-where n is the length of the main  string and m is the length of the potential substring
def knuthMorrisPrattAlgorithm(string, substring):
	pattern = buildPattern(substring)
	return doesMatch(string, substring, pattern)

def buildPattern(substring):
	pattern = [-1 for i in substring]
	j = 0
	i = 1
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return pattern

def doesMatch(string, substring, pattern):
	i = 0
	j = 0
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) - 1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j - 1] + 1
		else:
			i += 1
	return False