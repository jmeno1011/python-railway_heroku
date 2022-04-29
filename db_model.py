from sqlalchemy import Column, String, Integer
from database import Base, init_db

class BarChart(Base):
    __tablename__="barchart"
    City = Column(String, primary_key=True)
    state = Column(String)
    Population2010 = Column(Integer)
    Population2000 = Column(Integer)

    def __init__(self, city, state, population2010, population2000):
        self.City = city
        self.state = state
        self.Population2010 = population2010
        self.Population2000 = population2000

    def __repr__(self):
        return "%s, %s, %d, %d"% (self.City, self.state, self.Population2010, self.Population2000)

init_db()
