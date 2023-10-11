import random
#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
awkwardNumber1=chr(random.randint(48,57))
awkwardNumber2=chr(random.randint(48,57))
awkwardCharacter1=chr(random.randint(33,47))
awkwardCharacter2=chr(random.randint(58,64))
awkwardCharacter3=chr(random.randint(91,96))
awkwardCharacter4=chr(random.randint(123,191))
#Generate more characters here
#....
#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + awkwardNumber1 + awkwardNumber2 + awkwardCharacter1 +awkwardCharacter2 + awkwardCharacter3 + awkwardCharacter4
password = shuffle(password)
#Ouput
print(password)
