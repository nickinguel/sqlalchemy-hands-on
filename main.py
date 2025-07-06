from sqlalchemy import create_engine, MetaData
from urllib.parse import quote_plus
from lib.global_types import DatabaseConfig

mysqlPassword = quote_plus("handsOn@701")
engine = create_engine(f"mysql+pymysql://root:{mysqlPassword}@localhost:3306/sql_alchemy?charset=utf8mb4", echo=True)
# engine = create_engine("sqlite+pysqlite:///:memory:?charset=utf8mb4", echo=True)

db_config = DatabaseConfig(engine, MetaData())


def init(config: DatabaseConfig):
    global local_engine
    local_engine = config.engine


def main_core_hands_on():
    from core.hands_on_core import main, init
    
    init(db_config)
    main()


def main_core_dll():
    from core.core_ddl import main, init
    
    init(db_config)
    main()

# core_dll_main()
main_core_dll()