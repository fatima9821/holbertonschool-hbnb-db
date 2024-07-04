FROM python:3.12.3-slim

# Installer les dépendances nécessaires
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt /tmp/requirements.txt

# Installer les dépendances Python
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
  && rm -rf /tmp

# Copier le reste de l'application
COPY . .

# Définir les variables d'environnement
ENV PORT=5000
ENV DATABASE_URL=sqlite:///development.db
ENV JWT_SECRET_KEY=your_secret_key

# Exposer le port de l'application
EXPOSE $PORT

# Commande pour exécuter l'application
CMD ["gunicorn", "hbnb:app", "-w", "2", "-b", "0.0.0.0:$PORT"]

