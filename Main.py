import hashlib

hash1, salt1, fileName, fileText = "", "", "password_file.txt", ""
lineCount = 0

def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def letsPlay(n):
    if n == lineCount:
        print("Job completed!")
        return
    else:
        words = fileText[n].split(',') # split current line to words
        hash1, salt1 = words[2].replace(' ', ''), words[1].replace(' ', '') # remove spaces
        print("Trying->", words[0], end='') #keep printing in the same line print("Hello", end = '') print("world")
        i, stop, zeros = 0, 9999999, 3 # increment, where to stop, number of zeros
        while i < stop:
            x = '{:d}'.format(i).zfill(zeros)
            hex_dig = hash_with_sha256(x.replace(' ', '') + salt1)
            if hex_dig.lower().split() == hash1.lower().split():
                print(" # Password Cracked!!!\n",
                      words[0], ",password:", '{:d}'.format(i).zfill(zeros), ",salt:", salt1, "\nhash:", hex_dig,
                      "\n###############################################################################")
                break
            i += 1
            if i == 1000 and zeros == 3:
                # print("Ending 3 digit combinations - Restarting with 4")
                print(".", end='') # keep printing dots in 1 line
                i = 0
                zeros += 1  # increase number of zeros
            if i == 10000 and zeros == 4: # print("Ending 4 digit combinations - Restarting with 5")
                print(".", end='')
                i = 0
                zeros += 1  # increase number of zeros
            if i == 100000 and zeros == 5: # print("Ending 5 digit combinations - Restarting with 6")
                print(".", end='')
                i = 0
                zeros += 1  # increase number of zeros
            if i == 1000000 and zeros == 6: # print("Ending 6 digit combinations - Restarting with 7")
                print(".", end='')
                i = 0
                zeros += 1  # increase number of zeros
            if i == 10000000 and zeros == 7:
                print(".", end='')
                i, stop, zeros = 0, 9999999, 3  # reset for next loop
                break
        return letsPlay(n + 1)

with open(fileName, "r") as f: # getting file content
    fileText = f.readlines()

for line in fileText: # getting line count
    lineCount += 1

letsPlay(0) # start from line 0, minimum password length 3, max length 7
