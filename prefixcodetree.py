class PrefixCodeTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.symbol = None

    def insert(self, codeword, symbol):
        if codeword:
            if codeword[0] == 0:
                if self.left is None:
                    self.left = PrefixCodeTree()

                self.left.insert(codeword[1:], symbol)

            elif codeword[0] == 1:
                if self.right is None:
                    self.right = PrefixCodeTree()

                self.right.insert(codeword[1:], symbol)
        else:
            self.symbol = symbol

    def decode(self, encodedData, datalen):
        splitedData = list(encodedData)
        binData = ''
        message = ''
        curNode = self

        for byte in splitedData:
            binary = bin(byte)[2:].zfill(8)
            binData += binary

        print(binData)
        while datalen >= 0 and binData:
            if not (curNode.symbol is None):
                message += curNode.symbol
                curNode = self
            else:
                if binData[0] == '0':
                    curNode = curNode.left
                elif binData[0] == '1':
                    curNode = curNode.right

                binData = binData[1:]
                datalen -= 1

        return message


# codebook = {
#    'x1': [0],
#    'x2': [1, 0, 0],
#    'x3': [1, 0, 1],
#    'x4': [1, 1]
# }

# codeTree = PrefixCodeTree()

# for symbol in codebook:
#    codeTree.insert(codebook[symbol], symbol)

# message = codeTree.decode(b'\xd2\x9f\x20', 21)

# print(message)
