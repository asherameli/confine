License: SharmaLab - Channing Division of Network Medicine

To better use the package install "pip" and "python 2.7"

TO INSTALL:
sudo pip install confine


PACKAGE REQUIREMENTS:
The code can install all required packages for you.
1. pickle
2. networkx
3. os
4. time
5. pylab
6. pkg_resources

To INSTALL PACKAGES:

1. call python
2. import confine
3. confine.check()

To TEST:
1. call python
2. import confine
3. confine.run('test')


INPUT FORMAT:
it should be either in csv or txt format. It includes 2 Comma-delimited columns
in which the first column is reserved for gene id and the second is reserved for 
corresponding gene p.value.


OUTPUTS:
1. a text file that includes gene id and gene symbol of LCC.
2. a png file that shows how the significance of LCC varies with P.value cut-off 
over LCC thresholds given by user.
directory: Outputs are being generated at directory where the user is running python


TO RUN:
1. call python
2. import confine
3. confine.run('optional_name')
4. Answer 1st question
"Enter your file name located at INPUT folder: " path/filename
5. Answer 2nd question
Enter the minimum size of LCC, we recommend a number between 30 and 50: " 50
6. Answer last question
Enter the maximum size of LCC, we recommend a number between 300 and 500: " 400


TO ACCESS OUTPUT FILES:
two output files are being generated in a directory that is names the same as 
'optional_name' followed by a unique number.


GOAL:
Identifying the most significant region of connections between disease-related proteins 
with a limited size by user.
