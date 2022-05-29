

# noinspection PyUnusedLocal
# skus = unicode string

unit_cost = {"A": 50, "B": 30, "C":20, "D": 15, "E": 40}
multi_deals = {"A": [(5, 200), (3, 130)], "B": [(2,45)]}
free_deals = [("E", 2 , "B", 1)]

def checkout(skus):
    
    quantities = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    
    for c in skus:
        if c in unit_cost and c in quantities:
            quantities[c] += 1
        elif c in unit_cost:
            quantities[c] = 0
        else:
            return -1
    
    total = 0

    for f in free_deals:
        if f[0] in quantities and f[2] in quantities:
            quantities[f[2]] -= f[3]*(quantities[f[0]]//f[1])
            quantities[f[2]] = max(0, quantities[f[2]])
    
    for c in quantities:
        X = multi_deals.get(c, [])
        for x in X:
            print(c, quantities[c])
            total += x[1]*(quantities[c]//x[0])
            quantities[c] -= x[0]*(quantities[c]//x[0])

        total += quantities[c]*unit_cost[c]

    return total