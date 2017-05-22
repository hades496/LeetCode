class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur and count < k:
            count += 1
            cur = cur.next
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count > 0:
                count -= 1
                next = head.next
                head.next = cur
                cur = head
                head = next
            head = cur
        return head
