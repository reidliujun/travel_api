# AI Travel Planner API

An intelligent travel recommendation service built with FastAPI, PostgreSQL, and DeepSeek AI. The service provides customized travel itineraries based on city, duration, and budget preferences.

## Features

- AI-powered travel itinerary generation
- Markdown-formatted detailed travel plans
- Caching system for quick responses
- Support for different travel styles (luxury, normal, budget)

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- DeepSeek AI API
- Docker (for database)

## Prerequisites

- Python 3.8+
- PostgreSQL
- Docker and Docker Compose

## Setup backend api

1. Clone the repository:
```bash
git clone <repository-url>
cd travel_api/backend_api
```
2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```

3. Install dependencies:
```bash
pip install -r requirements.txt
 ```

4. Create .env file:
```plaintext
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/travel_db
DEEPSEEK_API_KEY=your-deepseek-api-key
CACHE_EXPIRY_DAYS=7
 ```

5. Start PostgreSQL using Docker:
```bash
docker-compose up -d
 ```

6. Insert test data (optional):
```bash
python -m scripts.insert_test_data
 ```

7. Run the application:
```bash
uvicorn main:app --reload
 ```

## Setup front end app
1. Navigate to frontend directory:
```bash
cd frontend
```
2. Install dependencies:
```bash
npm install
```

3. Create .env file (if needed):

```
VITE_API_URL=http://localhost:8000
```

4. Start development server:

```bash
npm run dev
```

## API Documentation

The API documentation is available through:

1. **Swagger UI (Interactive)**
   - URL: `http://localhost:8000/docs`
   - Interactive API documentation with testing capability
   - Try out API endpoints directly from the browser

2. **ReDoc (Reference)**
   - URL: `http://localhost:8000/redoc`
   - Clean, organized API reference documentation
   - Better for reading and sharing

### Example API Call

```bash
curl "http://localhost:8000/tokyo?days=3&type=luxury"