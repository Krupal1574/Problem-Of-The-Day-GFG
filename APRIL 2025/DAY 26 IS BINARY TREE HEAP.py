#User Template for python3

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Helper function to count total nodes in the tree
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    # Helper function to check completeness
    def isComplete(self, root, index, total_nodes):
        if root is None:
            return True
        if index >= total_nodes:  # If current index exceeds total nodes, it's not complete
            return False
        # Recursively check left and right subtrees
        return (self.isComplete(root.left, 2 * index + 1, total_nodes) and
                self.isComplete(root.right, 2 * index + 2, total_nodes))
    
    # Helper function to check max-heap property
    def isMaxHeap(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:  # Leaf node
            return True
        if root.right is None:  # Only left child exists
            return root.data >= root.left.data
        # Both children exist
        return (root.data >= root.left.data and
                root.data >= root.right.data and
                self.isMaxHeap(root.left) and
                self.isMaxHeap(root.right))
    
    # Main function to check if the tree is a max-heap
    def isHeap(self, root):
        total_nodes = self.countNodes(root)  # Count total nodes in the tree
        # Check completeness and max-heap property
        return self.isComplete(root, 0, total_nodes) and self.isMaxHeap(root)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Contributed by Susanta Mukherjee
import sys

sys.setrecursionlimit(10**6)
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    #Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        root = buildTree(input())
        ob = Solution()
        if ob.isHeap(root):
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends