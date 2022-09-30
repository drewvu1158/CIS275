class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Contact_list:
    def __init__(self):
        self.head = None

    def add(self, name, number):
        probe = self.head
        new_node = contact(name, number)
        if probe == None:
            self.head = node(new_node, self.head)
        elif probe.data.name > name:
            self.head = node(new_node, self.head)
        else:
            while probe.next != None and probe.next.data.name < name:
                probe = probe.next
            probe.next = node(new_node, probe.next)

        
        return self.head

            


    def __str__(self):
        string = self.head
        return_str = ""
        while string is not None:
            return_str += (string.data.name + ", " + string.data.phone + "\n")
            if string.next is not None:
                string = string.next
            else:
                break

        return return_str
        
    def remove_name(self, name):
        probe = self.head
        if probe.data.name == name:
            self.head = probe.next
        else:
            while probe.next != None and probe.next.data.name != name:
                probe = probe.next
            if probe.next != None:
                probe.next = probe.next.next
        return self.head

    def change_phone_number(self, name, number):
        probe = self.head
        if probe.data.name == name:
            probe.data.phone = number
        else:
            while probe.next != None and probe.next.data.name != name:
                probe = probe.next
            if probe.next != None:
                probe.next.data.phone = number
        return self.head

