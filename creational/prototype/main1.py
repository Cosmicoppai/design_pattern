

if __name__ == "__main__":
    import copy

    a = {"k": 0}
    b = copy.deepcopy(a)
    b["k"] = 1
    print(a, b)


    class Test:
        a: str = "k"
        b: str = "h"
        c: str = "hana"

        def __init__(self):
            self.test = "lol"


    c = Test()
    print(c.__dict__)
