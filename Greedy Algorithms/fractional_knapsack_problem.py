"""     fractional knapsack problem
time complexity of the fractional knapsack problem -> O(NlogN)
"""

class Item(object):
    def __init__(self, profit, weight ):
        self.weight = weight
        self.profit = profit
        self.ratio_by_profit = profit / weight


def  fractional_knapsack_problem(items , max_capacity):
    used_capacity = 0
    max_profit = 0
    items.sort(key=lambda x:x.ratio_by_profit,reverse=True)
    for values in items:
        if values.weight + used_capacity <= max_capacity:
            used_capacity += values.weight
            max_profit += values.profit
        else:
            remaning_capacity = max_capacity - used_capacity
            fraction = values.ratio_by_profit * remaning_capacity
            used_capacity += remaning_capacity
            max_profit += fraction
        if used_capacity == max_capacity:
            break
    print(f'Capacity of knapsack -> {max_capacity}')
    print(f'Maximum possible profit -> {int(max_profit)}')
#
item_1  = Item(10 , 2 )
item_2 = Item(5 , 3)
item_3 = Item(15 , 5)
item_4 = Item(7, 7)
item_5 = Item(6, 1)
item_6 = Item(18, 4)
item_7 = Item(3, 1)
#
lists = [item_1 , item_2 ,item_3, item_4 ,item_5 ,item_6 ,item_7]
# print(lists)
fractional_knapsack_problem(lists , 15)
