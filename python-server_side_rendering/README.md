# Module de Génération d'Invitations

Ce module Python permet de générer des invitations personnalisées à partir d'un template et d'une liste de participants.

## Fonctionnalités

- Génération d'invitations personnalisées à partir d'un template
- Validation du template et des données des participants
- Gestion des valeurs manquantes (remplacées par "N/A")
- Création automatique d'un dossier pour les fichiers d'invitation
- Logging détaillé des opérations

## Installation

Clonez le repository et assurez-vous d'avoir Python 3.x installé :

```bash
git clone https://github.com/your-username/holbertonschool-higher_level_programming.git
cd python-server_side_rendering
```

## Utilisation

### Structure du Template

Le template doit contenir les placeholders suivants :
- `{name}` : Nom du participant
- `{event_title}` : Titre de l'événement
- `{event_date}` : Date de l'événement
- `{event_location}` : Lieu de l'événement

Exemple de template :
```
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```

### Format des Données

Les participants doivent être fournis sous forme de liste de dictionnaires avec les clés suivantes :
```python
attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    # ... autres participants
]
```

### Exemple d'Utilisation

```python
from task_00_intro import generate_invitations

# Lire le template depuis un fichier
with open('template.txt', 'r') as file:
    template_content = file.read()

# Liste des participants
attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    {
        "name": "Bob",
        "event_title": "Data Science Workshop",
        "event_date": "2023-08-20",
        "event_location": "San Francisco"
    }
]

# Générer les invitations
generate_invitations(template_content, attendees)
```

### Sortie

Les invitations générées seront sauvegardées dans le dossier `invitations/` avec des noms de fichiers séquentiels (`output_1.txt`, `output_2.txt`, etc.).

## Tests

Le module inclut une suite de tests unitaires complète. Pour exécuter les tests :

```bash
python -m unittest test_task_00_intro.py
```

Les tests vérifient :
- La validation du template
- La validation des données des participants
- La génération correcte des fichiers d'invitation
- La gestion des valeurs manquantes
- La gestion des cas d'erreur

## Gestion des Erreurs

Le module gère les cas d'erreur suivants :
- Template invalide ou vide
- Données de participants invalides ou incomplètes
- Valeurs manquantes dans les données (remplacées par "N/A")
- Erreurs d'écriture de fichiers

## Logging

Le module utilise le système de logging Python pour tracer les opérations :
- Niveau INFO pour les opérations réussies
- Niveau ERROR pour les erreurs
- Format : `%(asctime)s - %(levelname)s - %(message)s`

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Créer une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails. 