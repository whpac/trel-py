from argparse import ArgumentParser
from datetime import datetime
from time import sleep
from download_feed import downloadGtfsRtFeed
from read_positions import getVehiclePositions
from compare_feeds import compare

# Output format:
# trip_id, stop_seq, timestamp


# Parse the cmdline arguments
argparser = ArgumentParser()
argparser.add_argument('--delay', '-d', type=int, default=10, help='Delay between feed downloads in seconds')
argparser.add_argument('--verbose', '-v', action='store_true', help='Print out some diagnostic information')
argparser.add_argument('--output', '-o', type=str, help='Output CSV file (record of stops)')
args = argparser.parse_args()


# The actual GTFS-RT parsing and comparison.
# The below code extracts the times when every vehicle stopped
# so that it can be then compared with the timetable
previousFeed = downloadGtfsRtFeed()
previousPositions = getVehiclePositions(previousFeed)
previousFeed = None # Not needed anymore
while True:
    sleep(args.delay)
    if args.verbose:
        print(f'Fetching at {datetime.now()}')

    try:
        currentFeed = downloadGtfsRtFeed()
        currentPositions = getVehiclePositions(currentFeed)
    except:
        print(currentFeed)
        continue

    diff = compare(previousPositions, currentPositions)
    previousPositions = currentPositions

    out_file = args.output if args.output is not None else datetime.now().strftime('%Y-%m-%d.csv')
    with open(out_file, 'a+') as f:
        for row in diff:
            line = f'{row[0]},{row[1]},{row[2]}\n'
            f.write(line)
