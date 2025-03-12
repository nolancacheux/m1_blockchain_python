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
        ownedMessageBits = sum(1 for bit in self.message if bit)
        if ownedMessageBits == 0:
            return
        selectedMessageIndex = int(random() * ownedMessageBits)
        for i, messageBit in enumerate(self.message):
            if messageBit:
                if selectedMessageIndex == 0:
                    selectedMessage = messageBit
                    break
                selectedMessageIndex -= 1
        for neighbor in self.neighbors:
            neighbor.deliver_message_bit(i + 1, selectedMessage)

    def tell_message(self):
        return f'[{self.name}] ' + ' '.join(m if m else '???' for m in self.message)

class Simulation:

    def __init__(self, nodeCount, connectProbability, crashProbability):
        self.nodeCount = nodeCount
        self.connectProbability = connectProbability
        self.crashProbability = crashProbability

    def reboot_node_with_random_neighbors(self, nodeToReboot, potentialNeighbors):
        neighbors = [node for node in potentialNeighbors if node != nodeToReboot and random() < self.connectProbability]
        nodeToReboot.reboot(neighbors)

    def run(self, days):
        nodes = [Node(f'Node {i + 1}') for i in range(self.nodeCount)]
        for node in nodes:
            self.reboot_node_with_random_neighbors(node, nodes)
            node.message = 'taking the hobbits to isengard'.split()
        for _ in range(days):
            for node in nodes:
                if random() < self.crashProbability:
                    self.reboot_node_with_random_neighbors(node, nodes)
                else:
                    node.send_random_message_bit_to_neighbors()
        for node in nodes:
            print(node.tell_message())
