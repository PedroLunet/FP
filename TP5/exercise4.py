def multi(g):
    multiplicities = {}
    
    for edge in g:
        if edge in multiplicities:
            multiplicities[edge] += 1
        else:
            multiplicities[edge] = 1

    triples = [(edge[0], multiplicities[edge], edge[1]) for edge in multiplicities]

    return tuple(triples)
    