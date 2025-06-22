class race:
    name = ""
    age = 25
    nationality = ""
    quality = ("apex", "beautiful", "mid", "minority")

    def __init__(self, name, age, nationality, quality):
        pass

    def colors(self, black, brown, chinko, white):
        """ self.black = black
        self.brown = brown
        self.chinko = chinko
        self.white = white
        """
    print(f"You are from the {colors} race")

# Create objects associated with this class
african = race()    # An object
arab = race(any)       # An object
asian = race(any)      # An object
caucasian = race(any)  # An object

# Lets call these object and functions
african = race()
african.colors()

arab = race()
arab.colors()
