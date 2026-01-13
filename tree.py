class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def insert(root,val):
    if root is None:
        return node(val)
    else:
        if val<root.val:
            root.left=insert(root.left,val)
        else:
            root.right=insert(root.right,val)
        return root
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
        
def preorder(root):
    if root:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)
        
def postorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.val,end=" ")
        
root=None
vals=[10,50,30,60,20,40]

for v in vals:
    root=insert(root,v)
    
print("INORDER")
inorder(root)
print("\nPREORDER")
preorder(root)
print("\nPOSTORDER")
postorder(root)
