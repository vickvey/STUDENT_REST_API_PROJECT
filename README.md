# STUDENT_REST_API_PROJECT

This project includes a backend API built with Django and a frontend application built with React. The backend provides a RESTful API for managing student records, while the frontend offers a user interface for interacting with this API.

## Project Structure

```bash
STUDENT_REST_API_PROJECT/
├── LICENSE
├── mysite/
│ ├── api/
│ ├── db.sqlite3
│ ├── frontend/
│ ├── manage.py
│ ├── mysite/
│ ├── REPORT.md
│ ├── requirements.txt
│ └── TODO.txt
└── README.md
```


## Getting Started

### Prerequisites

1. **Python** (for the backend)
   - Make sure Python 3.x is installed.
   
2. **Node.js** (for the frontend)
   - Make sure Node.js and npm are installed. You can download them from [nodejs.org](https://nodejs.org/).

### Setup Instructions

- Clone this github repository:

   ```bash   
   git clone https://github.com/vickvey/STUDENT_REST_API_PROJECT/   

#### Backend Setup

1. **Navigate to the Backend Directory:**

   ```bash
   cd mysite

2. **Create and Activate a Virtual Environment:**

    ```bash
    python3 -m venv .venv # On Windows use python3.exe -m venv .venv
    source .venv/bin/activate  # On Windows Command Prompt: use `.venv\Scripts\activate.bat`

3. **Install Backend Dependencies:**

    ```bash
    pip install -r requirements.txt

4. **Run Database Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Start the Django Development Server:**

    ```bash
    python manage.py runserver

#### Frontend Setup
Open another terminal or command-prompt window and proceed with these instructions.

1. **Navigate to the Frontend Directory:**

    ```bash
    cd mysite/frontend

2. **Install Frontend Dependencies:**

    ```bash
    npm install

3. **Start the React Development Server:**

    ```bash
    npm start

The frontend application will be running at `http://localhost:3000`.

## Testing

### Backend Tests
To run the backend tests, ensure your virtual environment is activated and then use:

```bash
python manage.py test
```

### Frontend Tests

To run the frontend tests, navigate to the frontend directory and use:

```bash
npm test (yet to be added!)
```

## API Endpoints

- GET /api/students/ - List all students.
- POST /api/students/ - Create a new student.
- GET /api/students/{roll_number}/ - Retrieve a specific student by roll number.
- PATCH /api/students/{roll_number}/ - Update a specific student by roll number.
- DELETE /api/students/{roll_number}/ - Delete a specific student by roll number.

## Project Details
- Backend: Django REST framework for API management.
- Frontend: React for user interface.
- Database: SQLite (for development purposes).

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.









