import cv2
import sys

def main():
    # Initialiser la capture vidéo avec la webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Essayez avec et sans CAP_DSHOW pour voir ce qui fonctionne.

    # Vérifier si la webcam est correctement ouverte
    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
        sys.exit()

    print("La webcam est ouverte. Appuyez sur 'q' pour quitter.")

    try:
        while True:
            # Lire une trame depuis la webcam
            ret, frame = cap.read()

            # Vérifier si la capture de la trame a réussi
            if not ret:
                print("Échec de la capture de la trame.")
                break

            # Afficher la trame capturée
            cv2.imshow('Test Webcam', frame)

            # Quitter si la touche 'q' est pressée
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitter l'application.")
                break

    except KeyboardInterrupt:
        print("Interruption du programme par l'utilisateur.")

    finally:
        # Libérer la capture vidéo et fermer les fenêtres
        cap.release()
        cv2.destroyAllWindows()
        print("Capture vidéo terminée et fenêtres fermées.")

if __name__ == "__main__":
    main()
