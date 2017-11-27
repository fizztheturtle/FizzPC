# This is a modified version of the Affine Cipher SUBSTITUTION CIPHER from:
# http://inventwithpython.com/hacking (BSD Licensed)
# THIS CODE REQUIRES PYTHON 3 AND ABOVE TO FUNCTION
import sys, cryptomath, random

# SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""  # note the space at the front
SYMBOLS=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 0:
        sys.exit('The affine cipher becomes incredibly weak when key A is set to   Choose a different key.')
    if keyB == 0 and mode == 0:
        sys.exit('The affine cipher becomes incredibly weak when key B is set to     Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB
# If affineCipher.py is run (instead of imported as a module) call
# the main() function.


def affineTranslate(message, key, mode):

    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, mode)
    translatedMessage = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if mode == 0:
            # encrypt this symbol
            if symbol in SYMBOLS:
                symIndex = SYMBOLS.find(symbol)
                translatedMessage += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
            else:
                translatedMessage += symbol  # just append this symbol unencrypted
        elif mode == 1:
            if symbol in SYMBOLS:
                # decrypt this symbol
                symIndex = SYMBOLS.find(symbol)
                translatedMessage += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
            else:
                translatedMessage += symbol  # just append this symbol undecrypted
    return translatedMessage
# def encryptMessage(key, message):
#     keyA, keyB = getKeyParts(key)
#     checkKeys(keyA, keyB, 'encrypt')
#     ciphertext = ''
#     for symbol in message:
#         if symbol in SYMBOLS:
#             # encrypt this symbol
#             symIndex = SYMBOLS.find(symbol)
#             ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
#     else:
#         ciphertext += symbol  # just append this symbol unencrypted
#         return ciphertext
#
#
# def decryptMessage(key, message):
#     keyA, keyB = getKeyParts(key)
#     checkKeys(keyA, keyB, 'decrypt')
#
#     plaintext = ''
#     modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
#     for symbol in message:
#         if symbol in SYMBOLS:
#             # decrypt this symbol
#             symIndex = SYMBOLS.find(symbol)
#             plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
#         else:
#             plaintext += symbol  # just append this symbol undecrypted
#             return plaintext

# def main():
#     myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
#     myKey = getRandomKey()
#     myMode = 'encrypt'  # set to 'encrypt' or 'decrypt'
#
#     if myMode == 'encrypt':
#         translated = encryptMessage(myKey, myMessage)
#     elif myMode == 'decrypt':
#         translated = decryptMessage(myKey, myMessage)
#     print('Key: %s' % (myKey))
#     print('%sed text:' % (myMode.title()))
#     print(translated)
#
#     print('Full %sed text copied to clipboard.' % (myMode))
