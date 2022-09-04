from fastapi import UploadFile, File, APIRouter
import pandas as pd
from io import StringIO
from app.config.context import get_db, engine
from app.schemas.sc_tables import df_schema, name_columns_csv

router = APIRouter()



@router.post("/upload/{table}", tags=["Upload Files"])
async def create_upload_file(table, file: UploadFile = File(...)):
    contents = await file.read()
    s = str(contents, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data, names=name_columns_csv[table], sep=',')
    df.to_sql(table, engine, if_exists='append', index=False, chunksize=1000, dtype=df_schema[table])
    return {file.filename}