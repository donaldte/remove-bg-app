

### README.md

# Remove BG App


### Vidéo de démonstration
[![Vidéo de démonstration](https://via.placeholder.com/400x200.png?text=Video+Demo)](https://github-production-user-asset-6210df.s3.amazonaws.com/81464575/393558594-ab248908-abd4-4032-a908-6334c117d85c.mp4)



**Remove BG App** est une application web développée avec Django qui permet de supprimer l'arrière-plan des images et de personnaliser le fond avec une couleur de votre choix. Elle utilise la bibliothèque `rembg` pour le traitement d'image.

## Fonctionnalités

- **Téléchargement d'image** : Téléchargez une image depuis votre appareil.
- **Suppression d'arrière-plan** : Supprimez l'arrière-plan d'une image automatiquement.
- **Personnalisation du fond** : Ajoutez une couleur de fond personnalisée.
- **Téléchargement** : Téléchargez l'image traitée.

## Captures d'écran


### Avant traitement
![Avant traitement]![avant](https://github.com/user-attachments/assets/fca0a819-94e1-4db9-b7e5-05c808741511)


### Après traitement
![Après traitement]![apres](https://github.com/user-attachments/assets/f3f269f8-7939-41c6-80bd-ca697dd7c107)



## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/donaldte/remove-bg-app.git
   cd remove-bg-app
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```

4. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

5. Accédez à l'application sur [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Dépendances principales

- Django
- Pillow
- Rembg
- SweetAlert2

## Contribution

Les contributions sont les bienvenues ! Suivez ces étapes pour contribuer :

1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Effectuez vos modifications.
4. Faites un commit :
   ```bash
   git commit -m "Ajout de ma fonctionnalité"
   ```
5. Poussez votre branche :
   ```bash
   git push origin feature/your-feature-name
   ```
6. Ouvrez une Pull Request sur GitHub.

## Auteur

- **Donald Tedom**  
  Email : [donaldtedom0@gmail.com](mailto:donaldtedom0@gmail.com)  
  GitHub : [@donaldte](https://github.com/donaldte)

