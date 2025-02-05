'''
General case represents that developer working on 
frontend cannot work backend development unless he/she is fullstack dev.

Write a method named verifier () that checks this condition.

The method should check that if frontend is True and backend is True,
the method returns Fullstack as string. If one of them is True, it should return
the respective desgination, and if none of them are true, it returns,
not a developer respectively.
'''

class Employee:
    def _init_ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def _repr_ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self):
        if ((self.backend) and (self.frontend)):
            return 'Fullstack '
        elif self.backend:
            return 'Backend '
        elif self.frontend:
            return 'Frontend'
        else:
            return 'Not a '

if __name__ == '_main_':
    frnt = bool(int(input("Does Employee know Frontend Coding?(Yes->1/No->0)\n")))
    bck = bool(int(input("Does Employee know Backend Coding?(Yes->1/No->0)\n")))
    firstEmployee = Employee (frontend=frnt, backend=bck)
    result = firstEmployee.verifier()
    print(result, firstEmployee.designation)