def total_distance(dist, cities):
    result = 0
    for i in range(1, len(cities)):
        trip = (cities[i - 1], cities[i])
        if trip in dist.keys():
            result += dist[trip]
        elif trip[::-1] in dist.keys():
            result += dist[trip[::-1]]
        elif trip == trip[::-1]:
            result += 0
        else:
            return -1
    return result



print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Lisboa']))
#    325
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Coimbra','Viseu','Coimbra']))
#    305
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto','Lisboa','Coimbra']))
#    -1
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Lisboa','Coimbra','Porto','Braga','Vigo']))
#    490
print(total_distance({('Coimbra','Porto'):125, ('Coimbra','Lisboa'):200, ('Coimbra','Viseu'):90, ('Porto','Braga'):55, ('Braga','Vigo'):110}, ['Porto']))
#    0

print(total_distance({('Porto','Coimbra'):125, ('Coimbra','Lisboa'):200, ('Lisboa','Evora'):133, ('Beja','Evora'):55, ('Faro','Beja'):145}, ['Lisboa','Beja','Evora']))
#    -1
print(total_distance({('Porto','Coimbra'):125, ('Coimbra','Lisboa'):200, ('Lisboa','Evora'):133, ('Beja','Evora'):55, ('Faro','Beja'):145}, ['Lisboa','Evora','Beja']))
#    188
print(total_distance({('Porto','Coimbra'):125, ('Coimbra','Lisboa'):200, ('Lisboa','Evora'):133, ('Beja','Evora'):55, ('Faro','Beja'):145}, ['Faro','Beja','Evora']))
#    200
print(total_distance({('Porto','Coimbra'):125, ('Coimbra','Lisboa'):200, ('Lisboa','Evora'):133, ('Beja','Evora'):55, ('Faro','Beja'):145}, ['Lisboa','Coimbra','Lisboa','Evora','Beja','Faro']))
#    733
print(total_distance({('Porto','Coimbra'):125, ('Coimbra','Lisboa'):200, ('Lisboa','Evora'):133, ('Beja','Evora'):55, ('Faro','Beja'):145}, ['Faro']))
#    0