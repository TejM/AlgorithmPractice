# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_nodes = []
        current = head
        while current != None:
            list_nodes.append(current)
            current = current.next
        return list_nodes[len(list_nodes)//2]
