# Брудний код

class Students:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        ##Використання словника замість класу для студентів
        self.students.append({"name": name, "grade": grade})

    def remove_student(self, name):
        ##Видалення студента через цикл з модифікацією списку
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                break

    def show_stats(self):
        total = 0
        count = 0
        for student in self.students:
            total += student["grade"]
            count += 1
        avg = total / count if count != 0 else 0
        print("Середній бал групи: ", avg)

    def show_students(self):
        for student in self.students:
            print(student["name"], " - ", student["grade"])

students_db = Students()
students_db.add_student("Іван", 90)
students_db.add_student("Марія", 85)
students_db.add_student("Олексій", 78)
students_db.show_students()
students_db.show_stats()

students_db.remove_student("Марія")
students_db.show_students()


## -------------------------------------------------------------------------------


# Чистий код після рефакторингу

class Student:
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade

class StudentDatabase:
    """
    Клас для зберігання і маніпулювання даними студентів.
    """

    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        self.students = [student for student in self.students if student.name != name]

    def calculate_average_grade(self) -> float:
        if not self.students:
            return 0.0
        total_grade = sum(student.grade for student in self.students)
        return total_grade / len(self.students)

    def list_students(self):
        for student in self.students:
            print(f"{student.name} - {student.grade}")

class StudentDatabaseManager:
    """
    Клас для керування та відображення статистики по студентам.
    """

    @staticmethod
    def display_average_grade(db: StudentDatabase):
        average = db.calculate_average_grade()
        print(f"Середній бал групи: {average}")

    @staticmethod
    def display_all_students(db: StudentDatabase):
        db.list_students()

if __name__ == "__main__":
    db = StudentDatabase()

    db.add_student(Student("Тарас", 90))
    db.add_student(Student("Олександр", 85))
    db.add_student(Student("Андрій", 78))

    # Виведення всіх студентів
    StudentDatabaseManager.display_all_students(db)

    # Виведення середнього балу
    StudentDatabaseManager.display_average_grade(db)

    # Видалення студента
    db.remove_student("Марія")
    StudentDatabaseManager.display_all_students(db)

