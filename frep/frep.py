"""
class FileReplacer
	.rep ()
		@param filename - name of file to operate on
		@param str - string to find and replace with 'rep'
		@param rep - string to replace 'str' in file text
		
	Usage:
		python frep.py <filename> <find> <replace>
"""
class FileReplacer:
	def rep (filename, str, rep):
		with open(filename, 'r') as file:
			text = file.read()
		with open(filename, 'w+') as file:	
			file.write(text.replace(str, rep))

if (__name__ == '__main__'):
	import sys
	fileName = sys.argv[1]
	searchFor = sys.argv[2]
	replaceWith = sys.argv[3]
	FileReplacer.rep(fileName, searchFor, replaceWith)