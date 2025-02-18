import os, re

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

textFile = open('madlib.txt', 'w')
textFile.write(text)
textFile.close()

print('Enter an anjective:')
adjective = str(input())
print('Enter a noun:')
noun = input()
print('Enter a verb:')
verb = input()
print('Enter a noun:')
noun2 = input()

textFile = open('madlib.txt', 'r')
content = textFile.read()



madlibRegex = re.compile(r'ADJECTIVE \w+')
madlibRegex.sub(adjective, content)
print(content)



textFile.close()




