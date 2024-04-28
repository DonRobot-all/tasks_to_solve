# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_node = ListNode()
        result = new_node
        temp = 0
        while l1 and l2:
            temp += l1.val + l2.val
            new_node.val = temp % 10
            temp = temp // 10       
            if l1.next and l2.next:
                new_node.next = ListNode()
                new_node = new_node.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            new_node.next = ListNode()
            new_node = new_node.next
            temp = temp + l1.val
            new_node.val = temp % 10
            temp = temp // 10
            l1 = l1.next
        while l2:
            new_node.next = ListNode()
            new_node = new_node.next
            temp = temp + l2.val
            new_node.val = temp % 10
            temp = temp // 10
            l2 = l2.next
        if temp:
            new_node.next = ListNode()
            new_node = new_node.next
            new_node.val = temp
        return result