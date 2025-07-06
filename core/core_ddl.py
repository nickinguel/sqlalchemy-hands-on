from sqlalchemy import Integer, String, Table, Column, ForeignKey
from lib.global_types import DatabaseConfig


db_config: DatabaseConfig


def create_table_user_and_address():
    user_table_name = 'user_account'

    user_table = Table(
        user_table_name, 
        db_config.metadata, 
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String(100)),
    )

    address_table = Table(
        "address",
        db_config.metadata,
        Column("id", Integer, primary_key=True),
        Column("user_id", ForeignKey(f"{user_table_name}.id"), nullable=False),
        Column("email_address", String(100), nullable=False),
    )

    db_config.metadata.create_all(db_config.engine)


def init(config: DatabaseConfig):
    global db_config
    db_config = config


def main():
    create_table_user_and_address()