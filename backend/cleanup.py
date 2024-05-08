import csv

def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        # Open the CSV file for writing
        with open(output_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            
            # Flag to keep track of whether header has been written or not
            header_written = False
            
            # Parse each line of the text file and write it to the CSV file
            for line in txt_file:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Split the line by comma
                parts = line.strip().split(',')
                
                # Write the header row if it hasn't been written yet
                if not header_written:
                    # Write the header row excluding the "Chq/Ref Number" and "Value Date" columns
                    header = ['Date', 'Narration', 'Debit Amount', 'Credit Amount', 'Closing Balance']
                    writer.writerow(header)
                    header_written = True
                    continue
                
                # Exclude the "Chq/Ref Number" and "Value Date" columns while writing the parts to the CSV file
                row = [part.strip() for i, part in enumerate(parts) if i not in (2, 5)]  # Exclude columns at index 2 (Value Date) and 5 (Chq/Ref Number)
                writer.writerow(row)

# Provide the paths to your input and output files
input_file = 'data.txt'
output_file = 'data.csv'

# Convert the text file to CSV, excluding the "Chq/Ref Number" and "Value Date" columns
txt_to_csv(input_file, output_file)

