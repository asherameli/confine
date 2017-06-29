# confine
Metadata-Version: 1.0
Name: confine
Version: 1
Summary: identifying disease module
Home-page: https://github.com/asherameli/confine
Author: Asher Ameli
Author-email: aameli@bwh.harvard.edu
License: SharmaLab - Channing Division of Network Medicine
Description: TO INSTALL:
        1. on terminal, find the directory where the package is located.
        2. pip install .
        
        INPUT FORMAT:
        it should be either in csv or txt format. It includes 2 Comma-delimited columns
        in which the first column is reserved for gene id and the second is reserved for 
        corresponding gene p.value.
        
        OUTPUTS:
        1. a text file that includes gene id and gene symbol of LCC genes
        2. a png file that shows how the significance of LCC varies with P.value cut-off
        
        
        TO RUN:
        1. Place input file in INPUT folder
        2. call python on your terminal
        3. import confine
        4. confine.run()
        
        TO ACCESS OUTPUT FILES:
        two output files are being generated with the same name of input file and will
        be placed on OUT directory
        
        
        TO TEST
        1. call python on terminal
        2. import confine
        3. confine.run()
        4. Answer 1st question
        "Enter your file name located at INPUT folder: " test.csv
        5. Answer 2nd question
        Enter the minimum size of LCC, we recommend a number between 30 and 50: " 50
        6. Answer last question
        Enter the maximum size of LCC, we recommend a number between 300 and 500: " 350
        
        GOAL:
        Identifying the most significant region of connections between disease-related proteins with 
        a limited size by user.
        
Platform: UNKNOWN
