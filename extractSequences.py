#!/usr/bin/env python

'''
Created by: Vasu Pranav Sai Iddamsetty
BIMM 185 Spring 2016-2017
'''

'''
A function whose purpose is to read the input file for the E. coli genome
and return it as a single string.
'''
def getSequence():

	# Open the file and read the lines into a list
	file = open('GCF_000005845.2_ASM584v2_genomic.fna')
	lines = file.readlines()

	# Intiailize the string that will contain the genome
	sequence = ''

	# Remove the header
	lines.pop(0)
	
	# Read the lines of the sequence
	#Remove the newlines
	for line in lines:

		sequence += line.replace('\n','')

	return sequence

'''
A function whose purpose is to return the reverse complement of the sequence that is inputed as the parameter.
'''
def reverseComplement(sequence):

	# Reverse the string
	reverse = sequence[::-1]

	#Initialize the string to return
	seq = ''

	#A dictionary which helps determine the complement
	dna = {'A':'T','G':'C','T':'A','C':'G'}

	# Create the complemented strand
	for i in reverse:

		seq += dna[i]

	return seq


'''
A functions whose purpose is to read the file containing all the proteins in the E. coli genome and find the sequence of each protein.
'''
def findProtein(sequence):

	#open the file and read the lines into a list
	file = open('ProteinTable167_161521.txt')
	lines = file.readlines()

	#Remove the header
	lines.pop(0)

	# make the sequence indexable
	sequence = list(sequence)


	#iterate throught the table
	for line in lines:

		data = line.split('\t')

		#Prepare the necessary information
		
		start = int(data[2])-1
		end = int(data[3])

		locus = data[8]
		geneID = data[7]
		strand = data[6]

		seq = ''

		#if the sequence is on the reverse strand, get the reverse complement
		if data[4] == '-':

			seq = reverseComplement(sequence[start:end])

		else:


			seq = ''.join(sequence[start:end])
		
		#print the GeneId and the sequence
		if len(seq) == 3:
			print('%s\t%s' %(geneID,seq))


'''
Executes the routine of the program
'''

if __name__ == "__main__":

	sequence = getSequence()
	findProtein(sequence)
