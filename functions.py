from database import init_db, db_session
from db_model import BarChart
import datetime as dt

def getBarChart():
    init_db()
    stmt =db_session.query(BarChart).all()
    print(f"{dt.datetime.now()}:: getBarChart event execute")
    return stmt
