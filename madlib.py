import os, re

text = "The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

textFile = open('madlib.txt', 'w')
textFile.write(text)
textFile.close()

print('Enter an anjective:')
adjective = input()
print('Enter a noun:')
noun = input()
print('Enter a verb:')
verb = input()
print('Enter a noun:')
noun2 = input()



adjectiveRegex = re.compile('ADJECTIVE')
nounRegex = re.compile('NOUN')
verbRegex = re.compile('VERB')
noun2Regex = re.compile('NOUN')


textFile = open('madlib.txt', 'r')
content = textFile.read()
textFile.close()

fillAdjective = adjectiveRegex.sub(adjective, content)
textFile = open('madlib.txt', 'w')
textFile.write(fillAdjective)
textFile.close()

textFile = open('madlib.txt', 'r')
content = textFile.read()
textFile.close()

fillNoun = nounRegex.sub(noun, content, count = 1)
textFile = open('madlib.txt', 'w')
textFile.write(fillNoun)
textFile.close()

textFile = open('madlib.txt', 'r')
content = textFile.read()
textFile.close()

fillVerb = verbRegex.sub(verb, content)
textFile = open('madlib.txt', 'w')
textFile.write(fillVerb)
textFile.close()

textFile = open('madlib.txt', 'r')
content = textFile.read()
textFile.close()

fillNoun2 = noun2Regex.sub(noun2, content)
textFile = open('madlib.txt', 'w')
textFile.write(fillNoun2)
textFile.close()


textFile = open('madlib.txt', 'r')
content = textFile.read()
print(content)
textFile.close()

newTextFile = open('newmadlib.txt', 'w')
newTextFile.write(content)
newTextFile.close()




