from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from pages.models import buildingData
import openpyxl
import pandas as pd

def excel_to_txt(excel_file, txt_file):
    """pulls out the data from columns of an excel document and turns it into a csv document. Each row is a new 'building', each
    column is a different data point
    
    Inputs: excel_file, txt_file
    """
    # Load the workbook
    workbook = openpyxl.load_workbook(excel_file)

    # Select the worksheet
    worksheet = workbook.active

    # Read the data from columns B and D
    data = []
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        col_a, col_b, col_c, col_d, col_e, col_f, col_g, col_h = row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
        if col_b:
            data.append([col_a, col_b, col_c, col_d, col_e, col_f, col_g, col_h])

    # Convert the data to a DataFrame using pandas
    df = pd.DataFrame(data, columns=['col_a', 'col_b', 'col_c', 'col_d', 'col_e', 'col_f', 'col_g', 'col_h'])

    # Write the data to a text file
    with open(txt_file, 'w') as f:
        for index, row in df.iterrows():
            f.write(f"{row['col_a']}\t{row['col_b']}\t{row['col_c']}\t{row['col_d']}\t{row['col_e']}\t{row['col_f']}\t{row['col_g']}\t{row['col_h']}\n")


class Command(BaseCommand):
    help = 'Loads data from building data file'
    
    def add_arguments(self, parser):
        parser.add_argument('excel_file', type=str, help='Path to Excel file')

    def handle(self, *args, **options):
        excel_file = options['excel_file']
        txt_file = "tempBuildingData.txt"

        # Convert Excel file to temporary text file
        excel_to_txt(excel_file, txt_file)

        # Update buildingData model data from temporary text file
        with open(txt_file, 'r') as f:
            for line in f:
                # Splits up all of the data
                b_data = line.strip().split('\t')
                temp_name = b_data[0].strip()
                temp_elevator = b_data[1].strip()
                temp_elevator_working = b_data[2].strip()
                temp_ramps = b_data[3].strip()
                temp_entrances = b_data[4].strip()
                temp_m_entrances = b_data[5].strip()
                temp_lat = b_data[6].strip()
                temp_long = b_data[7].strip()
                
                # Get or create the building object with the building's name
                newBuild, created = buildingData.objects.get_or_create(buildingName=temp_name)

                # populate data for new building object
                newBuild.hasElevator = temp_elevator
                newBuild.isElevatorWorking = temp_elevator_working
                newBuild.hasRamps = temp_ramps
                newBuild.numEntrances = temp_entrances
                newBuild.numMotorizedEntrances = temp_m_entrances
                newBuild.latitude = temp_lat
                newBuild.longitude = temp_long
                
                
                # Save the updated Building object
                newBuild.save()
                

                # Print a message for each updated Building object
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created Building: {temp_name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated Building: {temp_name}'))#)

#python manage.py loadBuildings ".\pages\management\BuildingData.xlsx"