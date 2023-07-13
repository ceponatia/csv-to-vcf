import csv
import os

def split_vcf(vcf_file, output_dir):
    with open(vcf_file, "r") as f:
        reader = csv.reader(f)
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
                    
                    if current_count == 1200:
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
    with open(os.path.join(output_dir, f"contact_{current_file}.vcf"), "w") as w:
        writer = csv.writer(w, lineterminator='\n')
        for row in contact_rows:
            if row != '':
                writer.writerow(row)

if __name__ == "__main__":
    vcf_file = "contacts.vcf"
    output_dir = "output"
    split_vcf(vcf_file, output_dir)