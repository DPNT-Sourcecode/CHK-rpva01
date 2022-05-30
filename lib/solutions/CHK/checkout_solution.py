

# noinspection PyUnusedLocal
# skus = unicode string

unit_cost = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, 
            "H": 10, "I": 35, "J": 60, "K": 70, "L": 90, "M": 15, "N": 40, 
            "O": 10, "P": 50, "Q": 30, "R": 50, "S": 20, "T": 20, "U": 40, 
            "V": 50, "W": 20, "X": 17, "Y": 20, "Z": 21}
multi_deals = {"A": [(5, 200), (3, 130)], "B": [(2,45)], 
            "H": [(10, 80), (5, 45)], "K" : [(2,150)], 
            "P" : [(5,200)], "Q": [(3, 80)], "V": [(3,130), (2,90)]}
free_deals = [("E", 2 , "B", 1), ("F", 2, "F", 1), ("N", 3, "M", 1), 
            ("R", 3, "Q", 1), ("U", 3, "U", 1)]
joint_deals = [(("S", "T", "X", "Y", "Z"), 45, 3)]

def checkout(skus):
    
    quantities = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0,
                "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0,
                "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                "Y": 0, "Z": 0}
    
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
            if f[0] == f[2]:
                x = quantities[f[2]]//(f[1]+f[3])
                y = max(0,quantities[f[2]] - (f[1]+f[3])*x - f[1])
                print(x,y)
                quantities[f[2]] -= f[3]*x + y
            else:
                quantities[f[2]] -= f[3]*(quantities[f[0]]//f[1])
                quantities[f[2]] = max(0, quantities[f[2]])
    
    ord_joint_deals = {}
    for j in joint_deals[0][0]:
        ord_joint_deals[j] = unit_cost[j]
    ord_joint_deals = dict(sorted(ord_joint_deals.items(), 
                        key= lambda item: item[1], reverse=True))

    for x in ord_joint_deals:
        ord_joint_deals[x] = quantities[x]

    sum_ojds = joint_deals[0][2]*(sum(ord_joint_deals.values())//joint_deals[0][2])
    subtotal = sum_ojds//joint_deals[0][2]

    for x in ord_joint_deals:
        if sum_ojds > 0:
            quantities[x] = max(0, ord_joint_deals[x]-sum_ojds)
            sum_ojds -= ord_joint_deals[x]
        else:
            break

    total += subtotal*joint_deals[0][1]
    
    for c in quantities:
        X = multi_deals.get(c, [])
        for x in X:
            total += x[1]*(quantities[c]//x[0])
            quantities[c] -= x[0]*(quantities[c]//x[0])

        total += quantities[c]*unit_cost[c]

    return total

