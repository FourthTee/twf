import networkx as nx
import math

items_weights = [3, 2, 8, 12, 25, 15, .5, 1, 2]

def createGraph():

    G = nx.Graph()
    
    #Add the nodes to the graph 0 is L1, 1 is C1, 2 is C2, and 3 is C3
    G.add_nodes_from([0, 1, 2, 3])

    #Add edges
    G.add_edge(1, 2, weight= 4)
    G.add_edge(1, 0, weight= 3)
    G.add_edge(0, 2, weight= 2.5)
    G.add_edge(0, 3, weight= 2)
    G.add_edge(2, 3, weight= 3)


    return G


def solve(potentialStart, items):
    min_cost = 1000000000
    G = createGraph()
    if (len(potentialStart) == 1):
        for start in potentialStart:
            paths = nx.all_simple_paths(G, source=start, target=0)
            for path in map(nx.utils.pairwise, paths):
                path_cost = cost(G, path, items, start)
                if path_cost < min_cost:
                    min_cost = path_cost
    if (len(potentialStart) == 2):
        first = potentialStart[0]
        second = potentialStart[1]
        
        #Start at first
        first_paths = nx.all_simple_paths(G, source=first, target=0)
        for path in first_paths:
            if second not in path:
                #need to add 0 to second to 0
                path_tuple = nx.utils.pairwise(path)
                path_cost = cost(G, path_tuple, items, first)

                #cost to go from 0 to second
                edge_weight = G.get_edge_data(0, second)
                path_cost += 10 * edge_weight['weight']

                #cost from second back to 0
                aug_path = []
                aug_path.append(tuple((second, 0)))
                c = cost(G, aug_path, items, second)
                path_cost += c
                if path_cost < min_cost:
                    min_cost = path_cost

            else:
                path_tuple = nx.utils.pairwise(path)
                path_cost = cost(G, path_tuple, items, first)
                if path_cost < min_cost:
                    min_cost = path_cost
        
        #Start at Second
        second_paths = nx.all_simple_paths(G, source=second, target=0)
        for path in second_paths:
            if first not in path:
                #need to add 0 to second to 0
                path_tuple = nx.utils.pairwise(path)
                path_cost = cost(G, path_tuple, items, second)

                #cost to go from 0 to second
                edge_weight = G.get_edge_data(0, first)
                path_cost += 10 * edge_weight['weight']

                #cost from second back to 0
                aug_path = []
                aug_path.append(tuple((first, 0)))
                path_cost += cost(G, aug_path, items, first)
                if path_cost < min_cost:
                    min_cost = path_cost

            else:
                path_tuple = nx.utils.pairwise(path)
                path_cost = cost(G, path_tuple, items, second)
                if path_cost < min_cost:
                    min_cost = path_cost

    if len(potentialStart) == 3:

        #Start at 1
        first_paths = []
        first_paths.append([1, 0, 2, 0, 3, 0])
        first_paths.append([1, 0, 2, 3, 0])
        first_paths.append([1, 0, 3, 2, 0])
        first_paths.append([1, 2, 3, 0])
        first_paths.append([1, 2, 0, 3, 0])
        
        for path in first_paths:
            first_tuple = nx.utils.pairwise(path)
            path_cost = cost(G, first_tuple, items, 1)
            if path_cost < min_cost:
                    min_cost = path_cost



        #Start at 2
        second_paths = []
        second_paths.append([2, 0, 1, 0, 3, 0])
        second_paths.append([2, 1, 0, 3, 0])
        second_paths.append([2, 3, 0, 1, 0])

        for path in second_paths:
            second_tuple = nx.utils.pairwise(path)
            path_cost = cost(G, second_tuple, items, 1)
            if path_cost < min_cost:
                    min_cost = path_cost


        #Start at 3
        third_paths = []
        third_paths.append([3, 0, 2, 0, 1, 0])
        third_paths.append([3, 0, 2, 1, 0])
        third_paths.append([3, 0, 1, 2, 0])
        third_paths.append([3, 2, 1, 0])
        third_paths.append([3, 2, 0, 1, 0])

        for path in first_paths:
            third_tuple = nx.utils.pairwise(path)
            path_cost = cost(G, third_tuple, items, 1)
            if path_cost < min_cost:
                    min_cost = path_cost
    
    return int(min_cost)


def cost(G, path, items, start):

    cost = 0
    itemWeight = 0
    #print(path)
    for edge in list(path):
        v1 = edge[0]
        v2 = edge[1]
        itemWeight += find_weight(items, v1)
        if v1 == 0:
            itemWeight = 0
        edge_weight = G.get_edge_data(v1, v2)
        if itemWeight <= 5:
            cost += 10 * edge_weight['weight']
        else:
            additional = math.ceil((itemWeight - 5) / 5) * 8
            cost = cost + (10 + additional)*edge_weight['weight']
        #print(cost)
    return cost



def find_weight(items, location):

    weight = 0
    if location == 1:
        for i in range(0, 3):
            weight += items[i] * items_weights[i]

    if location == 2:
        for i in range(3, 6):
                weight += items[i] * items_weights[i]

    if location == 3:
        for i in range(6, 9):
                weight += items[i] * items_weights[i]
    
    return weight
    

def api_solve(string_inp):
    lst = list(string_inp.split(" "))
    lst = list(map(int, lst))
    
    set1 = lst[0:3]
    set2 = lst[3:6]
    set3 = lst[6:]

    potenStart = []

    if any(set1):
        potenStart.append(1)
    
    if any(set2):
        potenStart.append(2)
    
    if any(set3):
        potenStart.append(3)

    min_cost = solve(potenStart, lst)

    return min_cost


#main function

if __name__ == '__main__':
        
    lst = [] 
    
    print("Input the amount of each item: ")
    inp = input()
    try:
        lst = list(inp.split(" "))
        assert len(lst) == 9
    except AssertionError:
        print("Wrong Input Format")
        quit()

    lst = list(map(int, lst))
    
    set1 = lst[0:3]
    set2 = lst[3:6]
    set3 = lst[6:]

    potenStart = []

    if any(set1):
        potenStart.append(1)
    
    if any(set2):
        potenStart.append(2)
    
    if any(set3):
        potenStart.append(3)

    min_cost = solve(potenStart, lst)

    print("Min Cost: "+ str(min_cost))

