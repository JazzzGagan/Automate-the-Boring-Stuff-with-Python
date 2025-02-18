Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import os
myFiles = ['account.txt', 'data.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

    
C:\Users\asweigart/account.txt
C:\Users\asweigart/data.csv
C:\Users\asweigart/invite.docx
os.getcdw()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    os.getcdw()
AttributeError: module 'os' has no attribute 'getcdw'. Did you mean: 'getcwd'?
os.getcwd()
'/Users/jazzgagan/Documents'
os.chdir('/Users/jazzgagan/Desktop/python')
os.getcwd()
'/Users/jazzgagan/Desktop/python'
os.chdir('/This folder does not exit')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.chdir('/This folder does not exit')
FileNotFoundError: [Errno 2] No such file or directory: '/This folder does not exit'
os.getcwd
<built-in function getcwd>
os.getcwd()
'/Users/jazzgagan/Desktop/python'
os.getcwd()
'/Users/jazzgagan/Desktop/BooringStuff-Python'
import os
os.makedirs('/desktop/testing/test')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.makedirs('/desktop/testing/test')
  File "<frozen os>", line 215, in makedirs
  File "<frozen os>", line 215, in makedirs
  File "<frozen os>", line 225, in makedirs
OSError: [Errno 30] Read-only file system: '/desktop'
os.getcwd()
'/Users/jazzgagan/Desktop/BooringStuff-Python'
'/Users/jazzgagan/Desktop/BooringStuff-Python'
'/Users/jazzgagan/Desktop/BooringStuff-Python'
os.makedirs('/Users/jazzgagan/Desktop/Gagan/Sunar/Jumla')
os.getcwd()
'/Users/jazzgagan/Desktop/BooringStuff-Python'
os.getcwd('/Desktop/Gagan/Sunar')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    os.getcwd('/Desktop/Gagan/Sunar')
TypeError: posix.getcwd() takes no arguments (1 given)
os.path.abspath('.')
'/Users/jazzgagan/Desktop/BooringStuff-Python'
os.path.isaba(path)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.path.isaba(path)
AttributeError: module 'posixpath' has no attribute 'isaba'. Did you mean: 'isabs'?
os.path.isabs('.)
              
SyntaxError: incomplete input
os.path.isabs('.')
              
False
os.path.isabs('../')
              
False
os.path.abspath('.//scripts')
              
'/Users/jazzgagan/Desktop/BooringStuff-Python/scripts'
os.path.abspath('..')
              
'/Users/jazzgagan/Desktop'
os.path.abspath('.')
              
'/Users/jazzgagan/Desktop/BooringStuff-Python'
os.path.isabs('.')
              
False
os.path.isabs(''/Users/jazzgagan/Desktop/BooringStuff-Python')
              
SyntaxError: incomplete input
os.path.isabs(os.path.abspath('.'))
              
True
os.path.relpath('/Users/jazzgagan', '/Users')
              
'jazzgagan'
os.path.relpath('/Users/jazzgagan')
              
'../..'
os.path.relpath('/Users/jazzgagan/Desktop')
              
'..'
os.path.relpath('/BooringStuff-Python', '/Users/jazzgagan/Desktop')
              
'../../../BooringStuff-Python'
os.path.relpath('/BooringStuff-Python', '/Users/jazzgagan/')
              
'../../BooringStuff-Python'
os.path.relpath('/Desktop', '/Users')
              
'../Desktop'
path = '/Users/jazzgagan/Desktop/BooringStuff-Python'
              
os.path.basename(path)
              
'BooringStuff-Python'
os.path.dirname(path)
              
'/Users/jazzgagan/Desktop'
path = '/Users/jazzgagan/Desktop/BooringStuff-Python/birthday.py'
              
os.path.basename(path)
              
'birthday.py'
os.path.dirname(path)
              
'/Users/jazzgagan/Desktop/BooringStuff-Python'
path = '/Users/jazzgagan/Desktop/BooringStuff-Python/birthday.py'
              
os.path.split(path)
              
('/Users/jazzgagan/Desktop/BooringStuff-Python', 'birthday.py')
(os.path.dirname(path),os.path.basename(path))
              
('/Users/jazzgagan/Desktop/BooringStuff-Python', 'birthday.py')
path.split(')
           
SyntaxError: incomplete input
path.split(os.path.sep)
           
['', 'Users', 'jazzgagan', 'Desktop', 'BooringStuff-Python', 'birthday.py']
os.path.sep()
...            
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    os.path.sep()
TypeError: 'str' object is not callable
>>> os.path.sep('/')
...            
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    os.path.sep('/')
TypeError: 'str' object is not callable
>>> os.path
...            
<module 'posixpath' (frozen)>
>>> print(os.path)
...            
<module 'posixpath' (frozen)>
>>> 'Usrbin'.split(os.path.sep)
...            
['Usrbin']
>>> 'usrbin'.split(os.path.sep)
...            
['usrbin']
>>> os.path.getsize(path)
...            
475
>>> path
...            
'/Users/jazzgagan/Desktop/BooringStuff-Python/birthday.py'
>>> os.path.getsize('birthday.py')
...            
475
>>> os.path.getsize('/Users/jazzgagan/Desktop/BooringStuff-Python')
...            
704
>>> os.path.getsize('/Users/jazzgagan/Desktop')
...            
832
>>> os.path.getsize('/Users/jazzgagan')
...            
2848
>>> “os.path.getsize('C:\\Windows\\System32\\calc.exe')”
...            
SyntaxError: invalid character '“' (U+201C)
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
...            
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    os.path.getsize('C:\\Windows\\System32\\calc.exe')
  File "<frozen genericpath>", line 50, in getsize
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Windows\\System32\\calc.exe'
>>> os.path.listdir('/Users/jazzgagan/Desktop/BooringStuff-Python')
...            
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    os.path.listdir('/Users/jazzgagan/Desktop/BooringStuff-Python')
AttributeError: module 'posixpath' has no attribute 'listdir'. Did you mean: 'isdir'?
>>> os.listdir('/Users/jazzgagan/Desktop/BooringStuff-Python')
...            
['.DS_Store', 'charactercount.py', 'regexproject.py', 'PyWhatKit_DB.txt', 'oddEven.py', 'catnapping.py', 'test.py', 'url.py', 'picnictable.py', 'send_button_image.png', '.venv', 'pprintcharactercount.py', 'birthday.py', 'pw.py', 'printtable.py', 'tictactoe.py', 'isPhoneNumber.py', 'printgrid.py', 'testin.py', 'inventory.py', 'validinput.py']
>>> os.path.getsize('/Users/jazzgagan/Desktop/BooringStuff-Python')
...            
736
>>> os.getcwd()
...            
'/Users/jazzgagan/Desktop/BooringStuff-Python'
