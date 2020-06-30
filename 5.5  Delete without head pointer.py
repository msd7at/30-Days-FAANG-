# link : https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1
def deleteNode(head):
    temp=head.next
    head.data=temp.data
    head.next=temp.next
