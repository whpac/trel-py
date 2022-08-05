import gtfs_realtime_pb2
import sys

# Example row of output:
# ('488', '1_5715761^M,X+', '488/12', 52.33440017700195, 17.16423988342285, 2, 1610041536)
def decodePositions(gtfs_message):
    positions = []
    for entity in gtfs_message.entity:
        if not entity.HasField('vehicle'):
            continue

        vehicle = entity.vehicle

        trip = vehicle.trip
        route_id = trip.route_id
        trip_id = trip.trip_id

        vehicleData = vehicle.vehicle
        label = vehicleData.label

        position = vehicle.position
        latitude = position.latitude
        longitude = position.longitude

        stop_seq = vehicle.current_stop_sequence
        timestamp = vehicle.timestamp
        
        positions.append((route_id, trip_id, label, latitude, longitude, stop_seq, timestamp))
    
    return positions

def getVehiclePositions(blob):
    gtfs_message = gtfs_realtime_pb2.FeedMessage()

    # Read the existing address book.
    gtfs_message.ParseFromString(blob)

    return decodePositions(gtfs_message)


# if len(sys.argv) != 2:
#     print("Usage:", sys.argv[0], "<GTFS RT feed>")
#     sys.exit(-1)
# print(getVehiclePositions(sys.argv[1])[0])
