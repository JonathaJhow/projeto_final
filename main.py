from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_passoword = os.getenv("DB_PASSOWORD")
api_key = os.getenv("API_KEY")

print(f"Conectando em {db_host} com usuario {db_user}")
print("Credenciais carregadas com sucesso!..g")