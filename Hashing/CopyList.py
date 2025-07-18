#  C++

RandomListNode* Solution::copyRandomList(RandomListNode* A) {
    if (!A)
        return NULL;
    
    RandomListNode* head = A;
    
    while (A)
    {
        RandomListNode* copyA = new RandomListNode(A->label);
        copyA->next = A->next;
        A->next = copyA;
        A = copyA->next;
    }
    A = head;
    
    while (A)
    {
        if (!A->random)             // I missed this check.
            A->next->random = NULL;
        else
            A->next->random = A->random->next;
            
        A = A->next->next;
    }
    A = head;
    
    RandomListNode* copy = A->next;
    RandomListNode* copyHead = A->next;
    
    while (A)
    {
        A->next = A->next->next;
        A = A->next;
        if (!copy->next)            // I missed this check.
            break;
        copy->next = copy->next->next;
        copy = copy->next;
    }
    
    return copyHead;
}






# PYTHON3



class RandomListNode:
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Interweave original and copied nodes
        curr = head
        while curr:
            copy = RandomListNode(curr.label)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers to copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the copied list from the original
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next

        return copy_head




#   JAVA




/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;

        // Step 1: Interleave original and copied nodes
        RandomListNode curr = head;
        while (curr != null) {
            RandomListNode copy = new RandomListNode(curr.label);
            copy.next = curr.next;
            curr.next = copy;
            curr = copy.next;
        }

        // Step 2: Assign random pointers
        curr = head;
        while (curr != null) {
            if (curr.random != null) {
                curr.next.random = curr.random.next;
            }
            curr = curr.next.next;
        }

        // Step 3: Separate the copied list from the original
        curr = head;
        RandomListNode pseudoHead = head.next;
        while (curr != null) {
            RandomListNode copy = curr.next;
            curr.next = copy.next;
            if (copy.next != null) {
                copy.next = copy.next.next;
            }
            curr = curr.next;
        }

        return pseudoHead;
    }
}






















