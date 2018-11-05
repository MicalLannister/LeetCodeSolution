# coding=utf-8

# createLinkedList by array


class ListNode:
    """docstring for ListNode"""

    def __init__(self, x):
        self.val = x
        self.next = None


def delete(node):
    node.val = node.next.val
    node.next = node.next.next


def createLinkedList(array):
    preNode = None
    headNode = None
    for i in array:
        if preNode:
            preNode.next = ListNode(i)
            preNode = preNode.next
        else:
            preNode = ListNode(i)
            head = preNode
    return head


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    curNode = dummy
    preNode = dummy
    for x in range(n):
        curNode = curNode.next
        print(curNode.val)
    while curNode.next:
        curNode = curNode.next
        preNode = preNode.next
    preNode.val = preNode.next.val
    preNode.next = preNode.next.next
    return dummy.next


def reverseList(head):
    currentHead = head
    newHead = None
    while currentHead:
        tmp = currentHead.next
        currentHead.next = newHead
        newHead = currentHead
        currentHead = tmp
    return newHead


def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    newHead = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            newHead.next = l1
            newHead = l1
            l1 = l1.next
        else:
            newHead.next = l2
            newHead = l2
            l2 = l2.next
    if l1:
        newHead.next = l1
    if l2:
        newHead.next = l2
    return dummy.next


def isPalindrome(head):
    fast = head
    slow = head
    tmp = []
    while fast and fast.next:
        fast = fast.next.next
        tmp.append(slow.val)
        slow = slow.next
    if fast:
        slow = slow.next
    for x in range(-1, -len(tmp) - 1, -1):
        if tmp[x] != slow.val:
            return False
        slow = slow.next
    return True


def hasCycle(head):
    if not head or not head.next:
        return False
    fast = head.next
    slow = head
    while fast.val != slow.val:
        if not fast.next:
            return False
        fast = fast.next
        slow = slow.next
        if not fast or not fast.next:
            return False
    return True


if __name__ == '__main__':
    head = createLinkedList([1, 2, 2, 1])
    print(isPalindrome(head))
    print('---------------')
