import string
import random

def encrypttext(text, keyv, characters = string.ascii_lowercase):
    
    #keyv = keyv[:-1]
    keyarr = [int(x) for x in keyv.split()]
    #keyarr = list(map(int, keyv.split(" ")))
    arr = list(text)
    print(arr)
    print(keyarr)
        
    for i in range(len(text)):
        arr[i] = ord(arr[i]) + keyarr[i] 
        #print(arr[i])
        if arr[i] > 122:
            arr[i] = arr[i] - 26
        arr[i] = chr(arr[i])
        #print(arr[i],ord(arr[i]))
        
    str1 = ""
    translated_text = str1.join(arr) 
    
    return translated_text


def decrypttext(text, keyv, characters = string.ascii_lowercase):

    #keyarr = list(map(int, keyv.split(" ")))
    keyarr = [int(x) for x in keyv.split()]
    arr = list(text)
        
    for i in range(len(text)):

        arr[i] = ord(arr[i]) - keyarr[i]
        if arr[i] < 97:
            arr[i] = arr[i] + 26
        arr[i] = chr(arr[i])
            
    str1 = ""

    translated_text = str1.join(arr) 
    
    return translated_text


def fileCipher(fileName, outputFileName, key , crypt):

    with open(key, "r") as f_in:

        keyv = f_in.readline()

    with open(fileName, "r") as f_in:

        with open(outputFileName, "w") as f_out:

            # iterate over each line in input file
            for line in f_in:
                
                if(crypt == "encrypt"):
                    #encrypt/decrypt the line
                    lineNew = encrypttext(line, keyv)
                    print(lineNew)
                    f_out.write(lineNew)
                else:
                    f_out.write(line)
                    f_out.write("\n")
                    lineNew = decrypttext(line, keyv)
                    print(lineNew)
                    f_out.write(lineNew)
                    
                
                    
    print("The file {} has been translated successfully and saved to {}".format(fileName, outputFileName))


def key_Generation(fileName, key):

    with open(fileName, "r") as f_in:
        data = f_in.read()
        leng = len(data) 
        
    
    y =''
    
    for i in range(leng):

        x = random.randint(1,26)
        y = y + str(x) + ' '


    with open(key, "w") as f_out:

        f_out.write(y) 
  

            
            
    
    

inputFile = "./plaintext1.txt"

outputFile = "./plaintext1_encrypted.txt"

key = "./key.txt"



key_Generation(inputFile, key)

fileCipher(inputFile, outputFile, key,"encrypt")

inputFile = "./plaintext1_encrypted.txt"

outputFile = "./output.txt"

fileCipher(inputFile, outputFile, key,"decrypt")

#Cryptanalytics(inputFile)
