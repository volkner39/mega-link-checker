import requests
import sys

# [-11] link exists

# [-9] or [-16] = The folder link you are trying to access is no longer available.
# THis could be due to the following reasons:
# The folder link has been removed because of a ToS/AUP violation
# Invalid URL - the link you are trying to access does not exist
# The folder link has been disabled by the user
		
# [-6] This folder/file was reported to contain objectionable content.

# OR

# The link is unavailable as the user's account has been closed for gross violation of MEGA's Terms of Service.

# Types of links:
# https://mega.nz/file/1yhgTSpD%22%22
# https://mega.nz/#F!ABcD1E2F!gHiJ23k-LMok45PqrSTUvw
# https://mega.nz/#!nUJwkIaA!OcSUiyCG8_Iimr5iqQ_GQZJDEPg3Tzz32U0b-V-6-tY
# https://mega.nz/file/Wbgh0QwS#qXTOLJdBgV9hMLQNOldsAOfqTq6yvJywPBWjqgUQJsU
# https://mega.nz/folder/HlFU3C6C#ZKZaLG1PMgiIjS5U3KljDg
# https://mega.nz/folder/TUUiHAgZ#Zce-2IEts3TiCVg_SCVsqQ/folder/PRU2kCbJ
# https://mega.nz/#F!Q6QFVKSQ!FalLuue3wOJJoRUny8KTfA!I2RgDAgb

def check(id):

	url = 'https://eu.api.mega.co.nz/cs'

	# data to send
	v1 = '[{"a":"g", "g":1, "ssl":0, "p": "' + id + '"}]'

	# post request
	resp = requests.post('https://eu.api.mega.co.nz/cs', data=v1)
	
	# print the status
	if (resp.text == '[-6]' or resp.text == '[-9]' or resp.text == '[-16]'):
		print(resp.text + ":  offline\n")
		return 1
	elif (resp.text == '[-11]'):
		print(resp.text + ":  online\n")
		return 0
	else:
		print("Not recognized status code\n")
		return 0


if __name__ == "__main__":

	to_keep = []
	
	if sys.argv[1] == "-d":
		file = sys.argv[2]
	else:
		file = sys.argv[1]
	
	# read file and compile links into list
	f = open(file, "r")
	list1 = f.read().splitlines()
	
	for link in list1:
	
		if link != "":
			# check if link has atleast two '!'
			if (link.count('!') >= 2):
				id = link.split('!')[1]
			else:
				# find the location of the hash
				hash_location = link.find("#")
		
				# remove irrelevant chars
				stripped1 = link.split('#', 1)[0]
				id = stripped1.split("/")[-1]
		
			print(id)
		
			# check it and keep track of ones that are online
			if (check(id) != 1):
				to_keep.append(link)
	
	f.close()
	
	# start deleting offline links (if -d is given) in the original text file
	if (sys.argv[1] == "-d"):
		with open(file, "w+") as f1:
			for x in sorted(to_keep):
				f1.write(x + '\n')
			f1.close()
