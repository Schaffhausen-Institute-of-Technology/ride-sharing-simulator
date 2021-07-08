import sys
import csv
import os

def generate_csv_file(destination_path, filename, header, rows):
    os.makedirs(destination_path, exist_ok=True)
    with open(f'{destination_path}/{filename}.csv', mode='w', newline='') as file:
                file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                file_writer.writerow(header)
                for row in rows:
                    file_writer.writerow(row)

def merge(scenario):
    path = f"../output/{scenario}/rides"

    for health_dimension in ["C","H","R"]:
        ride_filename = f"rides_{scenario}_{health_dimension}"
        net_filename = f"net_{scenario}_{health_dimension}"

        merge_rows = []

        with open(f"../output/{scenario}/rides/{ride_filename}.csv") as ride_file:
            csv_rides_reader = csv.reader(ride_file, delimiter=',')
            read_net_header = True
            header = next(csv_rides_reader)

            for ride_row in csv_rides_reader:
                request_timestamp = ride_row[0]

                merge_row = ride_row

                with open(f"../output/{scenario}/net/{net_filename}.csv") as net_file:
                    csv_net_reader = csv.reader(net_file, delimiter=',')

                    if (read_net_header):
                        read_net_header = False
                        net_header = next(csv_net_reader)
                        header.extend(net_header[1:])
                    else:
                        next(csv_net_reader)

                    for net_row in csv_net_reader:
                        if (int(net_row[0]) == int(float(request_timestamp))):
                            merge_row.extend(net_row[1:])
                            merge_rows.append(merge_row)
                            break
        generate_csv_file(f"../output/{scenario}/merge",f"merge_{scenario}_{health_dimension}",header,merge_rows)





def run():
    scenario = sys.argv[1]
    merge(scenario)

run()