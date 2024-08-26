from src.daos.connection import con
from src.daos.migrations import AssuntoMigration, FavoritoMigration


def migrate() -> None:
    with con:
        cur = con.execute(AssuntoMigration.definition)
        cur.execute(FavoritoMigration.definition)