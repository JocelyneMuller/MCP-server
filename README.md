# MCP-Server - Weather Service

Un serveur MCP (Model Context Protocol) simple fournissant des informations météorologiques.

## Description

Ce projet implémente un serveur MCP utilisant FastMCP qui expose un outil de consultation météo. Il s'agit d'un exemple de serveur MCP qui peut être intégré avec Claude Desktop ou d'autres clients MCP.

## Fonctionnalités

### Outils disponibles

- **get_weather**: Récupère les informations météorologiques pour une localisation donnée
  - Paramètre: `location` (str) - La localisation (ville, pays, état, etc.)
  - Retourne: Informations météorologiques sous forme de texte

## Prérequis

- Python >= 3.11
- uv (gestionnaire de paquets Python)

## Installation

1. Clonez le dépôt :
```bash
git clone <url-du-repo>
cd MCP-server
```

2. Installez les dépendances :
```bash
uv pip install -e .
```

Les dépendances principales incluent :
- `fastmcp>=2.14.1`
- `mcp[cli]>=1.24.0`

## Inspection et Développement

Avant de déployer le serveur sur Claude Desktop, vous pouvez l'inspecter en mode développement :

```bash
mcp dev weather.py
```

Cette commande va :
- Générer un token de session
- Fournir un lien de serveur localhost
- Afficher les outils et ressources disponibles du serveur

Cela permet de tester et valider le serveur avant le déploiement.

## Utilisation

### Exécution du serveur

Pour lancer le serveur MCP :

```bash
python weather.py
```

### Installation comme serveur MCP

Pour installer le serveur dans votre configuration MCP :

```bash
mcp install weather.py
```

## Structure du Projet

## 🧪 Inspection et Développement

Avant de déployer le serveur sur Claude Desktop, vous pouvez l'inspecter en mode développement :

```bash
mcp dev weather.py
```

Cette commande va :
- Générer un token de session
- Fournir un lien de serveur localhost
- Afficher les outils et ressources disponibles du serveur

Cela permet de tester et valider le serveur avant le déploiement.

## ▶️ Utilisation

### Exécution du serveur

Pour lancer le serveur MCP :

```bash
python weather.py
```

### Installation comme serveur MCP

Pour installer le serveur dans votre configuration MCP :

```bash
mcp install weather.py
```

## 🏗️ Structure du Projet

```
MCP-server/
├── weather.py          # Serveur MCP principal avec l'outil météo
├── main.py            # Point d'entrée alternatif
├── pyproject.toml     # Configuration du projet et dépendances
└── README.md          # Ce fichier
```

## Code Principal

Le serveur est implémenté dans `weather.py` en utilisant le framework FastMCP :

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather") 

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    return "The weather is hot and dry"

if __name__ == "__main__":
    mcp.run()
```

## Développement

Pour étendre ce serveur :

1. Ajoutez de nouveaux outils en utilisant le décorateur `@mcp.tool()`
2. Définissez les paramètres et types de retour appropriés
3. Ajoutez une docstring descriptive pour chaque outil
4. Testez avec `mcp dev weather.py`

## Ressources

- [Documentation FastMCP](https://github.com/jlowin/fastmcp)
- [Spécification MCP](https://modelcontextprotocol.io/)
- [Claude Desktop MCP Integration](https://docs.anthropic.com/claude/docs/model-context-protocol)

## License

Ce projet est distribué sous licence open source.

## Auteur

JocelyneMuller

---

*Dernière mise à jour: Décembre 2025*
