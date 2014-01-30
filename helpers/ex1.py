import logging

def test_largest_drop(func):
    try:
        assert func([6,1]) == 5, '[6,1] should return 5 (6-1=5)'
        assert func([4,3,2,1]) == 3, '[4,3,2,1] should return 3 (4-1=3)'
        assert func([1,2,3,4]) is None, 'What if the number are only increasing?'
        assert func([]) is None, 'What if the list is empty?'
        print 'perfect'
    except AssertionError as msg:
        logging.error(msg)

