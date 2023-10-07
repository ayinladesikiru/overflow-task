from challenge1 import challenge_1a


def test_compress_function():
    assert challenge_1a.compress('bbcceeee') == 'b2c2e4'
    assert challenge_1a.compress('aaabbbcccaaa') == 'a3b3c3a3'
    assert challenge_1a.compress('a') == 'a'
