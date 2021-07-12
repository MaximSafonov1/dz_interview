class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, el):
        self.list.append(el)

    def pop(self):
        self.list.pop()
        return self.peek()

    def peek(self):
        if self.is_empty():
            return None
        return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)


def balancing_parentheses(string_):
    stack = Stack()
    parentheses = {'(': ')', '[': ']', '{': '}'}
    print('начало')
    for el in string_:
        if el in parentheses:
            stack.push(el)
            print('добавление', el)
        elif el == parentheses.get(stack.peek()):
            stack.pop()
            print('удаление', el)
        else:
            print('Несбалансированная последовательность.')
            return False
    if stack.is_empty():
        print('Сбалансированная последовательность.')


#[[{())}]
#(((([{}]))))


if __name__ in '__main__':
    string = input('Введите строку: ')
    balancing_parentheses(string)
