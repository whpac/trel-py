import csv
from argparse import ArgumentParser
from zipfile import ZipFile
from download_timetable import downloadGtfsFeed
from timetable_compare import compareWithTimetable
from decode_trips import decodeTripIds
from delay_calculator import calculateDelay

# Output format:
# stop_id, route_id, stop_timestamp, scheduled_time

# Parse the cmdline arguments
argparser = ArgumentParser()
argparser.add_argument('--date', '-d', type=str, required=True, help='Date for which to download the GTFS feed')
argparser.add_argument('--stops', '-s', type=str, required=True, help='Path to the stops record')
argparser.add_argument('--output', '-o', type=str, help='Output CSV file (decoded stops record)')
argparser.add_argument('--append', '-a', action='store_true', help='Append to the output CSV file')
args = argparser.parse_args()

gtfs = downloadGtfsFeed(args.date)
with ZipFile(gtfs, 'r') as zip:
    stop_times = zip.read('stop_times.txt').decode('utf-8').splitlines()
    trips = zip.read('trips.txt').decode('utf-8').splitlines()


with open(args.stops, 'r') as f:
    stop_log = f.read().splitlines()

stop_times = list(csv.reader(stop_times))
trips = list(csv.reader(trips))
stop_log = list(csv.reader(stop_log))


stops_with_actual = compareWithTimetable(stop_log, stop_times)
stops_decoded = decodeTripIds(stops_with_actual, trips)
stops_with_delay = calculateDelay(stops_decoded)

open_mode = 'a+' if args.append else 'w'
with open(args.output, open_mode) as f:
    for row in stops_with_delay:
        line = f'{row[0]},{row[3]},{row[1]},{row[2]}\n'
        f.write(line)