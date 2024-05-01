class School:
    total_schools = 0  

    def __init__(self, name, level, num_students, year_founded):
        self.name = name
        self.level = level
        self.num_students = num_students
        self.year_founded = year_founded
        School.total_schools += 1  


    def description(self):
        return f"{self.name} - {self.level} school founded in {self.year_founded}. Currently has {self.num_students} students."


school1 = School("Primary School A", "Primary", 300, 1985)
school2 = School("High School B", "Secondary", 500, 2000)

print(school1.description())
print(school2.description())
print("Total schools created:", School.total_schools)
