def compare(feed1, feed2):
    # (trip_id, stop_seq, timestamp)
    stops = []

    # trip_id: stop_seq
    parsed1 = { f[1]: f[5] for f in feed1 }
    for f in feed2:
        if f[1] in parsed1:
            if parsed1[f[1]] != f[5]:
                stops.append((f[1], parsed1[f[1]], f[6]))
            # del parsed1[f[1]]

    return stops