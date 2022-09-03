from fastapi import UploadFile, File, APIRouter
import pandas as pd
from io import StringIO
from app.config.context import get_db, engine

router = APIRouter()

name_table = {'employees': ["id", "name", "datetime", "department_id", "job_id"],
              'departments': ["id", "department"],
              'jobs': ["id", "job"]}

@router.post("/upload/{table}", tags=["Upload Files"])
async def create_upload_file(table, file: UploadFile = File(...)):
    contents = await file.read()
    s = str(contents, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data, names=name_table[table], sep=',')
    df.to_sql(table, engine, if_exists='append', index=False, chunksize=1000)
    return {file.filename}