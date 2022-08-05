from datetime import datetime

# stop_log: [stop_id, timestamp, departure_time, route_id][]
# returns: [stop_id, actual_datetime, delay_minutes, route_id][]
def calculateDelay(stop_log):
    for i in range(len(stop_log)):
        actual_datetime = datetime.fromtimestamp(int(stop_log[i][1]))
        actual_date = str(actual_datetime.date())
        scheduled_datetime = datetime.strptime(f'{actual_date} {stop_log[i][2]}', '%Y-%m-%d %H:%M:%S')

        interval = actual_datetime - scheduled_datetime
        delay_minutes = int(interval.total_seconds() // 60)

        stop_log[i][1] = str(actual_datetime)
        stop_log[i][2] = delay_minutes

    return stop_log