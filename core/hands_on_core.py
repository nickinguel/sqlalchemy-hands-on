from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus
from sqlalchemy.orm import Session


mysqlPassword = quote_plus("handsOn@701")
engine = create_engine(f"mysql+pymysql://root:{mysqlPassword}@localhost:3306/sql_alchemy?charset=utf8mb4", echo=True)
# engine = create_engine("sqlite+pysqlite:///:memory:?charset=utf8mb4", echo=True)


def select_1():
    with engine.connect() as conn:  
        result = conn.execute(text("SELECT * FROM some_table")).all()
        
        for row in result:
            print("X: {}, Y: {}".format(row.x, row.y))


def select_2():
    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")

    with Session(engine) as session:
        result = session.execute(stmt, {"y": 6})

        for row in result:
            print(f"x: {row.x}  y: {row.y}")


def insert():
    global engine

    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table VALUES(:x, :y)"), 
            [{"x": 3, "y": 9}, {"x": 4, "y": 16}]   # Executemany syntax
        )
        # raise NameError()


def main():
    select_2()