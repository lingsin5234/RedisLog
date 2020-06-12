# this file sets up the classes for the datasets and database
from sqlalchemy import Table, Column, Integer, String, Boolean, MetaData, ForeignKey, create_engine

metadata = MetaData()

# manual load receipts table
mnl_load_receipt = Table('mnl_load_receipt', metadata,
                         Column('Id', Integer, primary_key=True),
                         Column('customer_id', Integer),
                         Column('image_name', String),
                         Column('container_name', String),
                         Column('processed_bool', Boolean),
                         Column('timestamp', String))

# setup engine and database
engine = create_engine('sqlite:///receipts.db', echo=True)

# safe to call multiple times as it will FIRST check for table presence
metadata.create_all(engine)
