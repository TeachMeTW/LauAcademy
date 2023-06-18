# Static Variables that can be accessed with each isntance of the SharedData class
user_information = None
flashcards = None
test = None

class SharedData:
    def __init__(self):
        self.data = None
    
    """
    user_information = {
        "name": name,
        "educational_background": educational_background,
        "desired_career": desired_career,
        "class_subject": class_subject,
        "uploaded_file": uploaded_file
    }
    """
    
    def store_user_information(self, user_information_param):
        global user_information
        user_information = user_information_param
    
    def get_user_information(self):
        global user_information
        return user_information
    
    # Data from the Flashcards
    def set_flashcards(self, flashcards_param):
        global flashcards
        flashcards = flashcards_param
        
    def get_flashcards(self):
        global flashcards
        return flashcards
    
    # Test Text that will be transfered from other python files
    def set_test(self, test_param):
        global test
        test = test_param
        print(f'[SharedData.py] set_test(): {test}')
    
    def get_test(self):
        global test
        print(f'[SharedData.py] get_test(): {test}')
        return test