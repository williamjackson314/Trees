def set_root(tree, data) :
    if tree[0] is None :
        tree[0] = data
    else :
        return 0

def insert(tree, data) :
    return 0

def search(tree, target):
    i = 0
    while i < len(tree) :
        if target == tree[i] :
            return i
        elif target < tree[i] :
            i = (2 * i) + 1
        else : # target > trees[i]
            i = (2 * i) + 2
    
    return None

def remove(tree, data) :
    i = search(tree, data)
    '''
    while i < len(tree) - 1 :
        tree[i] = tree[i + 1]
        i += 1
    tree.pop()
    '''
    print(tree)

def maximum(tree) :
    i = 0
    while i < len(tree) and tree[i] is not None :
        j = i
        i = (2 * i) + 2
    
    return j

def minimum(tree) :
    i = 0
    while i < len(tree) and tree[i] is not None:
        j = i
        i = (2 * i) + 1
    
    return j

def main() :
    tree = [13, None, 16, None, None, 14, 18]
    print(str(minimum(tree)))
    return 0

main()