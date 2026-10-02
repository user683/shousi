class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseKGroup(self, head: ListNode, K: int) -> ListNode:
        if not head or K == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        # 先数出链表的长度，判断还剩几组
        count = 0
        while curr:
            count += 1
            curr = curr.next
            
        while count >= K:
            curr = prev.next
            next_node = curr.next
            
            for _ in range(1, K):
                curr.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node
                next_node = curr.next
            
            prev = curr
            count -= K
            
        return dummy.next


def bulid_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head



if __name__ == '__main__':
    s = Solution()
    head = bulid_linked_list([1, 2, 3, 4, 5])
    K = 2
    new_head = s.reverseKGroup(head, K)
    


