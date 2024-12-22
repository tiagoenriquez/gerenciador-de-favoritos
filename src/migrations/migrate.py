from src.connections.DatabaseConnection import con
from src.migrations import FavoritoMigration


def migrate():
    with con:
        con.execute(FavoritoMigration.definition)
        con.commit()