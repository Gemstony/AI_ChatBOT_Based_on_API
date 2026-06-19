# 🍕 PizzaBot API

A simple AI-powered customer support chatbot built with Python, FastAPI, and Groq LLMs.

PizzaBot acts as a friendly pizza shop assistant that can answer customer questions, provide support, and maintain conversation context during a session.

---

## 🚀 Features

* FastAPI-powered REST API
* Groq LLM integration
* Conversation memory
* Custom system prompt
* JSON request/response format
* Easy deployment
* Swagger API documentation

---

## 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* Groq API
* Pydantic
* Uvicorn
* Python Dotenv

---

## 📂 Project Structure

```text
project/
│
├── main.py              # FastAPI application
├── .env                 # Environment variables
├── requirements.txt     # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pizzabot-api.git
cd pizzabot-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=your_groq_api_key
```

Get your API key from the Groq Console.

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 💬 Chat Endpoint

### Request

**POST** `/chat`

#### Request Body

```json
{
  "user_message": "Hello PizzaBot"
}
```

### Response

```json
{
  "bot_reply": "Hello! Welcome to our pizza shop. How can I help you today?"
}
```

---

## 🧠 Conversation Memory

PizzaBot maintains conversation history while the server is running.

Current implementation uses in-memory storage:

```python
conversation_history = []
```

Note:

* Memory resets when the server restarts.
* Not suitable for production environments.
* Database storage is recommended for persistent conversations.

---

## 🔄 Example Integration

### JavaScript

```javascript
async function sendMessage(message) {
  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user_message: message
    })
  });

  const data = await response.json();
  console.log(data.bot_reply);
}
```

---

### Python

```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={
        "user_message": "What pizzas do you offer?"
    }
)

print(response.json())
```

---

## 🔒 Production Considerations

Before deploying to production, consider adding:

* User authentication
* Database storage
* Conversation IDs
* Rate limiting
* Logging and monitoring
* Docker support
* HTTPS
* Persistent memory

---

## 🚀 Future Improvements

* Multi-user conversations
* Database-backed chat history
* RAG (Retrieval-Augmented Generation)
* PDF knowledge base
* Streaming responses
* WebSocket support
* Admin dashboard
* Analytics

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed with Python, FastAPI, and Groq LLMs.

If you found this project useful, consider giving it a ⭐ on GitHub.
