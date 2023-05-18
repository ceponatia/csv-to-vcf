import csv

def csv_to_vcf(csv_filename, vcf_filename):
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(vcf_filename, 'w') as vcf_file:
            for row in csv_reader:
                vcf_file.write('BEGIN:VCARD\n')
                vcf_file.write('VERSION:3.0\n')
                vcf_file.write('N:{};{};;;\n'.format(row['LastName'], row['FirstName']))
                vcf_file.write('FN:{} {}\n'.format(row['FirstName'], row['LastName']))
                vcf_file.write('ORG:{}\n'.format(row['Organization']))
                vcf_file.write('TITLE:{}\n'.format(row['Title']))
                vcf_file.write('TEL;TYPE=WORK,VOICE:{}\n'.format(row['WorkPhone']))
                vcf_file.write('EMAIL;TYPE=PREF,INTERNET:{}\n'.format(row['Email']))
                vcf_file.write('END:VCARD\n')
                vcf_file.write('\n')

csv_to_vcf('contacts.csv', 'contacts.vcf')