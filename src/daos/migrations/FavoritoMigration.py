definition = ""
definition += "CREATE TABLE IF NOT EXISTS favoritos ("
definition += "id INTEGER PRIMARY KEY AUTOINCREMENT, "
definition += "nome VACHAR(63), "
definition += "url VARCHAR(255), "
definition += "assunto_id INTEGER, "
definition += "FOREIGN KEY (assunto_id) REFERENCES assuntos (id)"
definition += ")"