import csv

input_filename = "security_incidents.csv"
output_filename = "security_incidents_modified.csv"

with open(input_filename, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    data = [row for row in reader]

if data and "Status" not in data[0]:
    data[0].append("Status")
    for row in data[1:]:  
        row.append("Pending")

with open(output_filename, mode="w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

print(f"Modified CSV file saved as {output_filename}")