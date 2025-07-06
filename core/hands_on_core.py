from sqlalchemy import text
from sqlalchemy.orm import Session
from lib.global_types import DatabaseConfig


db_config: DatabaseConfig

def init(config: DatabaseConfig):
    global db_config
    db_config = config


def select_1():
    with db_config.engine.connect() as conn:  
        result = conn.execute(text("SELECT * FROM some_table")).all()
        
        for row in result:
            print("X: {}, Y: {}".format(row.x, row.y))


def select_2():
    stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")

    with Session(db_config.engine) as session:
        result = session.execute(stmt, {"y": 6})

        for row in result:
            print(f"x: {row.x}  y: {row.y}")


def insert():
    global db_config

    with db_config.engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table VALUES(:x, :y)"), 
            [{"x": 3, "y": 9}, {"x": 4, "y": 16}]   # Executemany syntax
        )
        # raise NameError()


def update():
    with Session(db_config.engine) as session:
        result = session.execute(
            text("UPDATE some_table SET y=:y WHERE x=:x"),
            [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
        )
        print(result)

        session.commit()

def main():
    select_1()