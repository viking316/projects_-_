from collections import defaultdict

class Node():
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

class DLL():
  def __init__(self ):
    self.head = None
    self.tail = None


  def append(self,data):
    new = Node(data)

    if self.head == None:
      self.head = new
      self.tail = new

      return self.head.data, self.head

    else:
      new.prev = None
      new.next = self.head
      self.head.prev = new
      self.head  = new

      return self.head.data, self.head

  def delete(self):
    
    if self.head == self.tail:
        temp = self.tail.prev
        value = self.tail.data
    
        self.head = self.tail = None
        return value

    else:
        temp = self.tail.prev
        
        value = self.tail.data

        self.tail.prev = None
        temp.next = None
        self.tail = temp
        
        return value


  def printLL(self):

    print("\n ---------------------------------- \n")
    if self.head == None:
      print("DLL is empty")
    else:
      curr = self.head
      while(curr):
        print(curr.data)
        curr = curr.next
    print("\n ---------------------------------- \n")

class LRU():
  
  def __init__(self,n):
    self.size = 0
    self.limit = n

    self.cache = DLL()
    self.hashh = defaultdict(str)

  def unload(self):
    d = self.cache.delete()
    self.hashh.pop(d)

  def load(self,data):
    if data in self.hashh.keys():
      print("key already exists")
      ans = input("do you want to use it? [y/n]")
      if ans == "y" or ans == "Y":
        self.use(data)

      else:
        pass

    elif self.size == self.limit:
      print("cache size limit reached, deleting least used cache")
      self.unload()

      v,add = self.cache.append(data)
      self.hashh[v] = add

      print(f"loaded {data} ")

    else:
        v,add = self.cache.append(data)
        self.hashh[v] = add
        self.size=self.size+ 1
        print(f"loaded {data} ")

  def fetch(self, data): #fetches the address of the object directly using hashing table instead of iterating
    return self.hashh[data] 
  
  def use(self,data):

    if data in self.hashh:
      curr = self.fetch(data)

      if curr == self.cache.head:
        print("used head")

      elif curr == self.cache.tail:
        print("used tail")

        self.tail = curr.prev
        self.cache.head.prev = curr
        curr.next = self.cache.head
        curr.prev.next = None
        curr.prev = None
        self.cache.head = curr
      
      else:
        print(f"using {data}")
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.cache.head.prev = curr
        curr.next = self.cache.head
        self.cache.head = curr
     
    
    else:
      self.load(data)

  
  def get_hash(self):
    print(self.hashh)



# c = LRU(10)

# c.load("first")
# c.load("second")
# c.load("third")
# c.load("fourth")
# c.load("fifth")
# c.load("sixth")
# c.load("seventh")
# c.load("eighth")
# c.load("ninth")
# c.load("tenth")
# c.cache.printLL()

# c.use("seventh")
# c.cache.printLL()

# c.load("fifth")
# c.cache.printLL()

# c.load("eleventh")
# c.cache.printLL()
# # c.get_hash()

   
basket = LRU(6)
basket.load("apple")
basket.load("banana")
basket.load("pineapple")
basket.load("dragon fruit")
basket.load("mango")
basket.load("watermelon")

basket.cache.printLL()

basket.use("mango")

basket.cache.printLL()

basket.load("kiwi")
basket.load("cherry")

basket.cache.printLL()
basket.load("dragon fruit")

basket.cache.printLL()
