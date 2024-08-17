<h1>Potato Leaf Disease Identification</h1>
<p>This project aims to assist farmers and agriculturists in identifying diseases affecting potato leaves by using image recognition technology. Users can upload an image of a potato leaf, and the system will predict the type of disease and suggest preventive measures to help mitigate the issue. The project also provides information on common potato leaf diseases, their impact, and possible solutions.</p>

<h2>Table of Contents</h2>
    <ul>
        <li><a href="#project-overview">Project Overview</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#technologies-used">Technologies Used</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#dataset">Dataset</a></li>
        <li><a href="#model-training">Model Training</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>

 <h2 id="project-overview">Project Overview</h2>
<p>The "Potato Leaf Disease Identification" project uses deep learning to detect and classify potato leaf diseases from images. The project has the following components:</p>
    <ol>
        <li>A webpage interface for users to learn more about common potato leaf diseases.</li>
        <li>An image upload feature that allows users to upload a photo of their potato plant, after which a trained machine learning model identifies the disease.</li>
        <li>Information and resources on disease prevention and treatment.</li>
    </ol>

<h2 id="features">Features</h2>
    <ul>
        <li><strong>Know More</strong>: Provides detailed information about various potato leaf diseases, including their symptoms, impact, and prevention.</li>
        <li><strong>Disease Prediction</strong>: Upload an image of the leaf to get a prediction of whether it’s diseased and the type of disease.</li>
        <li><strong>Disease Treatment Suggestions</strong>: After the disease is identified, the system provides tips on how to treat and prevent the spread of the disease.</li>
        <li><strong>Responsive Design</strong>: The web interface is designed to work seamlessly on both desktops and mobile devices.</li>
    </ul>

<h2 id="technologies-used">Technologies Used</h2>
    <ul>
        <li><strong>Backend</strong>: Python, Flask (for API and model serving)</li>
        <li><strong>Frontend</strong>: HTML, CSS (for the user interface)</li>
        <li><strong>Machine Learning</strong>: TensorFlow/Keras (for training the leaf disease detection model)</li>
        <li><strong>Image Processing</strong>:  PIL (for image handling and preprocessing)</li>
    </ul>

<h2 id="installation">Installation</h2>
<p>Follow these steps to set up the project locally:</p>
    <ol>
        <li><strong>Clone the repository</strong>:
            <pre><code>git clone https://github.com/Priy-Sharma/Potato-Disease-Identification.git</code></pre>
        </li>
        <li><strong>Set up a virtual environment</strong> (optional but recommended):
            <pre><code>python3 -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate</code></pre>
        </li>
        <li><strong>Install required packages</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the web application</strong>:
            <pre><code>flask run   # Or, for Django, use python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the application</strong> by opening <a href="http://127.0.0.1:5000/" target="_blank">http://127.0.0.1:5000/</a> in your web browser.</li>
    </ol>

<h2 id="usage">Usage</h2>

<h3 id="know-more-about-diseases">Know More About Diseases</h3>
<p>Click the <strong>"Learn About Diseases"</strong> button on the homepage to be redirected to a page that provides detailed information about various types of potato leaf diseases, their symptoms, effects on the plant, and preventive measures.</p>

<h3 id="identify-your-plant-disease">Identify Your Plant Disease</h3>
<p>To identify a potential disease in your potato plant:</p>
<ol>
    <li>Click the <strong>"Diagnose Your Plant"</strong> button.</li>
    <li>Upload a clear image of the potato leaf.</li>
    <li>The model will analyze the image and provide a prediction, along with the type of disease (if any) and suggestions for treatment.</li>
</ol>

<h2 id="dataset">Dataset</h2>
<p>The model is trained on a dataset of potato leaf images with various diseases. The dataset contains labeled images of common diseases such as:</p>
<ul>
    <li><strong>Early Blight</strong></li>
    <li><strong>Late Blight</strong></li>
    <li><strong>Healthy Leaves</strong></li>
</ul>
<p>You can use publicly available datasets like the <strong>PlantVillage dataset</strong> or create your own dataset by collecting and labeling images.</p>

<h2 id="model-training">Model Training</h2>
<p>The model used for predicting diseases is a Convolutional Neural Network (CNN) built using <strong>Keras</strong> and trained on labeled leaf images. Here is a basic outline of how the model is trained:</p>
<ol>
    <li><strong>Preprocessing</strong>: Images are resized, normalized, and augmented to create a robust training set.</li>
    <li><strong>Model Architecture</strong>: A CNN is designed to extract features from the images and classify them into one of the disease categories.</li>
    <li><strong>Training</strong>: The model is trained using a training dataset and validated on a separate validation set to measure accuracy.</li>
</ol>
<p>To train the model, run:</p>
<pre><code>python Potato_Leaf_Disease_Identifier.ipynb</code></pre>
<p>The trained model will be saved in the <code>tf_Models/</code> directory with a version number.</p>

<h2 id="contributing">Contributing</h2>
<p>I welcome contributions from the community! To contribute:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or bug fix.</li>
    <li>Submit a pull request with a clear description of your changes.</li>
</ol>


<h2 id="contact">Contact</h2>
<p>For any inquiries, feel free to reach out:</p>
<ul>
    <li><strong>Email</strong>: <a>"asharmapriyanka2000@gmail.com"</a></li>
    <li><strong>GitHub</strong>: <a>https://github.com/Priy-Sharma/</a>
