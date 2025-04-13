# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()

        if root is None:
            return []

        final_res = []

        queue.append(root)

        while(queue):

            int_res = []

            k = len(queue)

            for i in range(k):

                node = queue.popleft()

                int_res.append(node.val)


                if (node.left!=None):
                    queue.append(node.left)
                if(node.right!=None):
                    queue.append(node.right)

            final_res.append(int_res)

        return final_res




