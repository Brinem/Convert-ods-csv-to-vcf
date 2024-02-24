import os
import csv
from vobject import vCard


def csv_to_vcard(csv_file, vcard_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 1 or ',' not in row[0]:
                print("Skipping row with missing or invalid data:", row)
                continue

            # Split each row into name and phone number using comma as delimiter
            name, phone_number = row[0].split(',', 1)
            name = name.strip()
            phone_number = phone_number.strip()

            # Remove any leading space from phone number
            phone_number = phone_number.lstrip()

            # Creating a vCard object
            vcard = vCard()
            vcard.add('fn').value = name
            vcard.add('tel').value = phone_number

            # Get the directory path of the CSV file
            directory = os.path.dirname(csv_file)

            # Construct the path for the vCard file in the same directory
            vcard_file_path = os.path.join(directory, vcard_file)

            # Writing vCard to file
            with open(vcard_file_path, 'a') as vcardfile:
                vcardfile.write(vcard.serialize())


# Specify the full path to your CSV file
csv_file_path = '/home/brian/Downloads/phone_numbers.csv'

# Specify the name for the output vCard file
vcard_file_name = 'output.vcf'

# Usage
csv_to_vcard(csv_file_path, vcard_file_name)
