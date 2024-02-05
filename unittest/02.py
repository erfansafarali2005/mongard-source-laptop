import unittest

class FuncTest(unittest.TestCase):
    def test_add(self):
        self.assert_Equal(doctest.add(2,3) , 5)

    def test_subtract(self):
        self.assert_Equal(doctest.add(5,3) , 2)

    def test_division(Self):
        self.assert_Raises(ZeroDivisionError , one.multiply , 4 , 2)    



if __name__ == __main__ :
    unittets.main()        