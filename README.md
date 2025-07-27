## **MLOps Pipeline – Summary**

This project sets up a complete MLOps workflow to predict housing prices in California. It integrates various tools and frameworks to demonstrate both traditional and deep learning approaches.

### **Core Components Used**

* **Scikit-learn** for implementing a Linear Regression model
* **PyTorch** for building and training a Neural Network
* **Docker** for creating a containerized environment
* **GitHub Actions** for automating CI/CD processes
* **Manual quantization techniques** for reducing model size

---

### **Project Resources**

* **GitHub Repository**: https://github.com/G24AI1036/housing-predictor
* **Docker Image**: https://hub.docker.com/r/g24ai1036/mlops-pipeline

---

### **Branch Overview**

* **`main`**: Contains base setup and documentation
* **`dev`**: Focuses on model development and training workflows
* **`docker_ci`**: Includes Dockerfile and CI/CD integration setup
* **`quantization`**: Contains scripts for model compression and optimization

---

### **Steps to Get Started**

1. Clone the GitHub repository
2. Install required packages using:

   ```bash
   pip install -r requirements.txt
   ```
3. Train the model by running:

   ```bash
   python src/train.py
   ```
4. Create the Docker image using:

   ```bash
   docker build -t housing-predictor .
   ```
5. Start a Docker container and run inference:

   ```bash
   docker run housing-predictor python src/predict.py
   ```

---

### **Performance Comparison**

| **Evaluation Metric** | **Scikit-learn Model** | **Quantized Model** |
| --------------------- | ---------------------- | ------------------- |
| R² Score              | 0.6053                 | 0.6051              |
| Model File Size       | 0.41 KB                | 0.32 KB             |


