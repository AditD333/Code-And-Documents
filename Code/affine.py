#Import cryptomath and sys module
import cryptomath,sys

Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getKeyParts(key):
	keyA = key // len(Letters) # KeyA is determined by the user defined key, floor-divided by number of characters presented in Letters
	keyB = key % len(Letters) # KeyB is determined by user defined key, then get the remainder when dividing by number of characters in Letters
	return(keyA, keyB)

def checkKeys(keyA,keyB,mode):
	if keyA == 1 and mode == "encrypt": # If we want to have encryption process but the keyA value is 1, so it returns an error and exit the program
		sys.exit("Cipher is weak if key A is 1. Choose a different key!")
	if keyB == 0 and mode == "encrypt":  # If we want to have encryption process but the keyB value is 0, so it returns an error and exit the program
		sys.exit("Cipher is weak if key B is 0. Choose a different key!")
	if keyA < 0 or keyB < 0 or keyB > len(Letters) - 1: # If either KeyA or KeyB is less than 0, keyB value is same as the number of characters in Letters or more, return an error and exit the program
		sys.exit("Key A must be greater than 0 and key B must between 0 and %s" % (len(Letters) - 1))
	if cryptomath.gcd(keyA, len(Letters)) != 1: # If the GCD of KeyA and the number of characters in Letters is not 1, then return the error and exit the program
		sys.exit("Key A (%s) and symbol set size (%s) are not relatively prime. Choose a different key!" %(keyA, len(Letters)))

def encrypt(key,message):
	keyA, keyB = getKeyParts(key) # The keyA and keyB from the module getKeyParts imported here.
	checkKeys(keyA,keyB,"encrypt") # Execute validation from checkKeys module
	ciphertext = '' # Cipher text default is set to empty

	for symbol in message: # Encrypting the message
		if symbol in Letters:
			symbolIndex = Letters.find(symbol)
			ciphertext += Letters[(symbolIndex * keyA + keyB) % len(Letters)]
		else:
			ciphertext += symbol

	return ciphertext

def decrypt(key,message):
	keyA, keyB = getKeyParts(key) # The keyA and keyB from the module getKeyParts imported here.
	checkKeys(keyA,keyB,"encrypt") # Execute validation from checkKeys module
	plaintext = '' # Plain text default is set to empty
	modInverseKeyA = cryptomath.findModInverse(keyA, len(Letters)) # Finding modular inverse to do decryption

	for symbol in message: # Decrypting the message
		if symbol in Letters:
			symbolIndex = Letters.find(symbol)
			plaintext += Letters[(symbolIndex - keyB) * modInverseKeyA % len(Letters)]
		else:
			plaintext += symbol
	return plaintext



def main():

	#msg = "\"Encryption works. Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.\"— Edward Snowden"
	msg = "AFFINE CIPHER"
	Key = 187
	print('Key %s' % (Key))
	keyA = Key // len(Letters) # KeyA is determined by the user defined key, floor-divided by number of characters presented in Letters
	keyB = Key % len(Letters) # KeyB is determined by user defined key, then get the remainder when dividing by number of characters in Letters
	modInverseKeyA = cryptomath.findModInverse(keyA, len(Letters)) # Call the function findModInverse from cryptomath module to calculate the modulo inverse of keyA and number of characters in Letters
	print("\n")
	print("Affine Key-A:",keyA)
	print("Affine Key-B:",keyB)
	print("Affine Mod-Inverse key-A:",modInverseKeyA)
	print("\n")
	translated = encrypt(Key,msg)
	print("Affine ciphertext:")
	print(translated) # Get the encrypted text
	
	print("\n")
	translated2 = decrypt(Key,translated)
	print("Affine plaintext:")
	print(translated2) # Get the decrypted text
	



# If there is a main function then main function will be executed first
if __name__ == '__main__':
	main()