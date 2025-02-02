"""•	17. Define an abstract class `IDatabaseOperations` 
with methods `insert()`, `update()`, and `delete()`.
 Implement this in `SQLDatabase` and `NoSQLDatabase`."""

from abc import ABC,abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self,data):
        pass
    @abstractmethod
    def update(self,data1):
        pass
    @abstractmethod
    def delete(self,data_id):
        pass
    
class SQLDatabase(IDatabaseOperations):        
    def insert(self,data):
        return f'SQL database inserted {data} performed '
    
    def update(self,data1):
        return f'SQL database updated {data1} performed '
    
    def delete(self,data_id):
        return f'SQL database deleted {data_id} performed'
    
class NoSQLDatabase(IDatabaseOperations):
    def insert(self,data):
        return f'NOSQL database inserted {data} performed'
    def update(self,data1):
        return f'NOSQL database updated {data1} performed'
    def delete(self,data_id):
        return f'NOSQL database deleted {data_id} performed'

data=input("enter data : ")
data1=input("enter data to update: ")
data_id=input("Enter data to delete: ")
sqldatabase=SQLDatabase()
print(sqldatabase.insert(data))
print(sqldatabase.update(data1))
print(sqldatabase.delete(data_id))

nosqldatabase=NoSQLDatabase()
print(nosqldatabase.insert(data))
print(nosqldatabase.update(data1))
print(nosqldatabase.delete(data_id))