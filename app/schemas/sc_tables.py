from tokenize import String
from sqlalchemy.types import INTEGER, String

name_columns_csv = {'employees': ["id", "name", "datetime", "department_id", "job_id"],
              'departments': ["id", "department"],
              'jobs': ["id", "job"]}

df_schema = {"employees": {
                "id": INTEGER,
                "name": String(200),
                "datatime": String(200),
                "department_id": INTEGER,
                "job_id": INTEGER
             },
             "departments":{
                "id": INTEGER,
                "department": String(200)
             },
             "jobs":{
                "id": INTEGER,
                "job": String(200)
             }
             }
