# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = self.size(head)
        for i in range(1, math.ceil(l/2)):
            removed, head = self.yoink(l-1, head)
            head = self.insertAt((i*2)-1, head, removed)
        

    def size(self, head: Optional[ListNode]) -> int:
        curr = head
        i=0
        while curr != None:
            i+=1
            curr = curr.next
        return i

    # returns newHead
    # head &node must not be None
    def insertAt(self, i: int, head: ListNode, node: ListNode)-> ListNode:
        if i == 0:
            node.next = head
            return node
        curr = head
        while i > 0:
            prev = curr
            curr = curr.next
            i-=1
        prev.next = node
        node.next = curr
        return head

    # returns (removed, newHead)
    # i must not exceed size of the list, head & node must not be None
    def yoink(self, i: int, head: ListNode) -> tuple[ListNode, ListNode]:
        ret = None
        if i == 0:
            return (head, head.next)
        curr = head
        while i > 0:
            prev = curr
            curr = curr.next
            i-=1
        ret = curr
        prev.next = curr.next
        return (ret, head)