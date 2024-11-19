from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Pinecone
from langchain_nvidia_ai_endpoints import ChatNVIDIA

app = Flask(__name__)

load_dotenv()
NVIDIA_API_KEY = os.environ.get('NVIDIA_API_KEY')


embeddings = download_hugging_face_embeddings()

index_name="medical-bot"

#Loading the index
docsearch = FAISS.load_local(r"F:\Medical-ChatBot\research\faiss_index", embeddings,allow_dangerous_deserialization=True)


PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
 
chain_type_kwargs={"prompt": PROMPT}

llm = ChatNVIDIA(
  model="meta/llama2-70b",
  api_key=NVIDIA_API_KEY, 
  temperature=0.7,
  top_p=1,
  max_tokens=256,
)


qa=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

