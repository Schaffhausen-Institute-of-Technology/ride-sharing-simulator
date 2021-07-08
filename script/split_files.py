import sys
import csv
import os

def generate_csv_file(destination_path, filename, header_indexes, rows, prefix):
    os.makedirs(destination_path, exist_ok=True)
    with open(f'{destination_path}/{filename}.csv', mode='w', newline='') as file:
                file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                header = list(map(lambda x: f"{prefix}{'0' if x < 10 else ''}{x}", header_indexes[1:]))
                header.insert(0,"timestamp")
                file_writer.writerow(header)
                for row in rows:
                    file_writer.writerow(row)


def split_files(csv_reader, c_indexes, h_indexes, r_indexes):
        c_rides_rows = []
        h_rides_rows = []
        r_rides_rows = []
        for ride_row in csv_reader:
            c_ride_row = []
            h_ride_row = []
            r_ride_row = []

            for idx in c_indexes:
                c_ride_row.append(ride_row[idx-1])
            for idx in h_indexes:
                h_ride_row.append(ride_row[idx-1])
            for idx in r_indexes:
                r_ride_row.append(ride_row[idx-1])

            c_rides_rows.append(c_ride_row)
            h_rides_rows.append(h_ride_row)
            r_rides_rows.append(r_ride_row)

        return (c_rides_rows, h_rides_rows, r_rides_rows)


def map_rides_files(scenario):
    path = f"../output_{scenario}/rides"
    files = [filename.split(".")[0] for filename in os.listdir(path)]

    c_indexes = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21]
    r_indexes = [1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,19,20,22]
    h_indexes = [1,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,20,22]

    for filename in files:
        with open(f"{path}/{filename}.csv") as csv_file:
            csv_rides_reader = csv.reader(csv_file, delimiter=',')
            c_rides_rows, h_rides_rows, r_rides_rows = split_files(csv_rides_reader,c_indexes,h_indexes,r_indexes)
            generate_csv_file(f"../output/{scenario}/rides",f"rides_{scenario}_C",c_indexes,c_rides_rows,"s0")
            generate_csv_file(f"../output/{scenario}/rides",f"rides_{scenario}_H",h_indexes,h_rides_rows,"s0")
            generate_csv_file(f"../output/{scenario}/rides",f"rides_{scenario}_R",r_indexes,r_rides_rows,"s0")
            

def map_net_files(scenario):
    path = f"../output_{scenario}/net"
    files = [filename.split(".")[0] for filename in os.listdir(path)]

    c_indexes = [1,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21]
    h_indexes = [1,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    r_indexes = [1,2,3,4,8,9,10,11,12,13,15,21]

    for filename in files:
        with open(f"{path}/{filename}.csv") as csv_file:
            csv_rides_reader = csv.reader(csv_file, delimiter=',')
            c_rides_rows, h_rides_rows, r_rides_rows = split_files(csv_rides_reader,c_indexes,h_indexes,r_indexes)
            generate_csv_file(f"../output/{scenario}/net",f"net_{scenario}_C",c_indexes,c_rides_rows,"g0")
            generate_csv_file(f"../output/{scenario}/net",f"net_{scenario}_H",h_indexes,h_rides_rows,"g0")
            generate_csv_file(f"../output/{scenario}/net",f"net_{scenario}_R",r_indexes,r_rides_rows,"g0")


def map_area_files(scenario):
    path = f"../output_{scenario}/area"
    files = [filename.split(".")[0] for filename in os.listdir(path)]

    c_indexes = [1,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21]
    h_indexes = [1,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    r_indexes = [1,2,3,4,8,9,10,11,12,13,15,21]

    for filename in files:
        with open(f"{path}/{filename}.csv") as csv_file:
            csv_rides_reader = csv.reader(csv_file, delimiter=',')
            c_rides_rows, h_rides_rows, r_rides_rows = split_files(csv_rides_reader,c_indexes,h_indexes,r_indexes)
            generate_csv_file(f"../output/{scenario}/area",f"area_{scenario}_C",c_indexes,c_rides_rows,"g0")
            generate_csv_file(f"../output/{scenario}/area",f"area_{scenario}_H",h_indexes,h_rides_rows,"g0")
            generate_csv_file(f"../output/{scenario}/area",f"area_{scenario}_R",r_indexes,r_rides_rows,"g0")


def run():
    scenario = sys.argv[1]
    map_rides_files(scenario)
    map_area_files(scenario)
    map_net_files(scenario)

run()