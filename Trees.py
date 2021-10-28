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

def swap(tree, index1, index2) :
    temp = tree[index1]
    tree[index1] = tree[index2]
    tree[index2] = temp

def left(index) :
    return (2 * index + 1)

def right(index):
    return (2 * index + 2)

''' Tree Functions '''
def insert(tree, data) :
    i = 0
    while tree[i] is not None :
        if data <= tree[i] :
            i = left(i)
        elif data > tree[i] :
            i = right(i)

        if i >= len(tree) :
            add_level(tree)

    tree[i] = data

def search(tree, target):
    i = 0
    while i < len(tree) and tree[i] is not None :
        if target == tree[i] :
            return i
        elif target < tree[i] :
            i = left(i)
        else : # target > tree[i]
            i = right(i) 

    return i

def minimum(tree) :
    i = 0
    while tree[i] is not None:
        j = i
        i = left(i)

        if i >= len(tree) :
            add_level(tree)

    return tree[j]


def maximum(tree) :
    i = 0
    while tree[i] is not None :
        j = i
        i = right(i)

        if i >= len(tree) :
            add_level(tree)

    return tree[j]

def inorder(tree, node_index) :
    if node_index < len(tree) and tree[node_index] is not None :
        inorder(tree, left(node_index))
        print(tree[node_index])
        inorder(tree, right(node_index))

def preorder(tree, node_index) :
    if node_index < len(tree) and tree[node_index] is not None :
        print(tree[node_index])
        preorder(tree, left(node_index))
        preorder(tree, right(node_index))

def postorder(tree, node_index) :
    if node_index < len(tree) and tree[node_index] is not None :
        postorder(tree, left(node_index))
        postorder(tree, right(node_index))
        print(tree[node_index])

def max_heapify(tree, index) :

    key = tree[index]

    if tree[left] is not None and tree[left] > key :
        largest = left(index)
    else :
        largest = index
    if tree[right] is not None and tree[right] > tree[largest] :
        largest = right(index)
    if largest != index :
        swap(tree, index, largest)
        max_heapify(tree, largest)

def build_max_heap(tree) :
    i = (len(tree) // 2) - 1
    while tree[i] is not None :
        max_heapify(tree, i)
        i -= 1


def main() :
    selection = input("Do you want to construct a new BST and/or Max Heap? [y/n] ")
    while selection == "y" :

        files = ["test1.csv", "test2.csv", "test3.csv"]
        tree = [None]

        file_choice = input("Please select test file to use: 1, 2, or 3 ")
        while (file_choice != "1") and (file_choice != "2") and (file_choice != "3") :
            print("Invalid choice\n")
            file_choice = input("Please select test file to use: 1, 2, or 3\n")

        data = read_file(files[int(file_choice) - 1])
        for num in data[:] :
            insert(tree, num)

        print_choice = input("Do you want to print the BST? [y/n] ")
        if print_choice == "y" :
            print(tree)

        print_choice = input("Do you want to print the max and min values? [y/n] ")
        if print_choice == "y" :
            tree_max = maximum(tree)
            tree_min = minimum(tree)
            print("Tree Max = " + str(tree_max) + "\n")
            print("Tree Min = " + str(tree_min) + "\n")

        user_search = input("Enter item to search: ('q' to not search) ")
        if user_search != "q" :
            item_index = search(tree, int(user_search))
            print("Item " + user_search + " at index " + str(item_index) + "\n")

        choice = input("Print traversals? [y/n] ")
        if choice == "y" :
            print("Inorder Traversal: ")
            inorder(tree, 0)
            print('\n')

            print("Preorder Traversal: ")
            preorder(tree, 0)
            print('\n')

            print("Postorder Traversal: ")
            postorder(tree, 0)
            print('\n')

        heap_choice = input("Do you want to construct a Max Heap? [y/n] ")
        if heap_choice == "y" :
            heap = tree
            heap = build_max_heap(heap)

            print_choice = input("Do you want to print the Max Heap? [y/n] ")
            if print_choice == "y" :
                print(heap)

        selection = input("Do you want to construct a new BST and/or Max Heap? [y/n] ")

main()