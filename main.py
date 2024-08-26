from src.controllers import AssuntoController
from src.daos.migrations.migrate import migrate
from src.views.Frame import Frame


migrate()
AssuntoController.abrir_seletor(Frame())