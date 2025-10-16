# class Student:
#     age = 20
#     name = "Bob"

class Student:
    spec = "Computer science"
    
    def __init__(self, name, age):
        self.name = name    
        self.age = age
    
    def showInfo(self):
        return f"Student {self.name} is {self.age} years old."
    
    def showMsg(self, msgText):
        return f"Student {self.name} says '{msgText}'."
    
student1 = Student("Name-1", 20)
student2 = Student("Name-2", 21)
student3 = Student("Name-3", 22)
student4 = Student("Name-4", 23)
student5 = Student("Name-5", 24)  
  
print(type(student1))

print(student1.name, student1.age)

# tema

# # Task 1
# Create a GitHub account. Your local repository should synchronize with GitHub.
 
 
 
# Task 2
# Create a folder with a set of subfolders and files.
 
 
 
# Task 3
# Create a repository in the main folder.
 
 
 
# Task 4
# Add the entire folder contents to the repository index using this command:
# git add
 
 
 
 
# Task 5
# Create a commit based on the data added to the index. Use this command:
# git commit
 
 
 
 
# Task 6:
# Create a new branch and name it newbranch.
 
 
 
 
# Task 7
# Create a new file and fill it with data. After that, create a commit with the new file in newbranch.
 
 
 
# Task 8
# Go to the master branch. Create a new file and fill it with data. After that, create a commit with the
# new file in the master branch.
 
 
 
 
# Task 9
# Go to newbranch. Merge the contents of master into newbranch.