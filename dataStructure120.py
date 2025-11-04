#120.Work with sets to remove duplicates from nested structures

data=[[1,2],
      [1,2],
      [1,2],
      [3,2],
      [4,4],
      [2,2],
    ]
def filter_list_data(data):
    for row_index in range(len(data)):
        data[row_index]=tuple(data[row_index])
    
    print(list(set(tuple(data))))

dict_data = [
    {"id": 1, "name": "Alice", "skills": ["Python", "SQL"]},
    {"id": 2, "name": "Bob", "skills": ["Java", "C++"]},
    {"id": 1, "name": "Alice", "skills": ["Python", "SQL"]},  # duplicate
    {"id": 3, "name": "Charlie", "skills": ["Python", "Go"]},
    {"id": 2, "name": "Bob", "skills": ["Java", "C++"]}       # duplicate
]

def filter_list_of_dict(dict_data):
    # Step 1: change "skills" lists into tuples (so they can go into a set)
    for i in range(len(dict_data)):
        if isinstance(dict_data[i]["skills"], list):
            dict_data[i]["skills"] = tuple(dict_data[i]["skills"])

    # Step 2: turn each dictionary into a frozenset of its items
    frozen_list = []
    for i in range(len(dict_data)):
        frozen_list.append(frozenset(dict_data[i].items()))

    # Step 3: put them into a set to remove duplicates
    unique_frozen = set(frozen_list)

    # Step 4: convert back into dictionaries
    unique_dicts = []
    for item in unique_frozen:
        d = dict(item)
        # change "skills" back into a list for readability
        if isinstance(d["skills"], tuple):
            d["skills"] = list(d["skills"])
        unique_dicts.append(d)

    return unique_dicts




print(filter_list_of_dict(dict_data))

