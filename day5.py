class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def user_logic(head):
    digits = ""

    temp=head
    while temp:
        digits += str(temp.val)
        temp = temp.next
    
    num = int(digits)
    rev_num = int(str(num)[::-1])
    num_sum = sum(int(d) for d in str(rev_num))
    result = rev_num - num_sum

    return "even" if result%2 == 0 else "false"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # Read the size of the linked list
    nodes = list(map(int, data[1:N+1]))  # Read the linked list nodes
    
    # Create the linked list from input
    head = None
    tail = None
    
    for digit in nodes:
        newNode = ListNode(digit)
        if not head:
            head = newNode  # Initialize the head if the list is empty
        else:
            tail.next = newNode  # Link the new node to the list
        tail = newNode  # Update the tail to the new node
    
    # Call user logic function and print the output
    result = user_logic(head)
    print(result)

if __name__ == "__main__":
    main()