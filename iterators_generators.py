import types


class FlatIterator:

    def __init__(self, list_of_list):
        self.result = list_of_list

    def __iter__(self):
        self.index = 0
        self.index_inner = 0
        return self

    def __next__(self):
        index_inner = self.index_inner
        if self.index >= len(self.result):
            raise StopIteration
        current = self.result[self.index]
        if index_inner < len(current) - 1:
            self.index_inner += 1
            return current[index_inner]
        else:
            buf = self.index_inner
            self.index_inner = 0
            self.index += 1
            return current[buf]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()


def flat_generator(list_of_lists):
    for item in list_of_lists:
        for el in item:
            yield el


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e',
                                                     'f', 'h', False, 1, 2,
                                                     None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
