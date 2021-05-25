import hashlib
import datetime


class Block:

    def __init__(self, data, timestamp, previous_hash):

        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8'))  # convert to
        sha.update(self.data.encode('utf-8'))
        sha.update(self.previous_hash.encode('utf-8'))

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data, timestamp):
        if data == "":
            print("error: data is empty, add an argument")
            return

        date = timestamp

        if self.tail is not None and date <= self.tail.timestamp:
            print("Can't assign new block with timestamp smaller than last block")
            return

        if self.head is None and self.tail is None:
            self.head = Block(data, date, previous_hash="0")
            self.tail = self.head
            return

        else:
            temp = self.tail
            temp.next = Block(data, date, temp.hash)
            self.tail = temp.next

        return

    def block_is_there(self, data):
        head = self.head

        while head:
            if head.data == data:
                return ("hash:    " + head.hash + "," + "   previous_hash:   "+ head.previous_hash)
            else:
                if head.next is None:
                    return False
                else:
                    head = head.next

    def print_chain_block(self):

        if self.head is None:
            print("The chain is empty")
            return
        else:
            print("\nBlockchain details: \n_________________________\n")
            index = 0
            head = self.head

            while head:

                print(f'Blockchain index: {index} \n'
                      f'Blockchain time stamp:{head.timestamp} \n'
                      f'Blockchain data: {head.data} \n'
                      f'Blockchain hash:{head.hash} \n'
                      f'Blockchain previous hash: {head.previous_hash} \n'
                      f'\n_________________________\n'
                      )

                index += 1

                if head.next is None:
                    return
                else:
                    head = head.next


block_chain = BlockChain()
# testing empty chain
block_chain.append("", datetime.datetime.strptime("2021-05-11 17:57:00.612678", '%Y-%m-%d %H:%M:%S.%f'))

block_chain.append("first block", datetime.datetime.strptime("2021-05-11 17:57:01.612678", '%Y-%m-%d %H:%M:%S.%f'))
block_chain.append("second block", datetime.datetime.strptime("2021-05-11 17:57:02.612678", '%Y-%m-%d %H:%M:%S.%f'))
block_chain.append("third block", datetime.datetime.strptime("2021-05-11 17:57:03.612678", '%Y-%m-%d %H:%M:%S.%f'))
block_chain.append("fourth block", datetime.datetime.strptime("2021-05-11 17:57:04.612678", '%Y-%m-%d %H:%M:%S.%f'))
block_chain.append("fifth block", datetime.datetime.strptime("2021-05-11 17:57:05.612678", '%Y-%m-%d %H:%M:%S.%f'))

# testing chain with the same timestamp used before
block_chain.append("sixth block", datetime.datetime.strptime("2021-05-11 17:57:05.612678", '%Y-%m-%d %H:%M:%S.%f'))
block_chain.print_chain_block()

# test

print("Pass" if (block_chain.block_is_there("fourth block")) else "Fail")
print("Pass" if (block_chain.block_is_there("fifth block")) else "Fail")
print("Pass" if (not block_chain.block_is_there("sixth block")) else "Fail")



