**Required Libraries**
- csv : to read in the csv file with the data to binary tree-ize.
- math : to find the number of levels of the tree from the length of the list.

**Support Functions**
- read_file : read data from csv file, convert to list of integers, return this list.
- add_level : Add a level of None type elements to the tree. Used when the index to insert a new element is out of the range of the binary search tree list.
- swap : swap two items in a list.
- left : find the index of the left child of the current node.
- right : find the index of the right child of the current node.

**Binary Search Tree (BST)**
- Binary Search Tree property states that a current node will be larger than its left child and smaller than
its right child
- Constructs a list that follows the Binary Search Tree property using data from csv. The functions Insert, Search, Minimum,
and Maximum are supported.

**Tree Functions** :

insert :
- Insert the specified item into the binary tree in the proper place.
- When an item already in the tree is passed to insert, the function places it in the left subtree of the node it equals.
- Uses the add_level() support function when inserting into a new level.

search :
- Search through the binary tree and return the index of the target item.

minimum :
- Find the smallest value item in the binary tree.
- Does this by iteratively calling the left() support function until a 'None' valued child is found.

maximum :
- Find the largest value item in the binary tree.
- Does this by iteratively calling the right() support function until a 'None' valued child is found.

**Traversals** :

inorder :
- Prints out nodes in left, middle, right order.

preorder :
- Prints out nodes in middle, left, right order.

postorder :
- Prints out nodes in left, right, middle order.


**Max Heaps**
- The Max Heap property states that the current node will be larger than its left and right children
- Constructs a list that follows the Max Heap property using data from a csv. Max Heapify and Build Max Heap functions are supported.

**Max Heap Functions** :

max_heapify :
- Make the current node follow the max heap property.
- If current node not larger than both its children, swap it with its largest child

build_max_heap :
- Construct a Max Heap from a list
- Iteratively calls max_heapify to rearrange list to follow the Max Heap property

**Main**

main :
- Read in csv data.
- Read in data from the csv file requested by the user
- Ask the user if they want to construct a BST, print BST, and print out specific values for the BST
- Ask the user if they want to construct a Max Heap, print Max Heap
- Repeat until they say no when asked to construct a new BST and/or Max Heap
