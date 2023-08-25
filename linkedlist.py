class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def take_linked_list_input():
    values = list(
        map(int, input("Enter values separated by spaces: ").split()))
    head = None
    tail = None
    for value in values:
        new_node = ListNode(value)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

head = take_linked_list_input()

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result

linked_list_as_list = linked_list_to_list(head)

print(linked_list_as_list[::-1])
