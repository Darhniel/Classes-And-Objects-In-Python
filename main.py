class Student:
    
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = [tracks]
        self.score = float(score)
        
        print("My name is ", self.name)
        print("My age is ", self.age)
        print("My tracks is/are ", self.tracks)
        print("My score is ", self.score)

        
    def change_name(self, new_name):
        self.name = new_name
        print("My name is ", self.name) 

    def change_age(self, change_age):
        self.age = int(change_age)
        print("My age is ", self.age)

    def add_track(self, add_track):
        self.tracks = add_track
        print("My tracks is/are ", self.tracks)

    def get_score(self, get_score):
        self.score = float(get_score)
        print("My score is ", self.score)
    
    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(4)


