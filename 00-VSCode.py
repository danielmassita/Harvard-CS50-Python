# VS Code Terminal - CLI Command Line Interface

"""
UNIX COMMMANDS

ls # list files in the current folder
cp # copy a file from one place to another
mv # move or rename from one place to another
rm # remove
mkdir # make a new directory (folder)
cd # change folder from one to another
rmdir # remove a directory (folder)
clear # clear terminal window (Ctrl+L)
"""


$ code hello.py 
# creates the hello.py file

$ python hello.py 
# runs the code

$ ls
hello.py

$ cp hello.py goodbye.py
# create a coppy of the file with a different name

$code goodbye.py
# allows me to code the new created file

$ ls
hello.py goodbye.py
# lists the files in the current folder

$ mv goodbye.py farewell.py
# renames in the same folder

$ rm farewell.py
rm: remove regular file 'farewell.py'? Y/N

$ mkdir folder
# creates a new folder

$ ls
folder/		hello.py

$ cd folder/
folder/ $ ls
(	) (	)
# we entered in the folder where we are, thou its empty

folder/ $ code farewell.py
# creates a new file inside the "folder/"

folder/ $ mv farewell.py .. 
# the .. redirects to the "parent folder"

folder/ $ ls


folder/ $ cd (goes to the primary folder)
$

$ ls
farewell.py	folder/		hello.py

$ rmdir folder







