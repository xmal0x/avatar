# Avatar Chat Application

An AI-powered personal avatar chat application that allows visitors to interact with a virtual representation of a professional Full-Stack Developer. The avatar responds as "John Doe" using AI, drawing from a comprehensive CV and personal biography to provide authentic, engaging conversations.

## 🚀 Features

- **AI-Powered Chat Interface**: Interactive chat with a virtual avatar using OpenAI's GPT models
- **Personalized Responses**: Avatar responds as a specific person with detailed background information
- **FastAPI Backend**: High-performance Python backend with async support
- **Docker Support**: Easy deployment with Docker Compose
- **CV Integration**: Avatar has access to professional CV and personal biography

## 🏗️ Architecture

### Backend (Python/FastAPI)
- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI Integration**: GPT-4o-mini for AI responses
- **PDF Processing**: Extracts text from CV documents
- **Async Support**: High-performance async/await patterns
- **CORS Enabled**: Cross-origin requests for frontend integration

### Frontend (React/TypeScript)
- **React 18**: Modern React with hooks
- **TypeScript**: Type-safe development
- **Vite**: Fast build tool and dev server
- **Zustand**: Lightweight state management
- **Responsive Design**: Mobile-friendly interface

## 📋 Prerequisites

- Docker and Docker Compose
- OpenAI API key

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd avatar
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

3. **Configure environment variables**
   Edit `.env` file with your settings:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   BACKEND_PORT=8000
   FRONTEND_PORT=5173
   VITE_API_URL=http://localhost:8000
   ```

4. **Start the application**
   ```bash
   docker-compose up --build
   ```

## 🚀 Usage

1. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

2. **Start chatting**
   - Open the frontend in your browser
   - Type your message in the chat input
   - The avatar will respond as "John Doe" based on the provided CV and biography

## 📁 Project Structure

```
avatar/
├── backend/
│   ├── app/
│   │   ├── adapters/ai/          # AI provider implementations
│   │   ├── api/routes/           # API route definitions
│   │   ├── assets/               # CV and biography files
│   │   ├── core/                 # Configuration and utilities
│   │   ├── domain/               # Data schemas and models
│   │   ├── services/             # Business logic
│   │   └── main.py              # FastAPI application entry point
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/                  # Main app component
│   │   ├── features/chat/        # Chat feature modules
│   │   │   ├── api/             # API client
│   │   │   ├── store/           # State management
│   │   │   └── ui/              # UI components
│   │   └── shared/              # Shared utilities
│   ├── Dockerfile
│   └── package.json
└── docker-compose.yml
```

## 🔧 Configuration

### Backend Configuration
- **AI Model**: Configure OpenAI model in `.env` (default: gpt-4o-mini)
- **History Limit**: Maximum conversation history (default: 200 messages)
- **CORS Origins**: Configure allowed frontend origins
- **Assets**: Paths to CV PDF and biography text files

### Frontend Configuration
- **API URL**: Backend API endpoint
- **Port**: Frontend development server port

## 🧪 API Endpoints

### Chat API
- `GET /messages` - Get conversation history
- `POST /messages` - Send a message and get AI response

### Health Check
- `GET /` - Application status and avatar name


## 📝 Customization

### Adding New Avatar Personas
1. Update `assets/CV.pdf` with new CV
2. Update `assets/summary.txt` with new biography
3. Modify `name` in backend configuration
4. Restart the application