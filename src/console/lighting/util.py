def calc_c_rate(c1, c2, duration, forwards):
    duration = float(duration)
    if forwards:
        if c2 > c1:
            return (c2 - c1) / duration
        else:
            return (((1.0 - c1) + c2) % 1.0) / duration
    else:
        if c2 > c1:
            return (-c1 - (1.0-c2)) / duration
        else:
            return -(c1 - c2) / duration
