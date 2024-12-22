definition = """
create table if not exists favoritos (
    id integer not null primary key,
    nome varchar (32) not nul unique,
    url varchar (255) not null unique
)
"""