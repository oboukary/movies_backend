"""
Configuration de la base de données
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"
# Créer un moteur de base de données (ici le moteur c'est du SQLITE) qui établit la connection
# avec notre vase de données movies.db
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# Crée une session pour interagir avec la base de données avec SessionLocal 
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base : Classe de base qui sert à déclarer tous vos modèles.
Base = declarative_base()

if __name__=='__main__':
  try:
    with  engine.connect() as conn:
      print("Connection à la base réussie")
  except Exception as e:
    print(f"Connection échoue: {e}")
