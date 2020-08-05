
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def main():
	msg = "\"Encryption works. Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.\"— Edward Snowden"

	Key = input("Enter Vigenere Key -> ") # Input vigenere key
	print("Vigenere Key:",Key)
	translated = encrypt(Key,msg)
	translated2 = decrypt(Key,translated)
	# Get the encrypted message and decrypted message using the same key at the same time 
	print("\nVigenere ciphertext:")
	print (translated)
	print("\nVigenere plaintext:")
	print (translated2)
	

def encrypt(key,message):
	return translate(key,message,"encrypt")
def decrypt(key,message):
	return translate(key,message,"decrypt")
def translate(key,message,mode):
	translated = []

	keyIndex = 0 # First index is set to be 0
	key = key.upper() # All the characters are switched to upper-case

	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			if mode == 'encrypt':
				num += LETTERS.find(key[keyIndex])
			elif mode == 'decrypt':
				num -= LETTERS.find(key[keyIndex])

			num %= len(LETTERS)

			if symbol.isupper():
				translated.append(LETTERS[num].upper())
			elif symbol.islower():
				translated.append(LETTERS[num].lower())
			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0

		else:
			translated.append(symbol)

	return ''.join(translated)




if __name__ == '__main__':
	main()