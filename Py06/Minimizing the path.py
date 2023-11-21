def min_path(path):
    minimized_path = []
    for i in range(len(path)):
        if i == 0 or path[i] != path[i-1]:
            minimized_path.append(path[i])
    return minimized_path
 
 
 
 ###ERRADO