from setuptools import find_packages, setup

setup(
    name = 'Medical Chatbot',
    version= '0.0.0',
    author= 'Dhruv Agrawal',
    author_email= 'thehackerschoice1@gmail.com',
    packages= find_packages(),
    install_requires = ["ctransformers==0.2.5","sentence-transformers==2.2.2","pinecone-client==2.2.4","langchain==0.0.225","flask","pypdf",
                        "python-dotenv","faiss-cpu","langchain_nvidia_ai_endpoints"]
)