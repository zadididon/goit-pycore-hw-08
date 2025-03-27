from graphviz import Digraph

# Create a new directed graph
uml = Digraph('UML_Diagram', filename='personal_assistant_uml', format='png')

# Define class nodes
uml.node('Field', '''Field
-----------------
- value: str
-----------------
+ __init__(value: str)
+ __str__(): str''', shape='record')

uml.node('Name', '''Name
-----------------
(inherits from Field)''', shape='record')

uml.node('Phone', '''Phone
-----------------
(inherits from Field)
-----------------
+ __init__(value: str)''', shape='record')

uml.node('Birthday', '''Birthday
-----------------
(inherits from Field)
-----------------
+ __init__(value: str)''', shape='record')

uml.node('Record', '''Record
-----------------
- name: Name
- phones: list[Phone]
- birthday: Birthday (optional)
-----------------
+ __init__(name: str)
+ add_phone(phone: str)
+ remove_phone(phone: str)
+ edit_phone(old: str, new: str)
+ find_phone(phone: str): Phone
+ add_birthday(birthday: str)
+ __str__(): str''', shape='record')

uml.node('AddressBook', '''AddressBook
-----------------
(inherits from UserDict)
-----------------
+ add_record(record: Record)
+ find(name: str): Record
+ delete(name: str)
+ birthdays(): list[dict]''', shape='record')

# Define relationships
uml.edge('Name', 'Field', arrowhead='empty')  # Inheritance
uml.edge('Phone', 'Field', arrowhead='empty')  # Inheritance
uml.edge('Birthday', 'Field', arrowhead='empty')  # Inheritance
uml.edge('Record', 'Name', label='- name', arrowhead='diamond')  # Composition
uml.edge('Record', 'Phone', label='- phones (list)', arrowhead='diamond')  # Composition
uml.edge('Record', 'Birthday', label='- birthday (optional)', arrowhead='diamond')  # Composition
uml.edge('AddressBook', 'Record', label='- records (dict)', arrowhead='diamond')  # Composition

# Render UML diagram
uml_path = '/mnt/data/personal_assistant_uml.png'
uml.render(uml_path, format='png', cleanup=True)

uml_path
