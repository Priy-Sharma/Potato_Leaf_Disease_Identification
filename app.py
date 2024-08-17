import os
import io
from flask import Flask, render_template, request, redirect, jsonify
from PIL import Image, UnidentifiedImageError
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Define the static folder path
STATIC_FOLDER = './static'
app.config['STATIC_FOLDER'] = STATIC_FOLDER


# Load the latest model version dynamically
def load_latest_model():
    models_dir = "./tf_Models"
    files = os.listdir(models_dir)

    numeric_versions = []
    for file in files:
        try:
            version = int(file.split('.')[0])
            numeric_versions.append(version)
        except ValueError:
            pass

    if not numeric_versions:
        raise FileNotFoundError("No models found in the directory.")

    latest_version = max(numeric_versions)
    model_path = os.path.join(models_dir, f"{latest_version}.keras")
    model = tf.keras.models.load_model(model_path)
    return model


MODEL = load_latest_model()
CLASS_NAMES = ['Early Blight', 'Late Blight', 'Healthy']

# Update image processing parameters
IMAGE_SIZE = 256
MAX_FILE_SIZE_MB = 50
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


def process_image(file, max_size=(IMAGE_SIZE, IMAGE_SIZE), quality=85) -> io.BytesIO:
    try:
        image = Image.open(file)
        image = image.convert('RGB')  # Ensure it's in RGB format

        # Resize the image
        image.thumbnail(max_size)  # Resize while maintaining aspect ratio

        # Create an in-memory file object for the compressed image
        in_memory_file = io.BytesIO()
        image.save(in_memory_file, format='JPEG', quality=quality)
        in_memory_file.seek(0)  # Reset file pointer to the beginning

        return in_memory_file
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")


def read_file_as_image(file) -> np.ndarray:
    try:
        image = Image.open(file)
        image = image.convert('RGB')  # Ensure it's in RGB format
        image = image.resize((IMAGE_SIZE, IMAGE_SIZE))  # Resize to 256x256
        image_array = np.array(image)
        return image_array
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")


@app.route('/')
def get_interface():
    return render_template("index.html")


@app.route('/upload')
def upload_page():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    # Check file size
    if file.content_length > MAX_FILE_SIZE_BYTES:
        return jsonify({"error": f"File size exceeds {MAX_FILE_SIZE_MB} MB limit."})

    if file:
        try:
            # Process and compress the uploaded file
            processed_image = process_image(file)

            # Save the processed image to the static folder
            destination_path = os.path.join(app.config['STATIC_FOLDER'], "1.jpg")
            with open(destination_path, 'wb') as f:
                f.write(processed_image.read())

            print("Image uploaded and processed successfully")

            # Process the image for prediction
            image = read_file_as_image(destination_path)
            img_batch = np.expand_dims(image, 0)  # Add batch dimension

            prediction = MODEL.predict(img_batch)  # Make prediction
            predicted_class = CLASS_NAMES[np.argmax(prediction[0])]  # Get the class with highest probability
            confidence = np.max(prediction[0])  # Get the confidence level

            final = {
                "class": predicted_class,
                "confidence": round(float(confidence) * 100, 2)
            }
            return render_template("result.html", result_dict=final)

        except UnidentifiedImageError:
            return jsonify({"error": "Cannot identify image file. Please upload a valid image."})
        except ValueError as ve:
            return jsonify({"error": str(ve)})
        except Exception as e:
            return jsonify({"error": f"An unexpected error occurred: {str(e)}"})


@app.route('/info_page')
def info_page():
    return render_template("information.html")


if __name__ == '__main__':
    app.run(debug=True)

