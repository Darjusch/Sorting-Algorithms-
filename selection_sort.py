class SelectionSort:
    def __init__(self, array_to_sort):
        self.array_to_sort = array_to_sort
        self.find_unsorted()

    def swap(self, minimum, current_number):
        print(f'min{minimum}, current{current_number}')
        self.array_to_sort[minimum], \
        self.array_to_sort[current_number] = self.array_to_sort[current_number],\
                                             self.array_to_sort[minimum]
        print(f'Each sortie displayed: {self.array_to_sort}')

    def find_unsorted(self):
        print(f'initial list: {self.array_to_sort}')
        moves_to_sort = 0
        for current_number in range(len(self.array_to_sort)):
            minimum = current_number
            for current_nested_number in range(current_number+1, len(self.array_to_sort)):
                if self.array_to_sort[current_nested_number] < self.array_to_sort[minimum]:
                    minimum = current_nested_number
            moves_to_sort = moves_to_sort+1
            self.swap(minimum, current_number)
        print(f'final: {self.array_to_sort} in {moves_to_sort} moves!')


select=SelectionSort([8, 2, 1, 5, 4, 7, 0])