from collections import defaultdict

def find_town_chief(trust):
    n = len(trust)
    graph = defaultdict(list)

    for i in range(n):
        ai, bi = trust[i]
        graph[ai].append(bi)

    town_chief_candidate = -1

    for person in range(1, n + 1):
        if not graph[person]:
            if town_chief_candidate == -1:
                town_chief_candidate = person
            else:
                
                return -1
    
    for person in range(1, n + 1):
        if person != town_chief_candidate and town_chief_candidate not in graph[person]:
            return -1

    return town_chief_candidate

trust = [[1, 3], [2, 3], [3, 4], [4, 1], [2, 5], [5, 2]]
town_chief = find_town_chief(trust)

if town_chief != -1:
    print(f"The town chief is person {town_chief}.")
else:
    print("There is no town chief in the given scenario.")
