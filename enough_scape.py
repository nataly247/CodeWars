def enough(cap, on, wait):
    if cap >= on + wait:
        return 0
    elif cap < on + wait:
        return on + wait - cap

# other version


def enough(cap, on, wait):
    if wait + on > cap:
        return wait + on - cap
    else:
        return 0
