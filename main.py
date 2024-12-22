from src.controllers import FavoritoController
from src.migrations.migrate import migrate
from src.views.Frame import Frame


migrate()
FavoritoController.cadastrar(Frame())