import csv
import math

''' Support Functions '''    
def read_file(file_name) :

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    data = [int(x[0]) for x in data[:]]
    return data

def add_level(tree) :
    levels = math.floor(math.log(len(tree), 2) + 1)
    for num in range(0, 2**levels) :
        tree.append(None)

''' Tree Functions '''
def insert(tree, data) :
    i = 0
    while tree[i] is not None :
        if data <= tree[i] :
            i = (2 * i) + 1
        elif data > tree[i] :
            i = (2 * i) + 2 

        if i >= len(tree) :
            add_level(tree)

    tree[i] = data

def search(tree, target):
    i = 0
    while i < len(tree) and tree[i] is not None :
        if target == tree[i] :
            return i
        elif target < tree[i] :
            i = (2 * i) + 1
        else : # target > tree[i]
            i = (2 * i) + 2 

    return i

def maximum(tree) :
    i = 0
    while tree[i] is not None :
        j = i
        i = (2 * i) + 2

        if i >= len(tree) :
            add_level(tree)

    return tree[j]

def minimum(tree) :
    i = 0
    while tree[i] is not None:
        j = i
        i = (2 * i) + 1

        if i >= len(tree) :
            add_level(tree)

    return tree[j]

def inorder(tree, node_index) :
    if tree[node_index] is not None :
        inorder(tree, node_index * 2 + 1)
        print(tree[node_index])
        inorder(tree, node_index * 2 + 2)

def preorder(tree, node_index) :
    if tree[node_index] is not None :
        print(tree[node_index])
        preorder(tree, node_index * 2 + 1)
        preorder(tree, node_index * 2 + 2)

def postorder(tree, node_index) :
    if tree[node_index] is not None :
        postorder(tree, node_index * 2 + 1)
        postorder(tree, node_index * 2 + 2)
        print(tree[node_index])



def main() :
    data = read_file("test1.csv")
    tree = [50,25,75,10,40,60,90, None, None, None, None, None, None, None, None]
    # for num in data[:] :
    #     insert(tree, num)
    return 0

main()