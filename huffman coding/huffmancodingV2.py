def pad_bitstring(bitstring):
    # Calculate the number of padding bits needed
    padding_length = (8 - len(bitstring) % 8) % 8
    padding = '0' * padding_length
    padded_bitstring = bitstring + padding
    return padded_bitstring, padding_length

def write_bits_to_file(bitstring, filename):
    padded_bitstring, padding_length = pad_bitstring(bitstring)
    
    # Write padding length at the beginning to handle it during decoding
    with open(filename, "wb") as file:
        file.write(bytes([padding_length]))  # Write the padding length as a single byte
        byte_array = bytearray()
        for i in range(0, len(padded_bitstring), 8):
            byte = padded_bitstring[i:i + 8]
            byte_array.append(int(byte, 2))
        file.write(byte_array)

def read_bits_from_file(filename):
    with open(filename, "rb") as file:
        padding_length = ord(file.read(1))  # Read the padding length
        bitstring = ""
        byte = file.read(1)
        while byte:
            bits = bin(ord(byte))[2:].rjust(8, '0')
            bitstring += bits
            byte = file.read(1)
        # Remove the padding
        if padding_length > 0:
            bitstring = bitstring[:-padding_length]
    return bitstring


import heapq

class Node:
    def __init__(self, charr, vall):
        self.charr = charr
        self.vall = vall
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.vall < other.vall


class Htree:
    def __init__(self):
        self.root = None
        self.huffmanhash = {}

    def aio(self, filee):
        temphash = {}

        with open(filee, "r") as o:
            while True:
                char = o.read(1)
                if not char:
                    break
                if char not in temphash:
                    temphash[char] = 1
                else:
                    temphash[char] += 1

        priority_queue = [Node(char, freq) for char, freq in temphash.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            n1 = heapq.heappop(priority_queue)
            n2 = heapq.heappop(priority_queue)
            merged = Node(None, n1.vall + n2.vall)
            merged.left = n1
            merged.right = n2
            heapq.heappush(priority_queue, merged)

        self.root = priority_queue[0]
        self.huffmangen()

    def huffmangen(self):
        self.__gener(self.root, "")

    def __gener(self, node, code):
        if node.charr is not None:
            self.huffmanhash[node.charr] = code
        else:
            self.__gener(node.left, code + "0")
            self.__gener(node.right, code + "1")

    def encoder(self, filee):
        if not self.huffmanhash or not self.root:
            print("Generate the Huffman tree and hashmap first!")
            return

        bitstring = ""
        with open(filee, "r") as o:
            while True:
                char = o.read(1)
                if not char:
                    break
                bitstring += self.huffmanhash[char]

        write_bits_to_file(bitstring, "encodedtext.bin")
        print("Finished encoding the file to encodedtext.bin")

    def decoder(self, filee):
        bitstring = read_bits_from_file(filee)

        with open("decodedfile.txt", "w") as d:
            current_node = self.root
            for bit in bitstring:
                if bit == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right

                if current_node.charr is not None:
                    d.write(current_node.charr)
                    current_node = self.root

        print("Finished decoding the file, saved it to decodedfile.txt.")


def pad_bitstring(bitstring):
    padding_length = (8 - len(bitstring) % 8) % 8
    padding = '0' * padding_length
    padded_bitstring = bitstring + padding
    return padded_bitstring, padding_length

def write_bits_to_file(bitstring, filename):
    padded_bitstring, padding_length = pad_bitstring(bitstring)
    
    with open(filename, "wb") as file:
        file.write(bytes([padding_length]))  # Write the padding length as a single byte
        byte_array = bytearray()
        for i in range(0, len(padded_bitstring), 8):
            byte = padded_bitstring[i:i + 8]
            byte_array.append(int(byte, 2))
        file.write(byte_array)

def read_bits_from_file(filename):
    with open(filename, "rb") as file:
        padding_length = ord(file.read(1))  # Read the padding length
        bitstring = ""
        byte = file.read(1)
        while byte:
            bits = bin(ord(byte))[2:].rjust(8, '0')
            bitstring += bits
            byte = file.read(1)
        if padding_length > 0:
            bitstring = bitstring[:-padding_length]
    return bitstring


ht = Htree()
ht.aio("test.txt")
print(ht.huffmanhash)
ht.encoder("test.txt")
ht.decoder("encodedtext.bin")
