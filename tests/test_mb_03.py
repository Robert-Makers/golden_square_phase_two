from mocking_bites.exercise3 import *
from unittest import mock

class TestSecretDiaryUnit():
    '''
    Given I initialise a secret diary
    The secret diary contains on empty diary instance
    The secret diary contains a locked parameter set to false
    '''


    '''
    Given I lock the secret diary
    The locked parameter is set to true
    '''


    '''
    Given I unlock the secret diary
    The locked parameter is set to false
    '''


    '''
    Given I red the diary and it is locked 
    Return a message to go away
    '''


    '''
    Give I read the diary and it is unlocked
    Return the diary contents
    '''



class TestSecretDiaryIntegration():
    '''
    Given I have a secret diary I initialise it with a Diary that has contents
    I can see the diary contents
    '''


    '''
    Given I lock the secret diary
    I get a message 'go away' when I try to read the diary
    '''


    '''
    Given I unlock the secret diary
    I can read the diary contents
    '''


class TestDiaryUnit():
    '''
    Given a diary that I can read
    Return diary contents
    '''