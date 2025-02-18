import re, pyperclip

urlRegex = re.compile('''(
    ^([a-z]+:// | [a-z]+://\.)
    
)''', re.VERBOSE)

txt = str(pyperclip.paste())

for urls in urlRegex.findall(txt):
                             
