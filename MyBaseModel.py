
from typing import Dict, Tuple
from db import DB
class MyBaseModel ():
    def __init__(self,*,id:int|None=None,fields: Dict[str, str]| None = None):
        self.db=DB()
        if(id):
            query = f"""
            SELECT * FROM {self.table} 
            WHERE id = {id}
            """
            data = self.db.call_from_db(query)
            
            for i,value in enumerate(data[0]):
                setattr(self,self.fields[i] , str(value))
            self.id=id
            
        if(fields):
            for key, val in fields.items():
                setattr(self,key , val)

    def __del__(self):
        self.db.conn_close()

    @classmethod
    def getAll(cls, *, where: Tuple[str, str] | None = None):
        tbl=cls.table
        query = f"""
        SELECT * FROM {tbl} 
        """
        if where:
            key, val = where
            where_query = f"""
            WHERE {key} = {val}
            """
            query = query + where_query
        db=DB()
        data = db.call_from_db(query)
        return data
    
    def get(self):
        fieldsDict={}
        for key in self.fields:
            fieldsDict[key]=getattr(self,key)
        
        return fieldsDict

    

    def delete(self):
        delete_query = f"""
        DELETE FROM {self.table} WHERE id = {self.id}
        """
        self.db.call_from_db(delete_query)

    def update(self,*,update: Dict[str, str]| None = None):
        
        if(update):
            for key, val in update.items():
                setattr(self,key , val)
        
        field_query = ""
        for field in self.fields:
            if field!="id":
                field_query+=f"{field}='{getattr(self,field)}',"
        field_query = field_query[:-1]
        
        update_query = f"""
        UPDATE {self.table} SET {field_query} WHERE id = {self.id}
        """
        self.db.call_from_db(update_query)
    
    def insert(self):
        keys = ",".join(self.fields)
        values_array=[]
        for field in self.fields:
            values_array.append(getattr(self,field))

        values = "','".join(values_array)

        query = f"""
        INSERT INTO {self.table} (
            {keys}
        ) VALUES (
            '{values}'
        )
        """
        return self.db.call_from_db(query)
    