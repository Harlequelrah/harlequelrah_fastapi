from elrahapi.authentication.authentication_provider import AuthenticationProvider
from dotenv import load_dotenv
import os

load_dotenv()


database_username=os.getenv("DATABASE_USERNAME")
database_password = os.getenv("DATABASE_PASSWORD")
connector = os.getenv("DATABASE_CONNECTOR")
database_name = os.getenv("DATABASE_NAME")
server = os.getenv("DATABASE_SERVER")

authentication_provider = AuthenticationProvider(
    database_username=database_username,
    database_password=database_password,
    connector=connector,
    database_name=database_name,
    server=server,
)
