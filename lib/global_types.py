from sqlalchemy import Engine, MetaData


class DatabaseConfig:

    def __init__(self, engine: Engine, meta: MetaData):
        self.engine = engine
        self.metadata = meta
