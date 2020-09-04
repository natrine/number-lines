'''
	this is a tool to number lines for every 10 words for AP Lang.
	this program was made by natrine who cannot code so Lol.

	BEFORE USING, remove or replace non-ascii characters (ctrl + h or whatever you use to replace) with ascii characters (ex. turning ” into ", ’ into ')
	because the commands i use don't recognize some of them
'''

import math, os, pathlib

# put this program in the same folder as your txt file, then simply replace 'file' in the command below with your txt name (recommended)
# if not, copy the full path name and replace all \ in the path with / because python no likey \ in a path
# for example, 'C:\Users\Windows\projects\ap lang number lines\ass001.txt' becomes 'C:/Users/Windows/projects/ap lang number lines/ass001.txt'

filePath = pathlib.Path('file.txt')
myFile = open(filePath,'r')
data = ' ' + myFile.read() + ' '

'''
	if you want to remove enters, you can use the command below or do it yourself. each \n represents one enter, so add or delete them to your liking.

	this
	is one enter and you should use \n

	this

	is 2 enters and you should use \n\n

	this assumes that there aren't any space characters between your paragraphs. if there is, turn the " " into "".
'''
dataStrip = data.replace("\n", " ")

# if you aren't using the command above to remove enters, this is True. if you are using the command above to remove enters, replace True with False.
# capitalizing the first letter is required BTW
dataOriginal = True
if (not(dataOriginal)):
	data = dataStrip


newFile = open('lines_' + filePath.name, 'w')
character = ' '

indices = [i for i, a in enumerate(data) if a == character]
x = 0
line = 1

for m in indices:
	if (x % 10 == 0) and x > 0:
		newFile.write(str(line) + ') '  + data[indices[x-10] + 1:indices[x] + 1] + '\n')
		last = indices[x]
		line += 1
	x += 1
	if  x == len(indices) - 1:
		newFile.write(str(line) + ') ' + data[last + 1:indices[x]])