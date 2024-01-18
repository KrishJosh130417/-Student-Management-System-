import string
import random
from pathlib import Path
import json


class Students:
    data = []
    database = "students.json"

    try:
     if Path(database).exists():
      with open(database) as fs:
         data = json.loads(fs.read)
    except Exception as err:
       print(err)

    @classmethod
    def UpdateStudent(cls):
       with open(cls.database,"w") as fs:
          fs.write(json.dumps(cls.data))

    @classmethod
    def randomid(cls):
       alpha = random.choices(string.ascii_letters,k=3)
       numbers = random.choices(string.digits, k=3)
       spchar = random.choices("!@#$%^&*",k=2)
       id = alpha+numbers+spchar
       random.shuffle(id)
       return "".join(id)
    
    def RegisterStudent(self):
       stu = {
          "ID":Students.randomid(),
          "Name":input("Tell your name "),
          "Email":input("Tell Your Email "),
          "Password":input("Tell Your Password "),
          "Skill":input("Tell your Skill ")
       }
       Students.data.append(stu)
       Students.UpdateStudent()

    def ReadSingleStudent(self):
       id = input("Enter ID : ")
       password = input("Enter Passsword : ")
       student = [i for i in Students.data if i["id"] == id and i["password"] == password]
       if len(student) == 0:
           print("invalid credentials")
       else:
           for j in student[0]:
               print(f"{j} : {student[0][j]}") 

    def AccessData(self):
       a = Students.data
       counter = 0
       for i in a:
          print()
          print(counter)
          print()
          for j in i:
              print(f"{j} : {i}{j}")
       counter+=1

    def UpdateStudentData(self):
       id = input("Enter Id : ")
       password = input("Enter Password : ")
       student = [i for i in Students.data if i["id"] == id and i["password"] == password]
       if len(student) == 0:
          print("invalid credentials")
       else:
          print("Enter to skip")
          stu = {
             "name": input("Please tell your new name"),
             "email": input("Please tell your new email"),
             "password":input("tell your password "),
             "skill": input("Update your skill ")
          }
          if stu["name"] =="":
             stu["name"] = student[0]["name"]
          if stu["email"] =="":
             stu["email"] = student[0]["email"]
          if stu["password"] =="":
             stu["password"] = student[0]["password"]
          if stu["skill"] =="":
             stu["skill"] = student[0]["skill"]

          for i in stu.keys():
             if stu[i] == student[0][i]:
                continue
             else:
                student[0][i] = stu[i]
          self.UpdateStudent()

    def DeleteStudentData(self):
       id = input("tell the id: ")
       password = input("Enter the password ")
       student = [
          i
          for i in Students.data
          if i["id"] == id and i["password"] == password
       ]           

       if len(student)==0:
          print("invalid credentials ")
       else:
          check = input("Are you sure to delete ie press Y/N ")

          if check == "Y" or check == "N":
             studentindex = Students.data.index(student[0])
             Students.data.pop(studentindex)
             self.UpdateStudent()
             print("Done ")

          elif check == "N" or check =="n":
             pass
          
          else:
             print("Wrong input ")
          



randomname = Students()

while True:

   print("""
   select an option
         1: register a student
         2: login student profile
         3: access database
         4: Update Student Data
         5: Delete Student Data
         0: Exitting the application
   """)

   n = int((input(" Tell your response ")))

   if n==0:
      exit(0)

   if n==1:
      randomname.RegisterStudent()

   if n==2:
      randomname.ReadSingleStudent()

   if n==3:
      randomname.AccessData()

   if n==4:
      randomname.UpdateStudentData()

   if n==5:
      randomname.DeleteStudentData()