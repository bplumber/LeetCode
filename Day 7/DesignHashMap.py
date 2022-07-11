class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        found = False
        for i,x in enumerate(self.arr):
            if x[0] == key:
                self.arr[i] = [key, value]
                found = True
        if found == False:
            self.arr.append([key, value])
                            
    def get(self, key: int) -> int:
        for i in self.arr:
            if i[0]==key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.arr:
            if i[0] == key:
                self.arr.remove(i)
                break

# ALTERNATE SOLUTION

class MyHashMap:

    def __init__(self):
        self.arr = {}

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        if key in self.arr:
            return self.arr[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.pop(key)

