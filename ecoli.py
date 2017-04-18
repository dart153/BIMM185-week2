#!/usr/bin/env python

'''
A function that reads the genome of the organism and returns 
the genome as a single string.
Created by: Vasu Pranav Sai Iddamsetty
BIMM 185 Spring 2016-2017
'''
def getSequence():

	# Open the file and read all the lnes into the list
	file = open('GCF_000005845.2_ASM584v2_genomic.fna')
	lines = file.readlines()


	# initialize the string which will contain the full genome
	sequence = ''

	# remove the header line
	lines.pop(0)
	

	# Read the lines into the sequence string. 
	#Remove new line characters
	for line in lines:

		sequence += line.replace('\n','')

	return sequence


'''
A helper function which allows for the reversal and complementation of
a DNA sequence which is on the reverse strand.
'''
def reverseComplement(sequence):

	# Reverse the sequence
	reverse = sequence[::-1]

	#Initialze the return sequence
	seq = ''

	#A dictionary used to determine the complements
	dna = {'A':'T','G':'C','T':'A','C':'G'}

	# create the complemented list
	for i in reverse:

		seq += dna[i]

	return seq

'''
A function that reads the protein data and subsets the genome into
it's protein parts.
'''
def findProtein(sequence):

	# Open the file and read the lines into a list
	file = open('ProteinTable167_161521.txt')
	lines = file.readlines()

	# Remove the header line
	lines.pop(0)

	#Convert the genome into an indexable list
	sequence = list(sequence)

	#Iterate throught the table
	for line in lines:

		data = line.split('\t')

		#Prepare the necessary information
		
		start = int(data[2])-1
		end = int(data[3])-1

		locus = data[8]
		geneID = data[7]
		strand = data[6]

		#initialize the string to be printed
		seq = ''

		#Determine if the sequence is on the reverse strand
		if data[4] == '-':

			seq = list(reverseComplement(sequence[start:end]))

		else:


			seq = sequence[start:end]
		

		#Print the header for the sequence
		print('>%s|%s|%s' %(locus,strand,geneID))

		#print lines with 70 characters max
		while len(seq)>70:

			print(''.join(seq[0:70]))
			del seq[0:70]

		if seq is not None:

			print(''.join(seq))

'''
Executes the routine to read the E. coli genome
and find all the protein sequence
'''
if __name__ == "__main__":

	sequence = getSequence()
	findProtein(sequence)
