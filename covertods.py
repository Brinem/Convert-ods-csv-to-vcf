import os
from pyexcel_ods import get_data
from vobject import vCard


def ods_to_vcard(ods_file, vcard_file):
    # Read data from the ODS file
    data = get_data(ods_file)

    # Extract data from the first sheet (assuming only one sheet is present)
    sheet_data = data[list(data.keys())[0]]

    # Iterate over rows in the sheet and generate vCard objects
    for row in sheet_data:
        if len(row) < 2:
            print("Skipping row with missing or invalid data:", row)
            continue

        # Extract name and phone number
        name, phone_number = row[:2]

        # Creating a vCard object
        vcard = vCard()
        vcard.add('fn').value = name
        vcard.add('tel').value = phone_number

        # Writing vCard to file
        with open(vcard_file, 'a') as vcardfile:
            vcardfile.write(vcard.serialize())


# Specify the full path to your ODS file
ods_file_path = '/home/brian/Downloads/phone_numbers.csv.ods'

# Specify the name for the output vCard file
vcard_file_path = '/home/brian/Downloads/output.vcf'

# Usage
ods_to_vcard(ods_file_path, vcard_file_path)
