def total_distance(dist, cities):
    ttl = 0

    if len(cities) <= 1:
        return ttl
    else:
        for i in range(1,len(cities)):
            trip = (cities[i -1], cities[i])
            trip2 =(cities[i], cities[i - 1])
            if dist.get(trip) == None:
                if dist.get(trip2) == None:
                    return -1
                else:
                    ttl += dist.get(trip2)
            else:
                    ttl += dist.get(trip)
 
    return ttl