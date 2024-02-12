import unittest

class Person:

    def __init__(self , fname , lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return f'{self.fname}  {self.lname}'

    def email(self):
        return f'{self.fullname()}@gmail.com'.replace(' ' , '') 

class PersonTest(unittest.TestCase):

    @pytest.fixture
    def init(self): #setUp will be ran before the class
        self.p1 = Person('amir' , 'amiri')
        self.p2 = Person('john' , 'doe')

 

    def test_fullname(self):
        #p1 = Person('amir' , 'amiri')
        #p2 = Person('ali' , 'aliyi')
        # here we are doing smt on and on , so if we want to prevent writing many codes , we use fixtures  
  
        assert self.p1.fullname() == 'amir amiri'   
        assert self.p2.fullname() == 'ali aliyi'

    def test_email(self):
        #p1 = Person('amir' , 'amiri')
        #p2 = Person('ali' , 'aliyi') 

        assert self.p1.email() =='amiramiri@gmail.com'
        assert self.p2.email() == 'alialiyi@gmail.com'
	#end

