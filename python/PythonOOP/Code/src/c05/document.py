# class Document:
#     def __init__(self):
#         self.characters = []
#         self.cursor = 0
#         self.filename = ''
    
#     def insert(self, character):
#         self.characters.insert(self.cursor, character)
#         self.cursor += 1

#     def delete(self):
#         del self.characters[self.cursor]
    
#     def save(self):
#         with open(self.filename, 'w') as f:
#             f.write(''.join(self.characters))
    
#     def forward(self):
#         self.cursor += 1
    
#     def backward(self):
#         self.cursor -= 1


class Cursor:
    def __init__(self, document):
        self.document = document
        self.position = 0
    
    def forward(self):
        self.position += 1

    def backward(self):
        self.position -= 1
    
    def home(self):
        while self.document.characters[self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1


class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()
    
    def delete(self):
        del self.characters[self.cursor.position]
    
    def save(self):
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        return "".join(self.characters)


doc = Document()
doc.filename = "test_document"
doc.insert('n')
doc.insert('e')
doc.insert('v')
doc.insert('e')
doc.insert('r')
doc.insert('g')
doc.insert('i')
doc.insert('v')
doc.insert('e')
doc.insert('u')
doc.insert('p')
print(doc.string)
print(doc.__dict__)
