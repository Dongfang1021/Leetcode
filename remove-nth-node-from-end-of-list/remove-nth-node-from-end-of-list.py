# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            totalNoOfNodes = self.findTotalNoOfNodes(head)
            if n == totalNoOfNodes:
                x = head
                head = x.next
                del x 
                return head
            index = totalNoOfNodes - n
            self.deleteNodeAfterIndex(head, index, n)
            return head
        
    def deleteNodeAfterIndex(self, head, index, n):
        if n is 1:
            current = head
            if current.next is None:
                del current
                head = None
                return head
            else:
                while current.next.next is not None:
                    current = current.next
                current.next = None
                return head
        else:
            count = 1
            current = head
            while count < index:
                count += 1
                current = current.next
            x = current.next.next
            y = current.next
            current.next = x
            del y
            return head
    
    def findTotalNoOfNodes(self, head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count 
    
