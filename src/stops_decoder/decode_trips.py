# stop_log: (stop_id, timestamp, departure_time, trip_id)[]
# trips: [route_id, service_id, trip_id, trip_headsign, direction_id, shape_id, wheelchair_accessible, brigade][]
# returns: [stop_id, timestamp, departure_time, route_id][]
def decodeTripIds(stop_log, trips):
    trips = { t[2]: t[0] for t in trips }

    result = []
    for s in stop_log:
        if s[3] not in trips:
            continue
        result.append([s[0], s[1], s[2], trips[s[3]]])
    
    return result