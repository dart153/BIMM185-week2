#!/usr/bin/env python
import textwrap

'''
Created by: Vasu Pranav Sai Iddamsetty
BIMM 185 Spring 2016-2017
'''

#Define a dictionary to keep track of the global count
globalCodons = {'ATG':0,'TTT':0,'TTC':0,'TTA':0,'TTG':0,'CTT':0,'CTC':0,'CTA':0,'CTG':0,'ATT':0,'ATC':0,'ATA':0,'GTT':0,'GTC':0,'GTA':0,'GTG':0, 'TCT':0,'TCC':0,'TCA':0,'TCG':0,'CCT':0,'CCC':0,'CCA':0,'CCG':0,'ACT':0,'ACA':0,'ACC':0,'ACG':0,'GCT':0,'GCC':0,'GCA':0, 'GCG':0,'TAT':0,'TAC':0,'CAT':0,'CAC':0,'CAA':0,'CAG':0,'AAT':0,'AAC':0,'AAA':0,'AAG':0,'GAT':0,'GAC':0,'GAA':0,'GAG':0,'TGT':0,'TGC':0,'TGG':0,'CGT':0,'CGC':0,'CGA':0,'CGG':0,'AGT':0,'AGC':0,'AGA':0,'AGG':0,'GGT':0,'GGC':0,'GGA':0,'GGG':0,'TGA':0,'TAG':0,'TAA':0 }

#Define a variable to keep track of the the total number of codons
totalCodonCount = 0


#Read the file containing the gene ID and the sequence

def readProteins():

	#Open the file and read it into a list
	file = open('ecoli_proteins.txt','rw')	
	lines = file.readlines()

	# A list of the codons used to create the header
	codons = ['ATG','TTT','TTC','TTA','TTG','CTT','CTC','CTA','CTG','ATT','ATC','ATA','GTT','GTC','GTA','GTG', 'TCT','TCC','TCA','TCG','CCT','CCC','CCA','CCG','ACT','ACA','ACC','ACG','GCT','GCC','GCA', 'GCG','TAT','TAC','CAT','CAC','CAA','CAG','AAT','AAC','AAA','AAG','GAT','GAC','GAA','GAG','TGT','TGC','TGG','CGT','CGC','CGA','CGG','AGT','AGC','AGA','AGG','GGT','GGC','GGA','GGG','TGA','TAG','TAA']

	# print the header
	print('geneID\t%s\tTotal'% ('\t'.join(codons)))

	# uses the global variable rather than creating a local variable
	global totalCodonCount


	#iterate through the table
	for line in lines:

		#Read the data (gene ID and sequence)
		data = line.split('\t')

		geneID = data[0]
		sequence = data[1].replace('\n','')


		#Check that the protein sequence is complete
		if len(sequence)%3 == 0:

			
			# create a list of the three base pair codons	
			codonList = seperateCodons(sequence)

			#return a list of the codon counts
			values = translator(codonList)
			
			# create a list containing the values in the
			# same order as the header
			codonstring=[]

			for codon in codons:
				codonstring.append(values[codon])


			#Create  the tab seperated list
			output = '\t'.join(map(str,codonstring))

			#Print the data
			print('%s\t%s\t%s' % (geneID,output,str(len(sequence))))
	
	#initialize a list to hold all the gloabl calues					
	totalCodons = []

	#Create a list in the same order as the header
	#Increment the global codon count
	for codon in codons:
		
		totalCodons.append(str(globalCodons[codon]))
		totalCodonCount += globalCodons[codon]

	#Print the data
	print('Total\t%s\t%s' % ('\t'.join(totalCodons),str(totalCodonCount)))

#Seperate the genes into codons.
def seperateCodons( sequence):


	return textwrap.wrap(sequence,3)
		 

def translator(codonList):

	codons = {'ATG':0,'TTT':0,'TTC':0,'TTA':0,'TTG':0,'CTT':0,'CTC':0,'CTA':0,'CTG':0,'ATT':0,'ATC':0,'ATA':0,'GTT':0,'GTC':0,'GTA':0,'GTG':0, 'TCT':0,'TCC':0,'TCA':0,'TCG':0,'CCT':0,'CCC':0,'CCA':0,'CCG':0,'ACT':0,'ACA':0,'ACC':0,'ACG':0,'GCT':0,'GCC':0,'GCA':0, 'GCG':0,'TAT':0,'TAC':0,'CAT':0,'CAC':0,'CAA':0,'CAG':0,'AAT':0,'AAC':0,'AAA':0,'AAG':0,'GAT':0,'GAC':0,'GAA':0,'GAG':0,'TGT':0,'TGC':0,'TGG':0,'CGT':0,'CGC':0,'CGA':0,'CGG':0,'AGT':0,'AGC':0,'AGA':0,'AGG':0,'GGT':0,'GGC':0,'GGA':0,'GGG':0,'TGA':0,'TAG':0,'TAA':0 }

	for triplet in codonList:

		#print(triplet)

		codons[triplet]+=1
		globalCodons[triplet]+=1


	return codons

'''
Executes the routine
'''
if __name__ == "__main__":

	readProteins()		
