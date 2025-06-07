class student:
    def __init__(self,name):
        self.__name = name
 
    def get__name(self):
        return self.__name
           
    def set__name(self,name):
        return self.__name
    
class person(student):
    def __init__(self,name,rollno,branchname):
        super().__init__(name)
        self.__rollno=rollno
        self.__branchname=branchname
    
    def get__branchname(self):
        return self.__branchname
    def get__rollno(self):
        return self.__rollno
    
    def set__(self,branchname):
        return self.__branchname
    
    def set__(self,rollno):
        return self.__rollno



    def __str__(self):
        return f"person:{self.get__namename} {self.__rolno} {self.__branchanme}"

        

    






    
      

obj=person()
obj.get()
obj.set()
