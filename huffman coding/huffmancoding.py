
class Node:
    vall = None
    charr = None
    right = None
    left = None
    
    def __init__(self,charr,vall):
        self.vall = vall
        self.charr = charr

class Htree:
    root = None
    huffmanhash = {}

    def aio(self,filee):
        temphash= {}
        templist = []

        with open(filee,"r") as o:
            while True:
                char = o.read(1)
                if not char:
                    break
                if char not in temphash:
                    # t = Node(char,0)
                    temphash[char] = 1
                else:
                    temphash[char] = temphash[char]+1
        
        for i in temphash:
            
            t = Node(i,temphash[i])
            templist.append(t)

        
        self.maker(templist)
        
    def encoder(self,filee):
        if self.huffmanhash == None:
            print("Generate the Hashmap first!")
            return
        if self.root == None:
            print("Generate the huffman tree first!")
            return
        with open("encodedtext.txt","w") as writer:

            with open(filee,"r") as o:
                while True:
                    char = o.read(1)
                    if not char:
                        break
                    writer.write(self.huffmanhash[char])

        print("finish encoding the file to encodedtext.txt")
             
    def decoder(self,filee):
        with open(filee,"r") as r:
            c = self.root
            with open("decodedfile.txt","w") as d:
                while True:
                    char = r.read(1)
                    if char == "0":
                        c = c.left
                        if c.charr != "nn":
                            d.write(c.charr)
                            c= self.root
                    elif char == "1":
                        c = c.right
                        if c.charr != "nn":
                            d.write(c.charr)
                            c = self.root
                    else:
                        break
            d.close()
        r.close()
        print("finished decoding the file, saved it to decodedfile.txt.")



 

    def maker(self,listt):   
 
        print("Generating the huffman tree!")

        while(len(listt)>1):

            listt.sort(key= lambda x:x.vall)

            n1 = listt.pop(0)
            n2 = listt.pop(0)
            n = Node("nn",n1.vall+n2.vall)

            if n1.vall < n2.vall:
                n.left = n1
                n.right = n2
            else:
                n.left = n2
                n.right = n1

            listt.append(n)
        print("Huffman tree generated!, saved it to the root attribute of the object")
        self.root = listt[0]
        self.huffmangen()
        

    

    def __gener(self,node, code):
        
        if node.charr == "nn":
            if node.left != None:

                self.__gener(node.left,code+"0")
            if node.right != None:
                
                self.__gener(node.right,code+"1")
            return
        else:
            self.huffmanhash[node.charr] = code
            # print(node.charr)
            if node.left != None:

                self.__gener(node.left,code+"0")
            if node.right != None:    
  
                self.__gener(node.right,code+"1")
            return
        print("finished generating hashmap for decoding.")
        

    
    def huffmangen(self):
        if self.root != None:
            print("generating the hashmap for encoding.")
            self.__gener(self.root,"")
        else:
            print("Generate the tree first!(call 'coder' on the text file )") 
        



ht = Htree()
ht.aio("test.txt")
print(ht.huffmanhash)
ht.encoder("test.txt")
ht.decoder("encodedtext.txt")
