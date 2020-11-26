def bar(a: int, b: int) -> int:
    if a > 100:
        raise ValueError()
    print(a, b)
    return a + b
