from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
import pandas as pd
from app.config.context import get_db, engine
import pandavro as pdx


router = APIRouter()

@router.get("/backup/{table}", tags=["backup"])
async def backup(table, db: session = Depends(get_db)):
    return pdx.to_avro(table + '.avro', pd.read_sql_table(table, engine))

@router.get("/restore/{table}", tags=["Restore Table"])
async def restore(table, db: session = Depends(get_db)):
    cdd = pdx.read_avro(table + '.avro')
    cdd.to_sql(table, engine, if_exists='replace', index=False, chunksize=1000)
    return 'succetful'