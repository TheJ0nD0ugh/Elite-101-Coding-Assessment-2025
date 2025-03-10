# This code is a STARTER scaffold for the E101 Coding assessment
"""
This coding assignment was coded on CodeHS as it is much easier for me to use
as it has a built in docs(you can find it here: 
https://codehs.com/documentation/new/python3 ) and in general is just something
I am much more used to in comparison to Github Codespaces. 
"""

def get_free_tables(tables):
    """
    Level 1
    Returns a list of table IDs (or entire objects) that are currently free.
    """
    # TODO: Implement your logic here
    """
    First I want to figure out exactly how to check how to find out if occupied
    is equal to True for each seperate table. After this, I will make a list of "Free tables" that can have all of the tables that don't return 'occupied' as True. Next I wlil use a while loop rather than a if loop just so I can keep track of the i a lot easier if I need to debug later. After that I 
    need to append the table id(the project does not say anything about saying 
    something like "Table 1 is free" or "Table 4 is occupied")and I will return the 
    list of free tables. 
    """
    # HINT: Loop through each 'table' dict, check 'occupied' status.
    #       If table["occupied"] is False, it is free.
    #       Append table["table_id"] (or the entire table dict) to the result list.
    free_tables = []
    i = 0
    while True:
        if tables_data[i]['occupied'] == False:
            free_tables.append(tables[i]["table_id"])
            i += 1
            if i >= len(tables):
                break
        else:
            i += 1
            if i >= len(tables):
                break
    return free_tables

def find_one_table_for_size(tables, party_size):
    """
    Level 2
    Returns the first table ID that can seat 'party_size' and is free,
    or None if none found.
    """
    # TODO: Implement your logic here
    """
    The very first thing I will do is create the i variable so my While loop will stop as well as so I can go through the whole dictionary.
    Next, I will be checking if the tables_data['occupied'] == false similarly to Level 1, but instead I will use another if statment after
    so I can check if the table size is more than or equal to the party size. If either of the if statements are not true, it will just add
    1 to 'i', but if both of them are true, it will return the table id 
    """
    # HINT: Loop through tables and check two conditions:
    #       1) table["occupied"] == False
    #       2) table["capacity"] >= party_size
    #       Return the table_id of the first match you find, otherwise return None.
    i = 0
    while True:
        if tables_data[i]['occupied'] == False:
            if tables_data[i]['capacity'] >= party_size:
                return tables_data[i]["table_id"]
            else:
                i += 1
        else:
            i+= 1


def find_all_tables_for_size(tables, party_size):
    """
    Level 3
    Returns a list of all table IDs that can seat 'party_size' and are free.
    """
    # TODO: Implement your logic here
    """
    Very similarly to Level 3, I will just add all of the matching tables to
    a list and then return the list. My thought process for the rest of the 
    level basically the exact same as level 2, but with a few more if-statements
    """
    # HINT: Similar to Level 2, but collect ALL matching tables instead of stopping at the first.
    all_combinations_for_size = []
    i = 0
    while True:
        if tables_data[i]['occupied'] == False:
            if tables_data[i]['capacity'] >= party_size:
                all_tables_for_size.append(tables[i]["table_id"])
                i += 1
                if i >= len(tables):
                    break
            else:
                i += 1
                if i >= len(tables):
                    break
        else:
            i+= 1
            if i >= len(tables):
                break
    return all_tables_for_size


def find_tables_including_combos(tables, party_size):
    """
    Level 4
    Returns a list of table or table combinations that can seat 'party_size'.
    Adjacent combos are determined via the table's "neighbors" list.
    
    Example output structure:
    [(1,), (3,), (1,2), (3,5)]  # Each tuple is a single table or a pair.
    """
    # TODO: Implement your logic here
    """
    I first want to take the while loop from level 3 and modify the second
    if-statement to make it so it can borrow the capacity from tables one lower 
    than it or one higher than it. Next I have to add a system to make sure the
    table above or below it actually equal to party size and then from there I 
    want to make sure the table actually exists and I don't have a non-existent 
    table trying to add itself. I will do this by making sure the first or last
    table don't try to add the capacity of its lower/upper table. NOT COMPLETE
    """
    # HINT: 
    #  1) If a single table has enough capacity, add (table_id,) to your results.
    #  2) Otherwise, try pairing with each of its neighbors (if they're free)
    #     and check combined capacity.
    #  3) Sort or otherwise avoid duplicate combos, e.g. (1,2) vs (2,1).
    """ 
    All of this is what I started coding but I couldn't figure it out after 
    around 2 hours so I stopped and decided to just turn in up to level 3(I still
    have my thought process and SOME of the code for level 4)
    all_tables_for_size = []
    all_tables_for_size2 = []
    i = 0
    is_Beginning = False #this is to determine if the table is the first in the dictionary
    is_End = False #this is to determine if the table is the last in the dictionary
    while True:
        if tables_data[i]['occupied'] == False:
            if tables_data[i]["table_id"] == 1 
                is_Beginning = True
            elif tables_data[i]["Table_id"] == 4:
                is_End = True
            if tables_data[i]['capacity'] == party_size:
                all_combinations_for_size.append(tables[i]["table_id"])
                i += 1
                if i >= len(tables):
                    break
            elif is_end == False:
                if tables_data[i - 1]['capacity'] + tables_data[i]['capacity'] == party_size:
                    all_combinations_for_size.append()
            else:
                i += 1
                if i >= len(tables):
                    break
        else:
            i+= 1
            if i >= len(tables):
                break
    return all_tables_for_size
    """
def friendly_output(tables, combos):
    """
    Bonus (Optional):
    Takes the combos from Level 4 (like [(1,), (2,), (1,2)]) and
    prints a more user-friendly message about each result.
    """
    # TODO: Implement your logic here (optional)
    # HINT: 
    #  1) For single-table tuples (like (1,)), find that table's capacity and print a message.
    #  2) For pairs, combine their capacities and print a message about the total.
    pass


# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # This example data shows how a list of dictionaries might look.
    # You can modify or replace it with your own tests.
    tables_data = [
        {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
        {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
        {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]
    # LEVEL 1
    print("LEVEL 1: Free Tables =", get_free_tables(tables_data))

    # LEVEL 2
    print("LEVEL 2: One table for party size 2 =", find_one_table_for_size(tables_data, 2))

    # LEVEL 3
    print("LEVEL 3: All tables for party size 2 =", find_all_tables_for_size(tables_data, 2))

    # LEVEL 4
    combos = find_tables_including_combos(tables_data, 5)
    print("LEVEL 4: Single or combined tables for party size 5 =", combos)

    # BONUS
    print("\nBONUS: Friendly output for the combos above")
    friendly_output(tables_data, combos)