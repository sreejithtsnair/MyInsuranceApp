import unittest
from user_manager import UserManager
from user import User

class UserManagerTest(unittest.TestCase):
    def test_1_addUser(self):
        user_manager=UserManager()
        aNewUser=User("Juan","j@j.com",34,"Lonsodn street")

        print(f"before: {len(user_manager.users)}")

        user_manager.addUser(aNewUser)
        print(f"valid added: {len(user_manager.users)}")
        
        self.assertTrue(len(user_manager.users)>0)

        user_manager.addUser(None)
        print(f"1 invalid added: {len(user_manager.users)}")        
        self.assertTrue(len(user_manager.users)==1)

        user_manager.addUser(User(None, None,0,None))
        print(f"2 invalid added: {len(user_manager.users)}")        
        self.assertTrue(len(user_manager.users)==1)

    def test_2_removeuser (self):
        user_manager=UserManager()
        aNewUser=User("Juan","j@j.com",34,"Lonsodn street")
        user_manager.addUser(aNewUser)
        users_size = len (user_manager.users)
        print(f"valid added for remove test: {users_size}")
        
        user_manager.removeUser (0) 
        print(f"user removed added: {len(user_manager.users)}")        
        self.assertTrue(len(user_manager.users)==users_size-1)

        users_size = len (user_manager.users)
        user_manager.removeUser (1.2)   
        self.assertTrue(len(user_manager.users)==users_size)

        #add new user to verify wrong indexes
        user_manager.addUser(aNewUser)
        
        users_size = len (user_manager.users)
        user_manager.removeUser (-1)   
        self.assertTrue(len(user_manager.users)==users_size)

        users_size = len (user_manager.users)
        user_manager.removeUser (1000)   
        self.assertTrue(len(user_manager.users)==users_size)


if __name__ == '__main__':
    unittest.main()


