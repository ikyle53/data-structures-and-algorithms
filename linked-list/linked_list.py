# Domain -----------------------------------------------------------------------------
# [ X ] Create a linked list class
# [ x ] Include a head property
# [ x ] Upon instantiation an empty linked list should be created

# Methods
# [ x ] insert(value) - adds a new node with that value to the head of the list with an O(1).
# [  ] includes(value) - Boolean/loop | indicates whether that value exists as a Node’s value somewhere
# within the list.
# [  ] to_string() - Returns a string representing all the values in the linked list formatted as:
#                       .format("{ a } -> { b } -> { c } -> NULL")
# Domain -----------------------------------------------------------------------------


##################### Node class #####################


class Node(object):
    """
    This node class constructs a node as part of a
    linked list. The constructor creates data and
    creates the address for the next node. As a
    linked list the HEAD is going to be fixed memory
    whereas the rest of the nodes will have static
    memory and be assigned to whatever is available.
    """

    ################ Constructor ######################
    """
    The node's instance of self creates data assigned
    to that node. The same instance also supplies an 
    address to the next node in line (if there is one)
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    ###################################################


##################### Linked list #####################


class linked_list(object):
    def __init__(self, head=None):
        self.head = head

    def get_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def print_list(self):
        header.head = Node("a")
        a = Node("b")
        b = Node("c")
        some_data = self.head
        while some_data:
            print("{{{}}} -> {{{}}} -> {{{}}} -> NULL".format(header.head.data, a.data, b.data), end='')
            some_data = some_data.next_node
        print("")

    def insert_node_at_head(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def get_next_node(self, node):
        return node.next_node.data


if __name__ == "__main__":
    header = linked_list()

    header.head = Node("a")
    a = Node("b")
    b = Node("c")
    header.head.next_node = a
    a.next_node = b
    header.print_list()
    # print(header.get_size())
    # header.insert_node_at_head()
