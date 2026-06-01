import os
import sys
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_ollama import ChatOllama

# Load environment variables from .env file
load_dotenv()

def test_ollama():
    print("\n" + "="*50)
    print("🤖 Testing Local Ollama Model")
    print("="*50)
    
    model_name = os.getenv("OLLAMA_MODEL", "qwen")
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    
    print(f"Connecting to Ollama at {base_url} using model: '{model_name}'...")
    
    try:
        # Initialize modern ChatOllama from langchain-ollama
        llm = ChatOllama(
            model=model_name,
            base_url=base_url,
            temperature=0.7,
        )
        
        messages = [
            SystemMessage(content="You are a helpful and concise assistant."),
            HumanMessage(content="Explain quantum computing in one sentence.")
        ]
        
        print("\nSending prompt: 'Explain quantum computing in one sentence.'")
        print("Waiting for local response...")
        
        response = llm.invoke(messages)
        print("\n✨ Ollama Response:")
        print(response.content)
        
    except Exception as e:
        print(f"\n❌ Error connecting to Ollama: {e}")
        print("\n💡 Tips for Ollama:")
        print("1. Download and run Ollama from https://ollama.com/")
        print(f"2. Pull the model in your terminal:  ollama pull {model_name}")
        print("3. Ensure the Ollama background service is running.")

def test_huggingface():
    print("\n" + "="*50)
    print("🤗 Testing Hugging Face Serverless Inference API")
    print("="*50)
    
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not hf_token or "your_huggingface_api_token" in hf_token:
        print("\n❌ Error: HUGGINGFACEHUB_API_TOKEN is missing or not set in the .env file.")
        print("Please edit the '.env' file in this directory and replace 'your_huggingface_api_token_here' with your real API token.")
        return
        
    # We will use Qwen/Qwen2.5-72B-Instruct as a powerful and free serverless instruct model
    # Another excellent free option: meta-llama/Meta-Llama-3-8B-Instruct
    repo_id = "Qwen/Qwen2.5-72B-Instruct"
    
    print(f"Initializing Hugging Face Endpoint for repo: '{repo_id}'...")
    
    try:
        # Initialize modern HuggingFaceEndpoint from langchain-huggingface
        llm = HuggingFaceEndpoint(
            repo_id=repo_id,
            max_new_tokens=512,
            temperature=0.7,
            huggingfacehub_api_token=hf_token,
        )
        
        # Wrap it with ChatHuggingFace to format prompt/messages appropriately for chat
        chat_model = ChatHuggingFace(llm=llm)
        
        messages = [
            SystemMessage(content="You are a creative assistant."),
            HumanMessage(content="Write a short, engaging 2-line poem about coding at midnight.")
        ]
        
        print("\nSending prompt: 'Write a short, engaging 2-line poem about coding at midnight.'")
        print("Waiting for serverless API response...")
        
        response = chat_model.invoke(messages)
        print("\n✨ Hugging Face Response:")
        print(response.content)
        
    except Exception as e:
        print(f"\n❌ Error calling Hugging Face: {e}")
        print("\n💡 Tips for Hugging Face:")
        print("1. Ensure your Hugging Face API key is correct in '.env'.")
        print("2. Ensure the model supports the free serverless Inference API.")

def main():
    print("="*50)
    print("🌟 LangChain Integration Starter 🌟")
    print("="*50)
    print("1: Test local Ollama model")
    print("2: Test Hugging Face Inference API")
    print("3: Test both")
    print("4: Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        test_ollama()
    elif choice == "2":
        test_huggingface()
    elif choice == "3":
        test_ollama()
        test_huggingface()
    else:
        print("Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
