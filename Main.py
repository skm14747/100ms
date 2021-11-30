from BinarySearch import pivotedBinarySearch

class DS():

    def __init__(self, n) -> None:
        self.n = n # to hold the size of the 
        self.currentSize = 0 # current size of the streamed number to check if stream is full or not
        self.arr = [] # to hold all the numbers which is coming in stream
        self.index = [] # to hold the index of the numbers coming in stream
        self.count = 0 # current count of the streamed numbers
    
    """
    Add function will simply keep on adding the numbers in the array untill it is full
    If the array is full then It will override the first most streamed element(using hashing) in the array 
    and simply remove it from linkedlist
    """
    def add(self, val):
        # check if current stream is full or not.
        if self.currentSize < self.n:
            self.arr.append(val)
            self.index.append(self.count)
            self.count += 1
            self.currentSize+=1

        else:
            # if current stream is full then it will override the first most sreamed element
            self.arr[(self.count%self.n)] = val
            self.index[(self.count%self.n)] = self.count
            self.count += 1
            

    def search(self,val):
        # since our elements will be in rotated yet sorted fashion
        # we can use special binary search to find the element
        searchedIndex = pivotedBinarySearch(self.arr, self.n, val)
        if searchedIndex == -1:
            return -1
        # If element is found in the rotated array 
        # then we can simply return the respective index from rotated array
        return self.index[searchedIndex]



n = 3
s = DS(n)

s.add(1)
s.add(2)
s.add(3)

print(s.search(1))
print(s.search(2))
print(s.search(3))
print(s.search(4))

s.add(4)


print(s.search(1))
print(s.search(2))
print(s.search(3))
print(s.search(4))
print(s.search(5))

s.add(5)



print(s.search(1))
print(s.search(2))
print(s.search(3))
print(s.search(4))
print(s.search(5))
print(s.search(6))







