def list_average(list):

    total = 0

    if len(list) < 1:
        return None

    for i in range(len(list)):

        try:
            int(list[i])
        except:
            return None

        total += list[i]
    
    total = total / (len(list))

    return total