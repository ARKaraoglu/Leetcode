# @leet start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # pointerOne = 0
        # pointerTwo = 0
        # print(list1.val)
        # print(list2.val)
        # totalLength = len(list1) + len(list2)
        # mergedList = []
        # for x in range(0, totalLength - 1):
        #     if list1[pointerOne] < list2[pointerTwo]:
        #         mergedList.append(list1[pointerOne])
        #         pointerOne += 1
        #     elif list1[pointerOne] > list2[pointerTwo]:
        #         mergedList.append(list2[pointerTwo])
        #         pointerTwo += 1
        # return mergedList
        headOne = list1
        headTwo = list2
        mergedLinkedLists = Node(0)
        pointer = mergedLinkedLists

        while headOne and headTwo:
            if headOne.val < headTwo.val:
                pointer.next = headOne
                headOne = headOne.next
            else:
                pointer.next = headTwo
                headTwo = headTwo.next
            pointer = pointer.next

        if headOne:
            while headOne:
                pointer.next = headOne
                headOne = headOne.next
                pointer = pointer.next
        elif headTwo:
            while headTwo:
                pointer.next = headTwo
                headTwo = headTwo.next
                pointer = pointer.next
        
        return mergedLinkedLists.next
# @leet end 
