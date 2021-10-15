**Required Libraries**
- csv : to read in the csv file with the data to binary tree-ize
- math : to find the number of levels of the tree from the length of the list

**Support Functions**
- read_file : read data from csv file, convert to list of integers, return this list
- add_level : Add a level of None type elements to the tree. Used when the index to insert a new element is out of
                the range of the binary search tree list

**Binary Search Tree**

Implement Binary Search Tree data structure using an list. The functions Insert, Search, Minimum, 
and Maximum are supported.

**Tree Functions** :

Insert :
- Insert specified item into the binary tree in the proper place.

Search :
- Search through the binary tree and return the index of the target item.

Minimum :
- Find the smallest value item in the binary tree.

Maximum :
- Find the largest value item in the binary tree.

Main :
- Read in csv data
- Create the tree list with one None type element as the root
- Iterate through the csv data and call Insert to insert each data point into the tree
