



'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val
        
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

# 双指正针写法
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre