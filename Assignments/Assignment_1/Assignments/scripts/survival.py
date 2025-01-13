from random import random

class Node:

    def __init__(self, name):
        self.name = name

    def reboot(self, neighbors):
        self.neighbors = neighbors
        self.message = ['', '', '', '', '']

    def deliver_message_bit(self, index, messageBit):
        self.message[index - 1] = messageBit

    def send_random_message_bit_to_neighbors(self):
        ownedMessageBits = 0
        for messageBit in self.message:
            if messageBit:
                ownedMessageBits += 1
        if ownedMessageBits == 0:
            return
        selectedMessageIndex = int(random() * ownedMessageBits)
        for i, messageBit in enumerate(self.message):
            if messageBit:
                if selectedMessageIndex == 0:
                    selectedMessageIndex = i
                    selectedMessage = messageBit
                    break
                else:
                    selectedMessageIndex -= 1
        for node in self.neighbors:
            node.deliver_message_bit(selectedMessageIndex + 1, selectedMessage)

    def tell_message(self):
        output = f'[{self.name}]'
        for m in self.message:
            if m == '': 
                output += ' ???'
            else:
                output += ' ' + m
        return output
        #return f'[{self.name}] ' + ' '.join(map(lambda x: x if x else '???', self.message))

class Simulation:

    def __init__(self, nodeCount, connectProbability, crashProbability):
        self.nodeCount = nodeCount
        self.connectProbability = connectProbability
        self.crashProbability = crashProbability

    def reboot_node_with_random_neighbors(self, nodeToReboot, potentialNeighbors):
        neighbors = []
        for node in potentialNeighbors:
            if node == nodeToReboot:
                continue
            if random() < self.connectProbability:
                neighbors.append(node)
        nodeToReboot.reboot(neighbors)

    def run(self, days):
        nodes = [Node(f'Noeud {i+1}') for i in range(self.nodeCount)]
        for node in nodes:
            self.reboot_node_with_random_neighbors(node, nodes)
            node.message = 'taking the hobbits to isengard'.split()
        for i in range(days):
            for node in nodes:
                if random() < self.crashProbability:
                    self.reboot_node_with_random_neighbors(node, nodes)
                else:
                    node.send_random_message_bit_to_neighbors()
        for node in nodes:
            print(node.tell_message())