# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return "*"

        q = deque([root])
        
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.extend([node.left, node.right])
            else:
                res.append("*")
        
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        if vals[0] == "*":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])

        i = 1
        while q:
            node = q.popleft()

            if vals[i] != "*":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "*":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

