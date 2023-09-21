#-------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4250- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#importing some Python libraries
import csv
import string

documents = []
labels = []

#reading the data in a csv file
with open('resources\collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])
            labels.append(row[1])

print("Documents: ")
for e in documents:
    print(e)
print("======================================")

#Conduct stopword removal.
#--> add your Python code here
stopWords = {'I', 'and', 'She', 'They', 'her', 'their'}

print("Stopwords to check: ")
for i in stopWords:
    for j in documents:
        if i in j:
            temp = j.replace(i, "")
            print("Changed an occurance of \"" + i + "\"")
            documents.remove(j)
            documents.append(temp)
for j in documents:
    if "and" in j:
        temp = j.replace("and", "")
        print("Changed an occurrence of \"and\"")
        documents.remove(j)
        documents.append(temp)
print("Stopwords removed")
print("======================================")
print("Documents (Modified for stopword removal): ")
for k in documents:
    print(k)
print("======================================")
#Conduct stemming. (with a dictionary)
#--> add your Python code here
stemming = {
  "cats": "cat",
  "dogs": "dog",
  "loves": "love",
}
for l in documents: # Go through all three documents
    for m in stemming: # and Go through all entries
        print("Stemming in Progress for: \"" + m + "\" for the word: " + l )
        if l in m: # and go through every letter in the document
            temp = m.replace(l, stemming[l]) # finding any occurrences of the word and replacing it with its entry
            print(m.replace(l, stemming[l]))
            print("Changed an occurrence of \"" + l + "\"")
            documents.remove(m)
            documents.append(temp)

print("Documents (Modified for stemming): ")
for k in documents:
    print(k)
#Identify the index terms.
#--> add your Python code here
terms = []
for n in documents:
    temp = ""
    for o in n:
        if o != " ":
            temp = temp + o
        else:
            terms.append(temp)
            print("Added \"" + temp + "\" to the term list")
            temp = ""

for p in terms:
    print(p)
#Build the tf-idf term weights matrix.
#--> add your Python code here
docMatrix = []

#Calculate the document scores (ranking) using document weigths (tf-idf) calculated before and query weights (binary - have or not the term).
#--> add your Python code here
docScores = []

#Calculate and print the precision and recall of the model by considering that the search engine will return all documents with scores >= 0.1.
#--> add your Python code here