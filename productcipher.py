
# THIS CODE REQUIRES PYTHON 3 OR ABOVE TO FUNCTION
import os


import sys
import time
import cryptomath
import random

from TranspositionCipher import *
from caesarCipher2 import *
from testingEncryption import *


def main():

        inputFilename = 'fizz.txt'
        outputFilename = 'fizz.encrypted.txt'
        decryptedFileName = 'fizz.decrypted.txt'
        mode = 1
        mykey =4190
        key = int(str(mykey)[:2])
        # print(desktop)
        print(mykey)
        print(inputFilename)
        print(outputFilename)

        # If the input file does not exist, then the program terminates early.
        if not os.path.exists(inputFilename):
            print('The file %s does not exist. Quitting...' % inputFilename)
            sys.exit()





            # Read in the message from the input file


        print('%sing...' % (myMode(mode)))

        # Measure how long the encryption/decryption takes.

        if mode == 0:
            fileObj = open(inputFilename)
            content = fileObj.read()
            fileObj.close()
            if os.path.exists(outputFilename):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()

            startTime = time.time()
            Text = transpositiontranslate(content, key, mode)
            # print('Output from transposition Cipher\t%s' % Text)
            Text1 = affineTranslate(Text, mykey, mode)
            # print('Output from affine Cipher\t%s' % Text1)
            Text2 = caesarTranslate(Text1, key, mode)
            print('Output from Caesar Cipher\t%s' % Text2)
            # Write out the translated message to the output file.
            outputFileObj = open(outputFilename, 'w')
            outputFileObj.write(Text2)
            outputFileObj.close()
            print('Done %sing %s (%s characters).' % (myMode(mode), inputFilename, len(content)))
            print('%sed file is %s.' % (myMode(mode), outputFilename))

        elif mode == 1:
            fileObj = open(outputFilename)
            content = fileObj.read()
            fileObj.close()
            if os.path.exists(decryptedFileName):
                print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (decryptedFileName))
                response = input('> ')
                if not response.lower().startswith('c'):
                    sys.exit()
            startTime = time.time()
            Text = caesarTranslate(content, key, mode)
            # print ('Output from transposition Cipher\t%s' %Text)
            Text1 = affineTranslate(Text, mykey, mode)
            # print ('Output from affine Cipher\t%s'%Text1)
            Text2 = transpositiontranslate(Text1, key, mode)
            print ('Output from Caesar Cipher\t%s'%Text2)
            outputFileObj = open(decryptedFileName, 'w')
            outputFileObj.write(Text2)
            outputFileObj.close()
            print('Done %sing %s (%s characters).' % (myMode(mode), outputFilename, len(content)))
            print('%sed file is %s.' % (myMode(mode), decryptedFileName))


        totalTime = round(time.time() - startTime, 2)
        print('%sion time: %s seconds' % (myMode(mode), totalTime))








# raw_input('input operation mode - encrypted = 0 / decrypted = 1:




# # # #this is A test7
# c = caesarTranslate(msg, key, mode)
# print ('Output from transposition Cipher\t%s' %c)
# c1 = affineTranslate(c, mykey, mode)
# print ('Output from affine Cipher\t%s'%c1)
# c2 = transpositiontranslate(c1, key, mode)
# print ('Output from Caesar Cipher\t%s'%c2)

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

def myMode(x):
    if x == 0:
        return 'Encrypt'
    elif x == 1:
        return 'Decrypt'

# 5671
# Output from Caesar Cipher	pks}kv
# Output from affine Cipher	qjbpjT
# Output from transposition Cipher	qjbpjT




if __name__ == '__main__':
    main()





            # # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        # directory = os.fsencode('D:\\Desktop')
        #
        # for file in os.listdir(directory):
        #     filename = os.fsdecode(file)
        #     if filename.endswith(".txt"):
        #         print(os.path.join(directory, filename))
        #         continue
        #     else:
        #         break

        #take input from the user: msg, key mode
        # msg = 'faisal here sqaaaaaaad hjfcyytufyv'        #raw_input('input a sentence to encrypt: ')
        # key = 10 #raw_input('input key: ') Has to be greater that 9 to work
        # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')