#!/usr/python

#Libraries
import sys
import glob
import os



def printInvalidInput():
    print >> sys.stderr, 'Incorrect number of arguements'
    print >> sys.stderr, 'python findFile.py -dirs [list of directories to search seperated by a ','] -ext [list of file extension of interest sperated by a \',\'>'
    sys.exit(1)
    return None

def getFiles(directories,extensions,outputfile):
    outFile = open(str(outputFile),'w')
    for d in directories:
        for root, dirs, files in os.walk(str(d)):
            for file in files:
                for ext in extensions:
                    if file.endswith(str(ext)):
                        outFile.write(str(os.path.join(root,file))+"\n")
    outFile.close()
    return None

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print "Less than 4"
        printInvalidInput()

    else:
        #variables
        directories = []
        extensions = []
        #get list of directores
        if '-dirs' in sys.argv:
            directories = str(sys.argv[sys.argv.index('-dirs')+1]).strip().split(',') 
        else:
            print "No -dirs"
            printInvalidInput()
        #Get Extension of interest
        if '-ext' in sys.argv:
            extensions = str(sys.argv[sys.argv.index('-ext')+1]).strip().split(',')
            
        else:
            print "No -ext"
            printInvalidInput()

    #Output filename
    outputFile = "listOfFiles.txt"
    listOfFiles = getFiles(directories,extensions,outputFile)
