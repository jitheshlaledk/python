class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
        #@ property
    def __str__(self):
        return self.course_name


class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name


django=Course()
django.add_course(course_name="django",status=True)
print(django)

meanstack=Course()
meanstack.add_course(course_name="meanstack",status=True)

batch1=Batch()
batch1.add_batch(course=django,batch_code="dkjangoapril2k22a1",start_date="20-06-2022")
print(batch1.course.status)

vishnu=Student()
vishnu.add_student(student_name="vishnu",email="vishnu@gmail.com",batch=batch1)

rahul=Student()
rahul.add_student(student_name="rahul",email="rahul@gmail.com",batch=batch1)

mean1=Batch()
mean1.add_batch(course=meanstack,batch_code="mean2k22a1",start_date="10-02-2022")

rahim=Student()
rahim.add_student(student_name="rahim",email="rahim@gmail.com",batch=mean1)

roy=Student()
roy.add_student(student_name="roy",email="roy@gmail.com",batch=mean1)


students=[]
students.append(roy)
students.append(rahim)
students.append(rahul)
students.append(vishnu)

m1=[student.student_name for student in students if student.batch.course.course_name=="meanstack"]
print(m1)

# masterstring="abbcddeghgggt"
# chkword="egg","cat"





