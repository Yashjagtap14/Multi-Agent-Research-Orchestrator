class Memory:
    def __init__(self):
        self.documents = []

    def add(self, text):
        self.documents.append(text)

    def search(self, query, k=3):
        return self.documents[:k]

