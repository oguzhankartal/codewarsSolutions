def barista(coffees):
    coffees.sort()
    waitingtime = 0
    for i, value in enumerate(coffees):
        waitingtime += value * (len(coffees)-i) + 2*(i)
    return waitingtime
