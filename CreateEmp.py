#Import the necessary modules
import requests
import json
import jsonpath

#####TASK 1#####
#Assign the Create Request call
createEmployeeurl = "http://dummy.restapiexample.com/api/v1/create"

#Read the input
with open("C:\\Users\\Dell\\Desktop\\API Testing\\CreateEmployee.json","r") as InputFile:
    FirstEmployee = InputFile.read()
    FirstEmployee_json = json.loads(FirstEmployee)
    print(FirstEmployee_json)
    
#Insert Employee details using POST method
createresponse = requests.post(createEmployeeurl,FirstEmployee_json)
print(createresponse.content)

assert createresponse.status_code == 201
#parse response as json format
createresponse_json = json.loads(createresponse.text)
print(createresponse_json)
empName = jsonpath.jsonpath(createresponse_json,'employee_name')
for name in empName:
    if name == 'Employee1':
        print ('Successful insertion')
        

#####TASK 2##### 
#Verification of employee creation
verifyEmployeeurl = "http://dummy.restapiexample.com/api/v1/employee/1"
verifyresponse = requests.get(verifyEmployeeurl)
print(verifyresponse.content)


#####TASK 3#####        
#updation of record
updateEmployeeurl = "http://dummy.restapiexample.com/api/v1/update/21"

#Read the input
with open("C:\\Users\\Dell\\Desktop\\API Testing\\UpdateEmployee.json","r") as UpdateFile:
    UpdateEmployee = UpdateFile.read()
    UpdateEmployee_json = json.loads(UpdateEmployee)
    print(UpdateEmployee_json)
    
#Update Employee details using PUT method
updateresponse = requests.put(updateEmployeeurl,UpdateEmployee_json)
print(updateresponse.content)

assert updateresponse.status_code == 200
#parse response as json format
updateresponse_json = json.loads(updateresponse.text)
print(updateresponse_json)
updatedempName = jsonpath.jsonpath(updateresponse_json,'employee_name')
for name in empName:
    if name == 'Employee1 Updated':
        print ('Successful Updation')
 

#####TASK 4#####        
#Deletion of record
deleteEmployeeurl = "http://dummy.restapiexample.com/api/v1/update/2"

deleteresponse = requests.delete(deleteEmployeeurl)
print(deleteresponse.status_code)