# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        slow = head
        fast = head 

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next 

        
        list1 = head
        list2 = slow.next
        slow.next = None


        previous = None 
        current = list2 

        while current:
            next_node = current.next
            current.next = previous 

            previous = current 
            current = next_node

        list2 = previous

        while list1 and list2:
            
            next1 = list1.next 
            list1.next = list2
            next2 = list2.next 
            list2.next = next1

            list1 = next1
            list2 = next2
        
            




