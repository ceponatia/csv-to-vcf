"""This module takes a csv file and converts it to vCard. There are many more
parameters for contact information, especially in version 4.0, but this module
contains the basics most people will use. You can easily add more by copying one
of the lines below and changing keywords as needed."""

import csv

def csv_to_vcf(csv_filename, vcf_filename):
    """converts csv files to vcard"""
    with open(csv_filename, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(vcf_filename, 'w', encoding="utf-8") as vcf_file:
            for row in csv_reader:
                vcf_file.write('BEGIN:VCARD\n')
                vcf_file.write('VERSION:3.0\n')
                vcf_file.write(f"N:{row['LastName']};{row['FirstName']};;;\n")
                vcf_file.write(f"FN:{row['FirstName']} {row['LastName']}\n")
                vcf_file.write(f"ORG:{row['Organization']}\n")
                vcf_file.write(f"TITLE:{row['Title']}\n")
                vcf_file.write(f"TEL;TYPE=WORK,VOICE:{row['WorkPhone']}\n")
                vcf_file.write(f"EMAIL;TYPE=PREF,INTERNET:{row['Email']}\n")
                vcf_file.write('END:VCARD\n')
                vcf_file.write('\n')

csv_to_vcf('contacts.csv', 'contacts.vcf')
