import re

#open the text file
document = open("raw_text.txt","r")


#this is for year
expression = "\d\d\d\d$"
replace = "<year>"
docWithYearTags = regexprep(document,expression,replace)