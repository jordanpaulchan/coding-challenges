import unittest


class FIFO:
    def __init__(self, size=5):
        self.list = [0] * size
        self.push_idx = 0
        self.pop_idx = 0

    def push(self, val):
        self.list[self.push_idx] = val
        self.push_idx = (self.push_idx + 1) % len(self.list)

        if self.push_idx == self.pop_idx:
            self.increase_lst_size()

    def pop(self):
        if self.pop_idx == self.push_idx:
            return None

        val = self.list[self.pop_idx]
        self.pop_idx = (self.pop_idx + 1) % len(self.list)

        return val

    def increase_lst_size(self):
        new_list = [0] * (len(self.list) * 2)
        new_list_idx = 0

        for i in xrange(0, len(self.list)):
            idx = (self.push_idx + i) % len(self.list)
            new_list[new_list_idx] = self.list[idx]
            new_list_idx += 1

        self.list = new_list
        self.push_idx = new_list_idx
        self.pop_idx = 0


class FIFOTests(unittest.TestCase):
    def test_push_pop(self):
        fifo = FIFO()
        fifo.push(1)
        self.assertEqual(fifo.pop(), 1)

    def test_increase_size(self):
        fifo = FIFO(2)
        fifo.push(1)
        fifo.push(2)
        self.assertEqual(len(fifo.list), 4)

    def test_wrap(self):
        fifo = FIFO(3)
        fifo.push(1)
        fifo.push(2)
        fifo.pop()
        fifo.pop()
        fifo.push(3)
        fifo.push(4)
        self.assertEqual(len(fifo.list), 3)
        self.assertEqual(fifo.pop(), 3)
        self.assertEqual(fifo.pop(), 4)


if __name__ == '__main__':
    unittest.main()
