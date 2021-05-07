import os
import time
import sys
import subprocess

'''

PROGRAM USAGE:
~~~~~~~~~~~~~

python xzfiles.py <FILENAME>

This program searches all subdirectories for the specified filename, then compresses them individually. Use this program to compress text files (like .lammpstrj) for best results.

'''

def compress(filePaths, cwd):

	for dirs, file in filePaths.items():
		os.chdir (dirs)
		print (dirs)

		for x in range (0, len (file), 1):
			subprocess.run (["xz", file[x], "-v"])

		os.chdir (cwd)
		print ("\n")


def getPaths():

	fileContains = str (sys.argv[1])
	filePaths = {}

	for dirs, dirname, files in os.walk("."):


		for file in files:
			if fileContains in file and ".xz" not in file:

				filePath = dirs + "/" + file

				if dirs in filePaths:
					filePaths[dirs].append (file)

				else:
					filePaths[dirs] = []
					filePaths[dirs].append (file)
	
	return (filePaths)


if __name__ == '__main__':
	cwd = os.getcwd()
	filePaths = getPaths()
	# print (filePaths)
	compress (filePaths, cwd)
