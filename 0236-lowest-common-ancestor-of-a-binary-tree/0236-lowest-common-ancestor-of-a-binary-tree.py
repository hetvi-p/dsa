# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qq = deque()
        parents = {root: None}
        qq.append(root)
        while qq:
            node = qq.popleft()
            if node.left:
                qq.append(node.left)
                parents[node.left] = node
            if node.right:
                qq.append(node.right)
                parents[node.right] = node


        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]

        while q not in ancestors:
            q = parents[q]

        return q