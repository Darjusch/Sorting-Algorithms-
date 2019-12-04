class InsertionSort:
    def __init__(self, array_to_sort):
        self.array_to_sort = array_to_sort
        self.sort_unsorted()

    def sort_unsorted(self):
        print(f'initial list: {self.array_to_sort}')
        moves_to_sort = 0
        for i in range(len(self.array_to_sort)):
            cursor = self.array_to_sort[i]
            pos = i
            while pos > 0 and self.array_to_sort[pos -1] > cursor:
                self.array_to_sort[pos] = self.array_to_sort[pos-1]
                pos = pos-1
                moves_to_sort = moves_to_sort + 1
                print(f'Each sortie displayed: {self.array_to_sort}')
            self.array_to_sort[pos] = cursor
        print(f'final: {self.array_to_sort} in {moves_to_sort} moves!')

insertion = InsertionSort([8, 2, 1, 5, 4, 7, 0])