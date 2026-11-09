// Last updated: 11/8/2026, 9:21:26 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current = head;
    struct ListNode* prev = NULL;

    while (current != NULL){

        struct ListNode* temp = current->next;
        current->next = prev;

        prev = current;
        current = temp;

    }

    return prev;
}