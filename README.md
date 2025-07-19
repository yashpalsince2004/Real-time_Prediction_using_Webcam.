# Real-Time Prediction using Webcam 🎥

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange)

This project demonstrates **real-time predictions using your webcam feed**, leveraging a trained model and computer vision techniques.
It captures live frames, preprocesses them, runs inference through a model, and overlays the predicted results on the video stream.

---

## 📂 Project Structure

```
.
├── Day10_Real-time_Prediction_using_Webcam.py  # Main Python script
├── README.md                                    # Project documentation
├── requirements.txt                            # Python dependencies
├── LICENSE                                     # MIT License
└── model/                                      # Folder to store your trained model
```

---

## 🚀 Features

✅ Captures video from your webcam in real-time.  
✅ Performs inference on each frame using a pre-trained model.  
✅ Displays predictions live on the video window.  
✅ Example of integrating OpenCV with deep learning for real-world applications.

---

## 🧰 Dependencies

Make sure you have Python 3.7+ installed.

You need the following Python libraries:
- `opencv-python`
- `tensorflow` or `keras` (depending on your model)
- `numpy`

Install them via pip:
```bash
pip install -r requirements.txt
```

---

## 📝 Usage

1️⃣ Clone this repository:
```bash
git clone https://github.com/yashpalsince2004/Real-time_Prediction_using_Webcam..git
cd real-time-webcam-prediction
```

2️⃣ Place your trained model file in the `model/` folder.  
   (Ensure the model’s path matches what is loaded in the script.)  

3️⃣ Run the script:
```bash
python Day10_Real-time_Prediction_using_Webcam.py
```

4️⃣ A window will open showing the webcam feed with predictions overlaid on the video.

---

## 🖼️ Output Example

The script will open a live webcam window like this:

```
+-------------------------+
| Webcam feed             |
|                         |
| [Prediction: Dog 🐶]   |
|                         |
+-------------------------+
```

---

## 📚 Notes

- Make sure your webcam is functional and accessible.
- If you face permissions or device errors on Linux/Mac, try running:
  ```bash
  sudo python Day10_Real-time_Prediction_using_Webcam.py
  ```
- If predictions seem wrong, double-check that the model is properly trained and matches the input preprocessing used in this script.

---

## 🤝 Contributing

Contributions are welcome!
If you find a bug, want to improve performance, or add features, feel free to open an issue or a pull request.

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

Thanks to the open-source community for tools like OpenCV, TensorFlow, and Keras which make such projects possible.

---
