"""This module splits VCF files containing a large number of contacts into
sizes that Google Contacts & iCloud Contacts can handle (1200 and ~500, respectively)"""

import csv
import os

def split_vcf(vcf_file, output_dir):
    """Splits VCF file by the number of contacts specified in contact_number"""
    with open(vcf_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        contact_number = 1200
        current_file = 1
        current_count = 0
        in_contact = False
        contact_rows = []  # List to accumulate contact rows
        
        for row in reader:
            if len(row) > 0:
                if row[0] == "BEGIN:VCARD":
                    in_contact = True
                    contact_rows.append(row)  # Add "BEGIN:VCARD" to contact_rows list
                elif row[0] == "END:VCARD":
                    in_contact = False
                    contact_rows.append(row)  # Add "END:VCARD" to contact_rows list
                    contact_rows.append([])  # Add a blank line between contacts
                    current_count += 1
                    
                    if current_count == contact_number:
                        current_count = 0
                        write_contact(contact_rows, output_dir, current_file)  # Write the contact rows
                        current_file += 1
                        contact_rows = []  # Reset contact_rows for the next contact
                else:
                    if in_contact:
                        contact_rows.append(row)  # Add non-empty rows to contact_rows list
        
        # Write the last contact after the loop ends
        if contact_rows:
            write_contact(contact_rows, output_dir, current_file)

def write_contact(contact_rows, output_dir, current_file):
    """Writes contacts to output file in the size specified in split_vcf"""
    with open(os.path.join(output_dir, f"contact_{current_file}.vcf"), "w", encoding="utf-8") as write:
        writer = csv.writer(write, lineterminator='\n')
        for row in contact_rows:
            if row != '':
                writer.writerow(row)

if __name__ == "__main__":
    VCF_FILE = "contacts.vcf"
    OUTPUT_DIR = "output"
    split_vcf(VCF_FILE, OUTPUT_DIR)
