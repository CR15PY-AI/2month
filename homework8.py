import sqlite3

class Person:
    def __init__(self, full_name):
        self._full_name = full_name

    def get_full_name(self):
        return self._full_name

class Database:
    def __init__(self, db_name="college.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT NOT NULL,
                age INTEGER)""")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                teacher TEXT NOT NULL)""")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                grade REAL,
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id))''')
        self.connection.commit()

class Students(Person, Database):
    def __init__(self, full_name, age):
        Person.__init__(self, full_name)
        Database.__init__(self)
        self._age = age

    def save_student(self):
        self.cursor.execute("INSERT INTO students(full_name, age) VALUES (?,?)", (self._full_name, self._age))
        self.connection.commit()

class Courses(Database):
    def __init__(self, title, teacher):
        Database.__init__(self)
        self._title = title
        self._teacher = teacher

    def save_course(self):
        self.cursor.execute("INSERT INTO courses(title, teacher) VALUES (?,?)", (self._title, self._teacher))
        self.connection.commit()

class Enrollment(Database):
    def __init__(self, student_id, course_id, grade):
        Database.__init__(self)
        self._student_id = student_id
        self._course_id = course_id
        self._grade = grade

    def save_enrollment(self):
        self.cursor.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)",
                            (self._student_id, self._course_id, self._grade))
        self.connection.commit()

def main_menu():
    db = Database()

    while True:
        print("\n==== МЕНЮ ====")
        print("1. Добавить студента")
        print("2. Добавить курс")
        print("3. Записать студента на курс с оценкой")
        print("4. Показать студентов с их курсами и оценками")
        print("5. Показать курсы с записанными студентами")
        print("6. Выход")
        choice = input("Выберите пункт: ")

        if choice == "1":
            name = input("ФИО студента: ")
            age = int(input("Возраст: "))
            student = Students(name, age)
            student.save_student()
            print("Студент добавлен.")

        elif choice == "2":
            title = input("Название курса: ")
            teacher = input("ФИО преподавателя: ")
            course = Courses(title, teacher)
            course.save_course()
            print("Курс добавлен.")

        elif choice == "3":
            student_id = int(input("ID студента: "))
            course_id = int(input("ID курса: "))
            grade = float(input("Оценка: "))
            enrollment = Enrollment(student_id, course_id, grade)
            enrollment.save_enrollment()
            print("Студент записан на курс.")

        elif choice == "4":
            db.cursor.execute("""
                SELECT students.id, students.full_name, students.age, courses.title, enrollments.grade
                FROM enrollments
                JOIN students ON enrollments.student_id = students.id
                JOIN courses ON enrollments.course_id = courses.id
            """)
            rows = db.cursor.fetchall()
            print("\nСтуденты с курсами и оценками:")
            for row in rows:
                print(f"ID: {row[0]}, ФИО: {row[1]}, Возраст: {row[2]}, Курс: {row[3]}, Оценка: {row[4]}")

        elif choice == "5":
            db.cursor.execute("""
                SELECT courses.id, courses.title, courses.teacher, students.full_name
                FROM enrollments
                JOIN courses ON enrollments.course_id = courses.id
                JOIN students ON enrollments.student_id = students.id
            """)
            rows = db.cursor.fetchall()
            print("\nКурсы с записанными студентами:")
            for row in rows:
                print(f"Курс ID: {row[0]}, Название: {row[1]}, Преподаватель: {row[2]}, Студент: {row[3]}")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор, попробуйте ещё раз.")

if __name__ == "__main__":
    main_menu()
