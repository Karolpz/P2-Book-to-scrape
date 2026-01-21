# Books to Scrape - Web Scraper

Ce projet est un outil de Web Scraping développé en Python permettant d'extraire l'intégralité des données du site Books to Scrape. Il a été conçu comme une pipeline ETL (Extract, Transform, Load) performante pour la surveillance des prix et du catalogue.

## Fonctionnalités

- Extraction complète : Scrape l'intégralité des catégories du site.
- Données détaillées : Récupère 10 informations clés par livre (UPC, prix, stock, description, etc.).
- Scraping Parallèle : Utilisation de ThreadPoolExecutor pour une exécution optimisée.
- Gestion des Médias : Téléchargement automatique et organisation des images de couverture.
- Organisation Automatique : Export des données en fichiers CSV structurés par catégorie.

## Architecture ETL

Le projet suit une logique de pipeline de données :
1. Extract : Récupération du HTML via requests et navigation récursive (pagination).
2. Transform : Parsing avec BeautifulSoup, nettoyage des caractères spéciaux et normalisation des données.
3. Load : Stockage local structuré dans les dossiers data/ et images/.


## Prérequis

- Python 3.8 ou supérieur
- uv (gestionnaire de paquets et d'environnements)

## Installation

### 1. Installer uv
Si vous ne l'avez pas encore, installez uv :
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Cloner le projet
```bash
git clone https://github.com/Karolpz/P2-Book-to-scrape
cd P2-Book-to-scrape
```

# Activer l'environnement et installer les dépendances
```bash
uv sync
```

## Utilisation

Pour lancer le cycle complet d'extraction :
```bash
uv run python -m scrapers
```

Le script générera automatiquement les répertoires suivants :
- /data : Contient les fichiers CSV (un par catégorie).
- /images : Contient les images organisées par sous-dossiers de catégories.


## Données extraites

Pour chaque livre, les informations suivantes sont collectées :
- Titre
- Prix
- Disponibilité
- Note (Rating)
- Description
- URL de l'image

## Technologies utilisées

- Python 3.x
- uv (Gestion de projet et dépendances)
- BeautifulSoup4 (Parsing HTML)
- Requests (Requêtes HTTP)
- Concurrent.futures (Multi-threading)

Un fichier requirements.txt est également fourni à des fins de compatibilité avec les
environnements ou outils ne supportant pas encore pyproject.toml ou uv.
