class Node:
    def __init__(self, data):
        self.data = data
        

class Solution:
    def reverse(self, start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reverseKGroup(self, head, k):
        count, temp = 0, head
        while temp and count < k:
            temp = temp.next
            count += 1
        if count < k:
            return head

        new_head = self.reverse(head, temp)
        head.next = self.reverseKGroup(temp, k)
        return new_head

def createLinkedList(arr):
    head = None
    temp = None
    for data in arr:
        newNode = Node(data)
        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            temp = temp.next
    return head

def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
k = 3
head = createLinkedList(arr)
sol = Solution()
new_head = sol.reverse
