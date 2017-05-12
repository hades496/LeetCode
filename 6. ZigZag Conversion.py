#!/usr/bin/python
#coding=UTF-8

class Solution(object):
    def convert(self, s, numRows):
		j=0
		n=numRows;
		if n==1: return(s)
		res=['']
		while j<len(s):
			res.append(s[j])
			j+=2*n-2
		for i in range(1,numRows-1):
			j=i
			while j<len(s):
				res.append(s[j])
				if j+2*n-2*i-2<len(s):
					res.append(s[j+2*n-2*i-2])
				j+=2*n-2
		j=n-1
		while j<len(s):
			res.append(s[j])
			j+=2*n-2
		return(''.join(res))
