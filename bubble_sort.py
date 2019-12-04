class BubbleSort:
    def __init__(self, array_to_sort):
        self.array_to_sort = array_to_sort
        self.find_unsorted()

    def swap(self, x, y):
        self.array_to_sort[x], self.array_to_sort[y] = self.array_to_sort[y], self.array_to_sort[x]
        print(f'Each sortie displayed: {self.array_to_sort}')

    def find_unsorted(self):
        print(f'initial list: {self.array_to_sort}')
        n = len(self.array_to_sort)
        unsorted = True
        x = -1
        moves_to_sort = 0
        while unsorted:
            unsorted = False
            x = x +1
            for number in range(1, n - x):
                if self.array_to_sort[number-1] > self.array_to_sort[number]:
                    self.swap(number-1, number)
                    moves_to_sort = moves_to_sort +1
                    unsorted = True
        print(f'final: {self.array_to_sort} in {moves_to_sort} moves!')


sort = BubbleSort([8, 2, 1, 5, 4, 7, 0])
