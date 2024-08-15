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
