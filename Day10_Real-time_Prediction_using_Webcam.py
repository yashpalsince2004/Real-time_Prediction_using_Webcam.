import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("mnist_cnn_model.h5")  # ya koi custom model

# Class names (digits/class labels)
class_names = [str(i) for i in range(10)]  # 0-9 ke liye

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # ROI select karo (central part)
    roi = frame[100:300, 100:300]  # you can adjust this
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(gray, (28, 28))
    img = 255 - img  # invert
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    # Predict
    pred = model.predict(img)
    predicted_class = np.argmax(pred)

    # Display result
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)
    cv2.putText(frame, f'Predicted: {class_names[predicted_class]}',
                (100, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Webcam Real-time Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
