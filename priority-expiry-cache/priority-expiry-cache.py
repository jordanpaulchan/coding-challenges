import time


class LinkedListNode:
    def __init__(self, key):
        # Key: the key inserted into the cache
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = LinkedListNode(-1)
        self.tail = LinkedListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Gets the earliest expiry time or lowest priority
    def getMinValueNode(self):
        current = self.root

        # loop down to find the leftmost leaf
        while current and current.left:
            current = current.left

        return current


class ExpireTimeNode:
    def __init__(self, time, keys=set()):
        # ExpireTime of the entry
        self.time = time
        # Set of keys with the expireTime
        self.keys = keys
        self.left = None
        self.right = None

    def removeKeyInNode(self):
        # removes arbitrary key from the list of keys
        key = self.keys.pop()
        if not self.keys:
            self.deleteNode()
        return key

    def deleteKeyInNode(self, key):
        self.keys.remove(key)
        if not self.keys:
            self.deleteNode()

    def deleteNode(self):
        # Removes the Node from the BST
        pass


class PriorityNode:
    def __init__(self, priority, lru={}):
        # Priority of the entry
        self.priority = priority
        # LRU Linked List Map: key is the key interested into the cache, value is a LinkedListNode
        self.lru = lru
        # Linked List: linked list to keep track of the head and tail of the  lru linked list
        self.linkedList = LinkedList()
        self.left = None
        self.right = None

    def deleteKeyInNode(self, key):
        llNode = self.lru[key]
        llNode.prev.next = llNode.next
        llNode.next.prev = llNode.prev
        del self.lru[key]
        if not self.lru:
            self.deleteNode()

    def deleteNode(self):
        # Removes the Node from the BST
        pass


class PriorityExpiryCache:
    def __init__(self, maxItems):
        self.maxItems = maxItems
        # Cache (map): key is the key inserted into the cache, value is an object with the value, priority and expireTime
        self.cache = {}
        # Expire Time BST: ordered based on the expire time
        self.expireTimeTree = BinarySearchTree()
        # Priority BST: ordered based on the priority
        self.priorityTree = BinarySearchTree()

    def evictItem(self):
        keyToDelete = None
        earliestExpiryTimeNode = self.expireTimeTree.getMinValueNode()
        if earliestExpiryTimeNode.key < int(time.time()):
            keyToDelete = earliestExpiryTimeNode.removeKeyInNode()

            keyPriority = self.cache[keyToDelete].priority

            priorityNode = self.priorityTree.getKeyNode(keyPriority)
            priorityNode.deleteKeyInNode(keyToDelete)
        else:
            lowestPriorityNode = self.priorityTree.getMinValueNode()
            keyToDelete = lowestPriorityNode.linkedList.tail.key
            priorityNode.deleteKeyInNode(keyToDelete)

            keyExpireTime = self.cache[keyToDelete].expireTime

            expireTimeNode = self.expireTimeTree.getKeyNode(keyExpireTime)
            expireTimeNode.deleteKeyInNode(keyToDelete)

        del self.cache[keyToDelete]

    def evictItems(self):
        while len(self.cache.keys()) > self.maxItems:
            self.evictItem()
