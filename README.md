# demoReconnaissanceEmotionsIA


### **Titre : Reconnaissance des Émotions en Temps Réel avec Python, OpenCV et FER**

---

### **Introduction**

La reconnaissance des émotions en temps réel est une technologie innovante qui permet d'analyser les expressions faciales pour identifier les émotions ressenties par une personne. Cette technologie trouve des applications variées, notamment dans l'amélioration de l'expérience utilisateur, la sécurité, et le marketing. En combinant Python, OpenCV, et la bibliothèque FER (Facial Expression Recognition), il est possible de créer un système efficace capable de détecter et d'afficher les émotions en temps réel à partir d'une vidéo capturée par une webcam.

Dans ce projet, nous allons implémenter une solution complète de reconnaissance des émotions en temps réel, incluant la détection de visages multiples, le suivi des émotions et la visualisation des données collectées.

---

### **Mini Backlog du Projet**

**Objectifs :**

1. **Configurer l'environnement de développement** : Installation des bibliothèques Python nécessaires (OpenCV, FER).
2. **Développer un système de capture vidéo** : Utiliser OpenCV pour accéder à la webcam et capturer des images en temps réel.
3. **Implémenter la détection des émotions** : Utiliser la bibliothèque FER pour analyser les expressions faciales et identifier les émotions.
4. **Gérer plusieurs visages** : Assurer que le système peut détecter et analyser les émotions de plusieurs visages simultanément.
5. **Afficher les émotions en temps réel** : Superposer les émotions détectées sur le flux vidéo en direct.
6. **Enregistrer et analyser les données émotionnelles** : Stocker les émotions détectées pour une analyse ultérieure, avec la possibilité de visualiser les tendances au fil du temps.
7. **Optimisation et débogage** : S'assurer que le système fonctionne de manière fluide et précise, avec un temps de réponse minimal.

---

### **1. Mise en Place de l'Environnement**

Assurez-vous que Python est installé sur votre système et installez les bibliothèques requises :

```bash
pip install opencv-python
pip install fer
pip install matplotlib  # Pour la visualisation des résultats
```

### **2. Importer les Bibliothèques Nécessaires**

```python
import cv2
from fer import FER
import time
import numpy as np
import matplotlib.pyplot as plt
```

### **3. Accéder à la Webcam**

```python
cap = cv2.VideoCapture(0)
```

### **4. Initialiser le Détecteur FER**

```python
emotion_detector = FER(mtcnn=True)  # MTCNN pour une meilleure précision
```

### **5. Reconnaissance des Émotions en Temps Réel avec Visages Multiples et Journalisation**

```python
# Stocker les émotions détectées
emotion_log = []

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Échec de la capture de la trame")
            break

        # Détecter les émotions sur la trame actuelle
        emotion_data = emotion_detector.detect_emotions(frame)

        for face in emotion_data:
            bounding_box = face["box"]
            emotions = face["emotions"]

            # Obtenir l'émotion dominante
            dominant_emotion, score = max(emotions.items(), key=lambda item: item[1])

            # Dessiner un rectangle autour du visage
            x, y, w, h = bounding_box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Afficher le texte avec l'émotion dominante
            text = f"{dominant_emotion} ({score:.2f})"
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

            # Enregistrer les émotions détectées
            emotion_log.append(emotions)

        # Afficher la trame avec les émotions détectées
        cv2.imshow('Reconnaissance des Émotions en Temps Réel', frame)

        # Appuyez sur 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Libérer la webcam et fermer la fenêtre
    cap.release()
    cv2.destroyAllWindows()

    # Optionnel : Visualiser les émotions enregistrées au fil du temps
    if emotion_log:
        # Agréger les émotions sur toutes les trames
        aggregated_emotions = {emotion: 0 for emotion in emotion_log[0].keys()}
        for log in emotion_log:
            for emotion, score in log.items():
                aggregated_emotions[emotion] += score
        
        # Visualisation
        emotions, scores = zip(*aggregated_emotions.items())
        plt.figure(figsize=(10, 6))
        plt.bar(emotions, scores, color='skyblue')
        plt.title('Scores Émotionnels Agrégés au Fil du Temps')
        plt.show()
```

### **6. Explications des Améliorations**

- **Gestion des Visages Multiples :** Le code détecte et traite plusieurs visages dans chaque trame. Chaque visage est analysé pour les émotions, et l'émotion dominante est affichée.
  
- **Journalisation des Émotions :** Les émotions détectées dans chaque trame sont enregistrées dans une liste (`emotion_log`). Ces données peuvent être utilisées ultérieurement pour une analyse, comme la visualisation des tendances émotionnelles au fil du temps.

- **Affichage Optimisé :** Le programme dessine efficacement des rectangles autour des visages et superpose le texte pour afficher l'émotion dominante détectée pour chaque visage.

- **Gestion des Erreurs :** Le code vérifie si une trame est capturée avec succès. Si ce n'est pas le cas, il se ferme proprement avec un message d'erreur.

- **Visualisation Optionnelle :** Après la fin du flux vidéo, les émotions agrégées au fil du temps peuvent être visualisées sous forme de graphique à barres pour montrer la prévalence de chaque émotion pendant la session.

### **Conclusion**

Ce projet offre une solution complète de reconnaissance des émotions en temps réel, avec des fonctionnalités avancées comme la gestion des visages multiples, la journalisation des émotions, et la visualisation des tendances. Il peut être utilisé dans diverses applications allant de l'amélioration de l'expérience client à la surveillance et à l'analyse comportementale.
