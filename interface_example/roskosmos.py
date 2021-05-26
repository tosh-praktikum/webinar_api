class Spaceship:
    def __init__ (self, title):
        self.title = title
        self.settings = {}

    def __first_stage(self):
        print("First stage")

    def __second_stage(self):
        print("Second stage")

    def __upper_stage(self):
        print("Upper stage")

    def setup(self, **settings):
        self.settings = settings
    
    def launch(self):
        print(f"Launching the spaceship {self.title} with the following settings: {self.settings}")

        self.__first_stage()
        self.__second_stage()
        self.__upper_stage()

        return True