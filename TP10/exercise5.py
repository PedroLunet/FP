def composition_relations(relations):
    return relations.union({(w, z) for w, x in relations for y, z in relations if y == x})

def transitive_closure(relations):
    return relations if composition_relations(relations).union(relations) == relations else transitive_closure(composition_relations(relations).union(relations))
