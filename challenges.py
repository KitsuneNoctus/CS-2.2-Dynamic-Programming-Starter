class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]: # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else: # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            #Square  will be at dp_table[row][col]

            #Base case
            if row == 0 or col == 0:
                dp_table[row][col] = 0
                continue

            #recusive case 1 - looking on the diagnol
            if strA[row-1] == strB[col-1]:
                prev_val = dp_table[row-1][col-1]
                dp_table[row][col] = prev_val + 1

            #recursive case 2 - looking up and left
            if strA[row-1] != strB[col-1]:
                top_val = dp_table[row][col-1]
                left_val = dp_table[row-1][col]
                dp_table[row][col] = max(top_val,left_val)

    print(dp_table)

    return dp_table[rows-1][cols-1]

def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # print(items)
    if items == [] or capacity <= 0:
        return 0

    if items[0][1] <= capacity:
        value_with = items[0][2] + knapsack(items[1:],capacity-items[0][1])
    else:
        value_with = 0
        
    value_without = knapsack(items[1:],capacity)
    
    return max(value_with,value_without)

def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            #fill in the table at i and j
            if row == 0 or col == 0:
                dp_table[row][col] = 0

            else:
                item = items[row-1]
                capacity = col

                value_without = dp_table[row-1][capacity]
                if item[1] <= capacity:
                    value_with = dp_table[row-1][capacity-item[1]] + item[2]
                    dp_table[row][col] = max(value_without, value_with)
                else:
                    dp_table[row][col] = value_without

    # for row in range(rows):
    #     print(dp_table[row])

    return dp_table[rows-1][cols-1]
    
def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    if len(str1) == 0 and len(str2) == 0:
        return 0
    if len(str1) != 0 and len(str2) == 0:
        return len(str1)
    if len(str2) != 0 and len(str1) == 0:
        return len(str2)

    # 1st recursive case
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1],str2[:-1])
    else:
        # 2nd is they don't match
        #insert
        insert = edit_distance(str1,str2[:-1])
        #delete
        delete = edit_distance(str1[:-1],str2)
        #replace
        replace = edit_distance(str1[:-1],str2[:-1])
        return 1 + min(insert, delete, replace)

def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    # TODO: Fill in the table using a nested for loop.
    for row in range(rows):
        for col in range(cols):
            # Base case
            # Figured change to base case from 
            # https://www.geeksforgeeks.org/edit-distance-dp-5/
            if row == 0:
                dp_table[row][col] = col
            elif col == 0:
                dp_table[row][col] = row

                # 1st recursive case
            elif str1[row-1] == str2[col-1]:
                # return edit_distance(str1[:-1],str2[:-1])
                prev_str = dp_table[row-1][col-1]
                dp_table[row][col] = prev_str
            else:
                # 2nd is they don't match
                #insert
                # insert = edit_distance(str1,str2[:-1])
                insert = dp_table[row][col-1]
                #delete
                # delete = edit_distance(str1[:-1],str2)
                delete = dp_table[row-1][col]
                #replace
                # replace = edit_distance(str1[:-1],str2[:-1])
                replace = dp_table[row-1][col-1]
                dp_table[row][col] = min(insert,delete,replace) + 1


    return dp_table[rows-1][cols-1]
