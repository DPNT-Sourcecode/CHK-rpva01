

# noinspection PyUnusedLocal
# skus = unicode string

unit_cost = {"A": 50, "B": 30, "C":20, "D": 15}
deals = {"A": (3, 130), "B": (2,45), "C": (1,20), "D": (1,15)}

def checkout(skus):
    
    quantities = {"A": 0, "B": 0, "C": 0, "D": 0}
    
    for c in skus:
        if c in quantities:
            quantities[c] += 1
        else:
            return -1
    
    total = 0
    for c in quantities:
        total += (quantities[c]//deals[c][0])*deals[c][1] + (quantities[c]%deals[c][0])*unit_cost[c]

    return total