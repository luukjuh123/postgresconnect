from os import getenv

class postgresDB:
    def __init__(self, database:str = getenv("DB_DATABASE"), host:str = getenv("DB_HOST"), password:str = getenv("DB_PASSWORD"), user:str = getenv("DB_USER"), port:str = getenv("DB_PORT")):
        self.database = database
        self.host = host
        self.password = password
        self.user = user
        self.port = port
        self.engine = create_engine(f'postgresql://{self.user}:{self.password}@localhost:{self.port}/{self.database}')

    def _postgres_connect(self):
        """ Connect to the database """
        connection = psycopg2.connect(
            host = self.host,
            database = self.database,
            user - self.user,
            password = self.password,
            post = self.port
            )
        return connection
    
