def test_mark(i):
    message = "This student got a bad mark!"
    assert i > 4, message
    return i


print(test_mark(5))  # 5
print(test_mark(2))
