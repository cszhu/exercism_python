import random
import string

class Robot(object):
    used_names = []

    def __init__(self):
        self.reset()

    @staticmethod
    def generate_new_name():
        tempLetters = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
        tempDigits = ''.join(random.choice(string.digits) for i in range(3))
        return (tempLetters + tempDigits)

    def set_new_name(self):
        noNameFound = False
        while noNameFound == False:
            tempName = self.generate_new_name()
            if tempName not in self.used_names:
                return tempName
                noNameFound = True

    def reset(self):
        self.name = self.set_new_name()
        self.used_names.append(self.name)
