# Import the secrets module
import secrets

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def generateotp(message):
	otp = '' # The One Time Pad cipher result default is set to empty
	for i in range(len(message)): # Encrypting the message using random key
		otp += secrets.choice(LETTERS)
	# Return the key for other operations
	print("\nOne Time Pad Key:")
	print(otp)
	print("\n")
	return otp
def main():
	msg = "ONE TIME PAD"
	#msg = "\"Encryption works. Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.\"— Edward Snowden"
	key = generateotp(msg) # Call the generateotp function
	translated = encrypt(key,msg) # Encryption process
	translated2 = decrypt(key,translated) # Decryption process
	
	# Get the encrypted and decrypted message at the same time
	print("One Time Pad ciphertext:")
	print (translated)
	print("\n")
	print("One Time Pad plaintext:")
	print(translated2)

def encrypt(key,message):
	return translateMessage(key,message,"encrypt")
def decrypt(key,message):
	return translateMessage(key,message,"decrypt")

def translateMessage(key, message, mode):
	translated = []

	keyIndex = 0 # First character is indexed as 0
	key = key.upper() # All the characters are switched to upper-case

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			if mode == "encrypt":
				num += LETTERS.find(key[keyIndex])
			elif mode == "decrypt":
				num -= LETTERS.find(key[keyIndex])

			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num].upper())
			elif symbol.islower():
				translated.append(LETTERS[num].lower())

			keyIndex +=1
			if keyIndex == len(key):
				keyIndex = 0

		else:
			translated.append(symbol)
	return ''.join(translated)





if __name__ == '__main__':
	main()