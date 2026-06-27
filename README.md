�# 📝 FastAPI Todo API

A complete CRUD (Create, Read, Update, Delete) API for managing todos, built with FastAPI and Python.

## 🚀 Features

- ✅ Create new todos
- 📋 Get all todos
- 🔍 Get a specific todo by ID
- ✏️ Update existing todos
- ❌ Delete todos
- 📚 Interactive API documentation (Swagger UI)
- 🧪 Automatic data validation with Pydantic
- ⚡ Fast and asynchronous
- 🔒 Type safety with Python type hints

## 🛠️ Tech Stack

- **FastAPI** - Modern web framework for building APIs
- **Python 3+** - Programming language
- **Pydantic** - Data validation library
- **Uvicorn** - ASGI server for running FastAPI
- **Swagger UI** - Interactive API documentation

## 📁 Project Structure

```

todo-api/
│
├── main.py                 # Main application code
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore rules

```

## 🔧 Installation & Setup

### Prerequisites
- Python 3 or higher installed
- Git installed
- A code editor (VS Code recommended)

### Step 1: Clone the repository
```bash
git clone https://github.com/asundah/fastapi-todo-api.git
cd fastapi-todo-api
```

Step 2: Create and activate virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

Step 4: Run the server

```bash
uvicorn main:app --reload
```

Step 5: Open in browser

· API Documentation: http://localhost:8000/docs
· Alternative Docs: http://localhost:8000/redoc
· Root Endpoint: http://localhost:8000

📡 API Endpoints

Method Endpoint Description Request Body
POST /todos Create a new todo {"title": "string", "completed": false}
GET /todos Get all todos -
GET /todos/{id} Get a specific todo by ID -
PUT /todos/{id} Update an existing todo {"title": "string", "completed": true}
DELETE /todos/{id} Delete a todo by ID -

Detailed Endpoint Information

POST /todos

Create a new todo item.

Request Body:

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

Response (201 Created):

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

GET /todos

Retrieve all todo items.

Response (200 OK):

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  },
  {
    "id": 2,
    "title": "Build a project",
    "completed": true
  }
]
```

GET /todos/{id}

Retrieve a specific todo by its ID.

Response (200 OK):

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

Error Response (404 Not Found):

```json
{
  "error": "Todo not found"
}
```

PUT /todos/{id}

Update an existing todo.

Request Body:

```json
{
  "title": "Learn FastAPI completely",
  "completed": true
}
```

Response (200 OK):

```json
{
  "id": 1,
  "title": "Learn FastAPI completely",
  "completed": true
}
```

DELETE /todos/{id}

Delete a todo by its ID.

Response (200 OK):

```json
{
  "message": "Todo deleted successfully"
}
```

🧪 Testing the API

Method 1: Using Swagger UI (Easiest)

1. Open http://localhost:8000/docs
2. Click on any endpoint
3. Click "Try it out"
4. Enter the required data
5. Click "Execute"
6. View the response

Method 2: Using curl (Command Line)

Create a todo:

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "completed": false}'
```

Get all todos:

```bash
curl http://localhost:8000/todos
```

Get a specific todo:

```bash
curl http://localhost:8000/todos/1
```

Update a todo:

```bash
curl -X PUT http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI completely", "completed": true}'
```

Delete a todo:

```bash
curl -X DELETE http://localhost:8000/todos/1
```

Method 3: Using Postman

1. Download Postman
2. Create a new request
3. Set the method and URL
4. For POST/PUT, add body as JSON
5. Send and view response

📊 Data Models

TodoCreate Model

Field Type Required Description
title string Yes The todo title
completed boolean No Completion status (default: false)

TodoResponse Model

Field Type Description
id integer Unique todo identifier
title string The todo title
completed boolean Completion status

🚀 Deployment Options

Deploy to Render (Free)

1. Push code to GitHub
2. Go to render.com
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   · Build Command: pip install -r requirements.txt
   · Start Command: uvicorn main:app --host 0.0.0.0 --port 10000
6. Click "Create Web Service"

Deploy to Heroku

1. Create a Procfile:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
2. Push to Heroku:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

Deploy to PythonAnywhere

1. Upload your code via the web interface
2. Create a Web app
3. Set the WSGI configuration file to point to your FastAPI app

🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

📝 License

This project is open source and available under the MIT License.

👨‍💻 Author

Amos Asunda

· GitHub: @asundah

🙏 Acknowledgments

· FastAPI - The amazing framework
· Pydantic - Data validation
· Swagger UI - Interactive documentation

📊 API Statistics

Statistic Value
Total Endpoints 5
Data Models 2
Tech Stack 4 technologies
Setup Time ~5 minutes

⭐ Show Your Support

If this project helped you, please give it a ⭐️ on GitHub!
