 Medical-ChatBot
An end-to-end medical chatbot leveraging Llama 2, designed to provide accurate, AI-driven healthcare assistance. This project integrates advanced NLP capabilities to answer medical queries, guide users, and offer general health advice. Includes features like user authentication, secure data handling, and dynamic responses for enhanced interaction. 

Demo
[![Watch the video](https://raw.githubusercontent.com/dhruvagrawal27/Medical-ChatBot/main/Thumbnail.png)](https://raw.githubusercontent.com/dhruvagrawal27/Medical-ChatBot/main/DemoVideo.mp4)

1. Extract Medical Data from PDF:
   - Use Python libraries like `PyPDF` to extract medical text data from PDF files.
   - Preprocess the extracted data by cleaning and formatting it for further use.

2. Embed Data with Hugging Face Model:
   - Choose an appropriate pre-trained model from Hugging Face, such as `sentence-transformers` for generating embeddings.
   - Generate vector embeddings for the extracted medical data to represent it numerically in a form suitable for storage and retrieval.

3. Store Embeddings in FAISS Index Locally:
   - Use Facebook AI Similarity Search (FAISS) to store the generated vector embeddings locally.
   - Create a FAISS index, which allows for efficient similarity searches.
   - Store these embeddings in the FAISS index on your local machine for later retrieval.

4. Load Vector Database:
   - Load the FAISS index into memory for querying during chatbot interactions.
   - Ensure that the FAISS index is preloaded when the application starts to improve performance during queries.

5. Create LLM Interface with NVIDIA Llama 2:
   - Use NVIDIA Llama 2 or a similar large language model (LLM) to process and refine chatbot queries.
   - Fine-tune the LLM for the medical domain if needed to improve its responses.
   - Design an interface to query the LLM based on relevant medical data retrieved from the FAISS index.

6. Integrate Vector Database Retrieval with LLM:
   - When the chatbot receives a query, first retrieve the most relevant vector embeddings from the FAISS index.
   - Use the retrieved embeddings as context for the LLM to generate a refined response.

7. Frontend Development with Flask:
   - Use Flask to create a simple web server for hosting the chatbot interface.
   - Implement REST API endpoints in Flask to handle user queries and interact with the LLM and FAISS index.

8. Frontend User Interface with HTML and CSS:
   - Design the frontend using HTML and CSS for a user-friendly experience.
   - Create text input forms for users to interact with the chatbot, and display responses from the backend using Flask.

9. Connect Frontend with Backend:
   - Use JavaScript (AJAX or Fetch API) to send user input from the frontend to the Flask server.
   - Display the response from the backend (LLM+FAISS) on the web page in real-time.

10. Testing and Deployment:
    - Test the entire system to ensure the data extraction, embedding, FAISS retrieval, LLM processing, and frontend interaction work smoothly.
    - Deploy the web application to a cloud platform or a local server as per your requirements.

Below is a step-by-step breakdown of the commands used in your project development, edited to be more beginner-friendly and suitable for a README file. Each command is explained clearly to ensure that new users can follow the process:

Follow these steps to set up the project and get it running on your local machine.

 1. Set up the Virtual Environment

Start by activating the virtual environment where all your project dependencies will be installed.

```
 Activate conda environment
conda activate mchatbot
```

This assumes that you've already created a conda environment named `mchatbot`. If you haven't, create one with the following command:

```
 Create a new conda environment (if not already created)
conda create --name mchatbot python=3.8
conda activate mchatbot
```

 2. Install Dependencies

Install all necessary dependencies listed in the `requirements.txt` file.

```
 Install all required Python packages
pip install -r requirements.txt
```

 3. Install Additional Libraries

Next, install specific libraries like `sentence-transformers`, `transformers`, and other necessary tools.

```
 Install sentence-transformers
pip install sentence_transformers

 Check if sentence-transformers is installed
pip show sentence-transformers

 Install Hugging Face transformers
pip install transformers huggingface-hub

 Install PyTorch (torch, torchvision, torchaudio)
pip install torch torchvision torchaudio

 Install Pinecone (for vector storage)
pip install "pinecone[grpc]"

 Install FAISS (for similarity search)
pip install faiss-cpu

 Install Weaviate (for vector database)
pip install weaviate

 Install Pydantic (for data validation)
pip install pydantic==1.10.12
```

If you face any version conflicts, try upgrading or downgrading the package versions accordingly:

```
 If needed, upgrade pydantic to a compatible version
pip install pydantic==2.5.
```

 4. Check Installed Packages

After installation, you can check if everything is correctly installed by running:

```
 List installed Python packages
pip list
```

 5. Version Control with Git

Track your changes with Git to maintain version control. Make sure you have initialized a Git repository.

```
 Add all files to the staging area
git add .

 Commit the changes
git commit -m "First commit"

 Push to the remote repository (main branch)
git push -f origin main
```

 6. Run the Application

Run the chatbot application. This will start a Flask server that serves the frontend and backend of the chatbot.

```
 Run the Flask application
python app.py
```

 7. Additional Tools (Optional)

```
 Install LangChain for LLM handling
pip install langchain

 Install LangChain with Hugging Face integration
pip install langchain-huggingface

 Install LangChain for NVIDIA AI endpoints (if needed)
pip install langchain_nvidia_ai_endpoints

 Install Flask extensions like Flask-Limiter for rate-limiting requests
pip install flask_limiter

 Install Flask-CORS for cross-origin resource sharing
pip install flask_cors
```

 8. Upgrade and Reinstall Packages (If Necessary)

Sometimes, you may need to upgrade or reinstall packages:

```
 Upgrade sentence-transformers
pip install --upgrade --force-reinstall sentence-transformers

 Upgrade Pinecone client
pip install --upgrade pinecone-client
```

 9. Networking Commands (Optional)

For troubleshooting network-related issues, you can use commands like `nslookup` and `ping` to verify server accessibility:

```
 Verify Pinecone server connection
nslookup controller.us-east-1.pinecone.io

 Ping Pinecone server to check for connectivity
ping controller.us-east-1.pinecone.io
```

 10. Uninstall Packages (If Necessary)

If you need to uninstall a package, use the following command:

```
 Uninstall a package (e.g., Pinecone-client)
pip uninstall pinecone-client
```
