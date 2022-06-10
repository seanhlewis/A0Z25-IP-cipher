ip = ""
code = ""

#A0Z25 CIPHER
ip_dict = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L",
12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S",
19: "T", 20: "U", 21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z"}

dot_dict = {"A": [3,3,3], "B": [3,3,2], "C": [3,3,1], "D": [3,2,3],
"E": [3,2,2], "F": [3,2,1], "G": [3,1,3], "H": [3,1,2], "I": [3,1,1],
"J": [2,3,3], "K": [2,3,2], "L": [2,3,1], "M": [2,2,3], "N": [2,2,2],
"O": [2,2,1], "P": [2,1,3], "Q": [2,1,2], "R": [2,1,1], "S": [1,3,3],
"T": [1,3,2], "U": [1,3,1], "V": [1,2,3], "W": [1,2,2], "X": [1,2,1],
"Y": [1,1,3], "Z": [1,1,2]}

def encrypt(ip_address):
	#HEADER
	new_ip = ip_address.split(".")
	#print(new_ip)
	dvalue = [len(new_ip[0]), len(new_ip[1]), len(new_ip[2])]
	header = ""
	for i in dot_dict:
		if dvalue == dot_dict.get(i):
			header = i 
			break
	#print(header)
	#BODY
	new_ip = ip_address.replace(".", "")
	encode_wip = new_ip
	#print(new_ip)
	#eliminate doubles first
	for i in range(len(new_ip) - 1):
		two = str(new_ip[i]) + str(new_ip[i+1])
		for j in ip_dict:
			if str(j) == two:
				encode_wip = encode_wip.replace(two, ip_dict.get(j))
				#print(ip_dict.get(j))
				#print("MATCHED")
		#print(encode_wip)
	#then singles
	for i in range(len(encode_wip)):
		one = str(encode_wip[i])
		for j in ip_dict:
			if str(j) == one:
				encode_wip = encode_wip.replace(one, ip_dict.get(j))
				#print(ip_dict.get(j))
				#print("MATCHED")
		#print(encode_wip)
	encoded = str(header) + str(encode_wip)
	return encoded
	
def decrypt(code):
	#BODY
	wcode = code
	code_wip = code
	wcode = wcode[1:]
	code_wip = code_wip[1:]
	#print(wcode)
	for i in wcode:
		for j in ip_dict:
			if i == ip_dict[j]:
				code_wip = code_wip.replace(i, str(j))
	#print(code_wip)
	#HEADER
	header = code[0]
	dvalue = ""
	for i in dot_dict:
		if str(header) == i:
			dvalue = dot_dict.get(i)
			#print(dvalue)
			break
	curval = 0
	for i in range(3):
		code_wip = code_wip[:curval + dvalue[i]] + '.' + code_wip[curval + dvalue[i]:]
		curval += int(dvalue[i] + 1)
	return code_wip

def back2main():
    print("\n\n\n\n\n\n\n\n")
    main()

def encryptme():
    encryption = "ABCDEFG"
    while encryption != "":
        try:
            print(encrypt(input("Enter an IP address to encrypt:\n")))
        except:
            break
    back2main()
    

def decryptme():
    decryption = "1.1.1.1"
    while decryption != "":
        try:
            print(decrypt(input("Enter an A0Z25 cipher to decrypt:\n")))
        except:
            break
    back2main()

def main():
    choice = "selection"
    while choice != "":
        choice = input("Enter the number of program to run\n[1] IP Address to A0Z25 cipher\n[2] A0Z25 cipher to IP Address\n")
        options = {1 : encryptme, 2 : decryptme}
        try:
            options[int(choice)]()
        except:
            print("Please enter a valid number")
            continue
main()