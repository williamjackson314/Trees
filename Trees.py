# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:36:48 2021

@author: wtjac
"""
class Node :
    
    def __init__(self, data):
        self.low = None
        self.high = None
        self.data = data
        
    def __str__(self) :
        return str(self.low.__str__()) +  str(self.data) + str(self.high.__str__())
        
    def insert(self, new_data) :
        if self.data :
            if new_data < self.data :
                if self.low is None :
                    self.low = Node(new_data)
                else :
                    self.low.insert(new_data)
            elif new_data >= self.data :
                if self.high is None :
                    self.high = Node(new_data)
                else :
                    self.high.insert(new_data)
            else :
                self.data = new_data
    
    def search(self, target) :
    
        if target == self.data or self.data is None:
            return self.data
        elif target < self.data :
            self.low.search(target)
        else :
            self.high.search(target)
        
def main():

    Binary_Tree = Node(10)
    Binary_Tree.insert(11)
    Binary_Tree.insert(12)
    Binary_Tree.insert(3)
    root = Binary_Tree.search(12)
    print(str(root))
    return 0
    
main()