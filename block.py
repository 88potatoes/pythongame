class Block:
    def __iter__(self, tup):
        self.x, self.y, self.width, self.height = tup
        print(self.x, self.x, self.y, self.width, self.height)