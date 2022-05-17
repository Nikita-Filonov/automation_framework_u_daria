class Animal:
    voice = 'some'

    def say(self):
        print(self.voice)


dog = Animal()

dog.voice = 'Hello'

dog.say()
