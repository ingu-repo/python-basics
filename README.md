# Python Basics

### Type
* "" : String   : Can change : 
* [] : Array    : Can change : keeps order: sort()
* () : Tuple    : No  change : No keeps order: 
* {} : Map      : Can change : keeps order: keys() values() items() 

```
t = "a", "b"
t = ("a", "b")
```

### Operator
* \* : Unpack. Pick out every element from list
```
list = ["a", "b"]
print (*list) # same as print (list[0], list[1])
Output: a b 
``` 

### Function
* lambda : one line function : lambda PARAMS : RETURN
```
f = lambda a, b : a + b
print (f(1, 2))
```

### Function Parameters
* '*'  : receive parameter as tuple
* '**' : receive parameter as map
```
f = lambda a, b : a + b
print (f(1, 2))
```

### General
*from PACKAGE import \**
> it can import all module names ONLY for the names not starting with _ (underscore)

*OS Independant*
> Python compiled codes can run platforms

*Exit Prompt*
> Ctrl+Z or Ctlr+D to quit python prompt

*Exit Program*
> quit() or exit() to quit python program

*struct Module*
> for handling binary data type<br>
> pack()   : python type to binary<br>
> unpack() : binary to python type

*Operand vs Operator*
> Operator is such as + - etc<br>
> Operand is such as variables constants etc

### Normalization
|Expression|Desc|Example|
|---|---|---|
|*| repeat previous char more than 0 times|u\* matches u or uu or uuu 
|^| the first char at string|\^a matches abc or apple apple etc
|$| the last char at string|d\$ matches cd or abcd etc
|.| one char except return code|a.c matches abc a+c etc
|\|| or|a\|c matches a or c 
|\\d| number|


### Package
Having various moudles. Usually each module saved by each directory<br>
* Installation
> pip will skip if the package is already installed

* requirements.txt for specifying versions to build an env easily
> numpy==1.20.1 <br>
> pandas==1.2.2 <br>
> matplotlib==3.3.4 <br>

* Module
> It consists of either a single file or multiple files<br>
> a module can import another module

* \__init\__.py
> called first when a package imported so that can do common initializing process

* import all functions from a package/module
> from math import *

### Python Environment
*Language Spec*
* Interprete and run line by line 
* As default, GUI toolset library is provided
* No need to declare variables
* Free from Open Source
*.python_history*
> store user command history in interactive mode in user directory

*bpython
> extended version of python for interactive mode

### Encoding
Default encoding in python3 is UTF-8
* How to run python with EUC-JP
> Save code file as EUC<br>
> Define encoding setting in code file<br>
> Set env locale as EUC<br>

* If want to use other encodings then need to define it on source codes at the first line or 2nd if Shebang
```
#! /Users/appa/.pyenv/versions/3.9.4/bin/python
# coding: EUC-JP
```

* System locale can be taken by locale module*
```
export LC_ALL=ja_JP.eucjp
export LC_ALL=ja_JP.UTF-8
python -c "import locale; print(locale.getpreferredencoding())"
```

* Python encoding can be defined in env variable
```
PYTHONIOENCODING=utf-8 python3 hello
```

### Command Line
* Run source codes in command line
```
python -c 'print ("good morning")'
```

* Interactive mode after file run
```
python -i hello.py
```

* Save Installed Package information to file
```
pip freeze > requirements.txt
```

## Mail
*smtplib*
* for sending email

*poplib*
* for receiving email

## Appendix
* timeif : checking python code running time
* doctest : running test codes in documentation
* unittest : standard library for unit testing of python codes
* sqlite3 : standard library for connecting to SQLite DB
* logging : for logging library







