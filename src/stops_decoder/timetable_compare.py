# stop_events: [trip_id, stop_seq, timestamp][]
# stop_times: [trip_id, arrival_time, departure_time, stop_id, stop_sequence, stop_headsign, pickup_type, drop_off_type][]
# returns: (stop_id, timestamp, departure_time, trip_id)
def compareWithTimetable(stop_events, stop_times):
    # Make a dictionary keyed by trip_id and stop_sequence
    # yielding the departure time for each stop and the stop id
    stop_times = { (t[0], t[4]): (t[2], t[3]) for t in stop_times }

    result = []

    for [trip_id, stop_seq, actual_time] in stop_events:
        if (trip_id, stop_seq) not in stop_times:
            continue

        (tt_time, stop_id) = stop_times[(trip_id, stop_seq)]
        result.append((stop_id, actual_time, tt_time, trip_id))
    
    return result