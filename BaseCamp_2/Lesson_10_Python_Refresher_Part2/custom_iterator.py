# Custom Iterators for Specialized Data Processing

class EvenNumberIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# Using the custom iterator
print("Even numbers from 0 to 10:")
even_iter = EvenNumberIterator(0, 10)
for num in even_iter:
    print(num, end=" ")  # 0 2 4 6 8 10

# Custom iterator with a specific condition (e.g., multiples of 3)
class MultiplesIterator:
    def __init__(self, start, end, multiple):
        self.current = start
        self.end = end
        self.multiple = multiple

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.end:
            result = self.current
            self.current += self.multiple
            if result % self.multiple == 0:
                return result
        raise StopIteration

# Using the multiples iterator
print("\nMultiples of 3 from 0 to 15:")
multiples_iter = MultiplesIterator(0, 15, 3)
for num in multiples_iter:
    print(num, end=" ")  # 0 3 6 9 12 15