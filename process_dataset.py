#Author: Chang Ee Chuan
#Date: 2020-08-22

import csv

#contains all the abbreviations in name field
abb_set = {
	'Mr.','Miss','Mrs.','Jr.','MD','DDS','PhD','DVM','Dr.','Ms.','III','II','IV'
}

#opening daily dataset file and begin processing
with open('dataset.csv', newline='') as f:

	#reader is a iterator which can be looped to process line by line
	reader = csv.reader(f)

	#Skip header row
	header = next(reader)

	#process each row in reader iterator
	for row in reader:

		#setting variables accordingly
		name = row[0]
		price = row[1]
		above_100 = "false"

		#split name string into a list, delimited by spaces
		name = name.split(" ")

		#declaring variables for first and last name
		first_name = ""
		last_name = ""

		#checking each component in name list
		for name_component in name:
			#check if the component is not an abbreviation, which means it is a proper name component
			if name_component not in abb_set:
				#check if first name have been loaded
				if first_name == "":
					first_name = name_component
				#check if last name have been loaded
				else:
					last_name = name_component


	



