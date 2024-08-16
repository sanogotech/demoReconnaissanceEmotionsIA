import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Essayez avec et sans CAP_DSHOW pour voir ce qui fonctionne.

if not cap.isOpened():
    print("Erreur: Impossible d'accéder à la webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Échec de la capture de la trame")
        break

    cv2.imshow('Test Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
