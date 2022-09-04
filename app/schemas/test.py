from tokenize import String
from sqlalchemy.types import Integer, String

df_schema = {"employees": [{"id": Integer()},
             {"name": String},
             {"datatime": String},
             {"department_id": Integer()},
             {"job_id": Integer()}]
             }
