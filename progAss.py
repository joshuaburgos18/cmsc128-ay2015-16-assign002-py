#Mark Joshua B. Burgos
#AB-7L
#2013-09836

'''
	This function accepts 2 string and compare each character in the first string
	to the character in the second string with same index. A counter is initialized
	to the length of the first string. First, length of the two strings will be 
	checked. This only consider same length strings. When a same character is found, 
	the counter declared will be decremented. 
	Thus, when not equal length strings are given, an error prompt will be returned
'''
def getHammingDistance(str1, str2):
    sameChar = len(str1)
    i = -1
    if len(str1) == len(str2):
        for letter in str1:
            i = i + 1
            if letter == str2[i]:
                sameChar = sameChar - 1
        return sameChar    
    else:    
        return "Error! Strings are not equal!"

'''
	This function accepts 2 strings. One is the original string. The other one is the
	pattern string. It will find a pattern string from the original string while cutting 
	the string (removing the first character) until it reaches the length of the pattern.
	It returns the number of patterns
'''

def countSubstrPattern(original, pattern):
	occur = 0
	start = 0
	end = len(pattern)
	if len(original) > len(pattern):
		while(end <= len(original)):
			if original[start:end] == pattern:
				occur = occur + 1 
			start = start + 1
			end = end + 1	
	return occur

'''
	This function accepts 2 string. One is for the original string and the other one is
	for the alphabet. The original string will be traversed and checks if all characters
	are present in the given alphabet. If a character is not found in the alphabet, it
	returns false. If all characters are traversed and all are part of the given alphabet,
	it will return True
'''

def isValidString(str, alphabet):
	for letter in alphabet:
	    if alphabet.count(letter) > 1:
	        return False
	        
	for letter in str:
		if alphabet.find(letter, 0) < 0:
			return False

	return True	

'''
	This function accepts a string and an integer. The integer will dictate the ending 
	point of the traversal. All Gs and Cs will be counted. It will return the difference
	of total G count and total C count in a given ending point respectively. Hence, if 
	the given integer is invalid, it returns an error prompt
'''

def getSkew(str, n):
	gCount = 0
	cCount = 0
	i = 0
	if n > 0 and n <= len(str):
		while(i < n):
			if str[i] == 'G':
				gCount = gCount + 1
			elif str[i] == 'C':
				cCount = cCount + 1	
			i = i + 1	
		return gCount - cCount		
	elif n <= 0 or n > len(str):
		return "Invalid given Length!"

'''
	This function accepts a string and an integer. G count and C count will be recorded and 
	their difference will be computed per iteration. The function iterates n number of times.
	Every difference will be compared and the maximum value will be returned. Hence, if the 
	given integer is invalid, it returns an error prompt
'''

def getMaxSkewN(str, n):
	gCount = 0
	cCount = 0
	temp = 0
	i = 0
	if n > 0 and n <= len(str):
		while(i < n):
			if str[i] == 'G':
				gCount = gCount + 1
			elif str[i] == 'C':
				cCount = cCount + 1	
			if temp < gCount - cCount:
				temp = 	gCount - cCount
			i = i + 1	
		return temp		
	elif n <= 0 or n > len(str):
		return "Invalid given Length!"

'''
	This function accepts a string and an integer. G count and C count will be recorded and 
	their difference will be computed per iteration. The function iterates n number of times.
	Every difference will be compared and the minimum value will be returned. Hence, if the 
	given integer is invalid, it returns an error prompt
'''

def getMinSkewN(str, n):
	gCount = 0
	cCount = 0
	temp = 1
	i = 0
	if n > 0 and n <= len(str):
		while(i < n):
			if str[i] == 'G':
				gCount = gCount + 1
			elif str[i] == 'C':
				cCount = cCount + 1	
			if temp > gCount - cCount:
				temp = 	gCount - cCount
			i = i + 1	
		return temp		
	elif n <= 0 or n > len(str):
		return "Invalid given Length!"
