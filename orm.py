from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, relationship

import model


metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderid", String(255)),
    Column("sku", String(255)),
    Column("orderid", String(255))
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)