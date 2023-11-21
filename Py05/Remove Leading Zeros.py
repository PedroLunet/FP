def remove_leading(ip):
    aux_l = ip.split(".")
    for i in range(len(aux_l)):
        aux_l[i] = str(int(aux_l[i]))  # Convert to integer and back to string to remove leading zeros
    return ".".join(aux_l)

