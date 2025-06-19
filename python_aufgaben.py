
top_20_tv_shows = [("The Twilight Zone", 9.0),("Rick and Morty", 9.1),("Planet Earth", 9.4),("Band of Brothers", 9.4),("Blue Planet II", 9.3),("Breaking Bad", 9.5),("Game of Thrones", 9.2),("Life", 9.1),("Avatar: The Last Airbender", 9.3),("Fullmetal Alchemist: Brotherhood", 9.1),("Chernobyl", 9.3),("Cosmos", 9.3),("Planet Earth II", 9.5),("Our Planet", 9.2),("Cosmos: A Spacetime Odyssey", 9.2),("The World at War", 9.2),("The Wire", 9.3),("Bluey", 9.3),("The Sopranos", 9.2), ("The Last Dance", 9.1)]

def sort_via_lambda(list):
    return sorted(list, key = lambda x: (x[1], x[0]), reverse=True)

class iterator_for_powers_of:

    n = 0

    def  __init__(self, base=1):
        self.base = base

    def __iter__(self):
        self.n = 0
        return self
    

    def __next__(self):
        result =  self.base ** self.n
        self.n += 1

        return result


def fibonacci(n):
    x, y = 0,1

    for i in range(n):
        x, y = y, x+y
        yield x

print(sort_via_lambda(top_20_tv_shows))

power_of_2 = iterator_for_powers_of(2)

for i in range(10):
    print(next(power_of_2))

for i in fibonacci(10):
    print(i)

