class User:
    '''
    This class helps generate instances for creating a new account on this appliation
    '''
    profile_list = [] # empty profile list
    def __init__(self, userName, password):
        '''
        This function helps define properties to create a PASSWORD-MANAGER account.
        Args: 
            userName: user's username
            password: user's password
        '''
        self.userName = userName
        self.password = password

    def save_profile(self):
        '''
        Test to save a new profile
        '''
        User.profile_list.append(self)

    def delete_profile(self):
        '''
        Test to delete user's profile
        '''
        User.profile_list.remove(self)

# end of users instance
#starts of accounts credentials
## generate credentials instances