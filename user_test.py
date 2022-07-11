import imp
import unittest
from user import User

class UserTest(unittest.TestCase):
    def test_user_talks(self):
        juan_object = User ("Juan", "j@j.com", "23", "London Street")
        print(juan_object)
        print(juan_object.name)
        print(juan_object.address)
        self.assertIsNotNone(juan_object)
        message = juan_object.talk()
        print (message)
        self.assertIsNotNone(message)
        self.assertTrue(message.index ('Juan') >=0)
        ana_object = User ("ana", "a@j.com", "23", "Munich Street")
        message_from_ana = ana_object.talk()
        print(message_from_ana)
        self.assertTrue(message_from_ana.index ('ana') >=0)

    def test_user_says_address(self):
        sree_object = User ("Sree", "S@j.com", "23", "Kerala Street")
        theaddress = sree_object.saysAddress()
        self.assertTrue(theaddress.index ('Kerala') >=0)
        self.assertTrue(theaddress.index ('It is in India') >=0)
        print(theaddress)
        self.assertTrue(theaddress.index ('It is in India') >=0)
        print(theaddress)