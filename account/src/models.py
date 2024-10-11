from sqlalchemy import MetaData, String, Table, Column, ForeignKey

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("nameRole", String, nullable=False)
)

user = Table(
    "user",
    metadata,
    Column("lastName", String, nullable=False),  
    Column("firstName", String, nullable=False),  
    Column("fullName", String, nullable=False),  
    Column("userName", String, nullable=False),  
    Column("password", String, nullable=False), 
    Column("roles", String, ForeignKey("role.nameRole")) 
)