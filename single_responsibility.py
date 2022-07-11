class Student:
    def __init__(self, name, id, major):
        self.student_info = Student_info(name, id, major)
        self.student_grade = Student_grade()

    def print_report_card(self):
        print(f'코드잇 대학 성적표\n\n학생 이름:{self.student_info.name}\n학생 번호:{self.student_info.id}\n소속 학과:{self.student_info.major}\n평균 학점:{self.student_grade.get_average_gpa()}')

class Student_info:
    def __init__(self, name, id, major):
        self._name = name
        self._id = id
        self._major = major

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, new_major):
        self._major = new_major

    def change_info(self, new_name, new_id, new_major):
        self._name = new_name
        self._id = new_id
        self._major = new_major

class Student_grade:
    def __init__(self):
        self._grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 4.3:
            self._grades.append(grade)
        else:
            print('수업 학점은 0과 4.3 사이여야 합니다!')

    def get_average_gpa(self):
        return sum(self._grades) / len(self._grades)

younghoon = Student('강영훈', 20120034, '통계학과')
younghoon.student_info.change_info('강영훈', 20130024, '컴퓨터 공학과')

younghoon.student_grade.add_grade(3.0)
younghoon.student_grade.add_grade(3.33)
younghoon.student_grade.add_grade(3.67)
younghoon.student_grade.add_grade(4.3)

younghoon.print_report_card()