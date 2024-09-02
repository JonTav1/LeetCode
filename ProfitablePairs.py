def getProfitablePairs(profit, implementationCost):
    num_projects = len(profit)
    net_profits = [profit[i] - implementationCost[i] for i in range(num_projects)]
    
    net_profits.sort()
    
    left = 0
    right = num_projects - 1
    valid_pairs = 0
    
    while left < right:
        if net_profits[left] + net_profits[right] > 0:
            valid_pairs += (right - left)
            right -= 1
        else:
            left += 1
    
    return valid_pairs