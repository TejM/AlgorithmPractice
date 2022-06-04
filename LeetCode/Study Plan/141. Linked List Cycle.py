class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        while head is not None:
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
        return False

# Time complexity : O(N)
# Space complexity : O(N)
