import sqlalchemy
import databases
from config import DBconfig



# # SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
# DATABASE_URL = "postgresql://epzqbkmaqhhbos:d74313ac4560b18b6a0f2a5969ece5f39e231762b06c94db7f344b91ed3d54aa@ec2-184-73-243-101.compute-1.amazonaws.com:5432/db641vr50biusv"
DATABASE_URL = f"postgresql://{DBconfig.username}:{DBconfig.password}@{DBconfig.host}/postgres"
database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL# , connect_args={"check_same_thread": False}
)

from . import(
    screeners,
)