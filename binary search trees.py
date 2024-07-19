class node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            if data>self.data:
                 if self.right==None:
                     self.right=node(data)
                 else:
                    self.right.insert(data)
        else:
            self.data=data
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    def minimalvalue(self,root):
        current=root
        while current.left!=None:
            current=current.left
        return current.data
    def maxvalue(self,root):
        current=root
        while current.right!=None:
            current=current.right
        return current.data
    def deleteleaf(self,root,value):
        if (root==None):
            return None
        root.left=self.deleteleaf(root.left,value)
        root.right=self.deleteleaf(root.right,value)

        if (root.data==value) & (root.left==None) & (root.right==None):
            return None
        else:
            return root
    def deletenode(self,root,value):
        if root.data>value:
            root.left=self.deletenode(root.left,value)
        elif root.data<value:
            root.right=self.deletenode(root.right,value)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right
            temp=root.right
            min=temp.data
            while temp.left:
                temp=temp.left
                min=temp.data
            root.right=self.deletenode(root.right,root.value)
        return root
            
root=node(20)
root.insert(29)
root.insert(35)
root.insert(98)
root.preorder(root)
#root.inorder(root)
#root.postorder(root)
root.deletenode(root,98)
#print(root.minimalvalue(root))
#print(root.maxvalue(root))
root.preorder(root)
