# DorukLED Website - Reorganized Flask Application

This document provides an overview of the reorganized Flask application structure for the DorukLED website, configured for both test and server environments.

## Project Overview

The original website code was reorganized into a standard Flask project structure to improve maintainability and scalability. The core requirements, including using Flask, integrating directly with MySQL using `Flask-MySQLdb`, and enforcing HTTPS with `Flask-Talisman`, have been implemented.

Key changes:

*   **Standard Flask Structure:** The code is organized into standard directories like `src`, `static`, `templates`, `models`, and `routes`.
*   **Frontend Assets:** Your original HTML, CSS, JavaScript, images, and video files have been preserved and moved to the appropriate `src/templates` and `src/static` directories.
*   **Backend Logic:** The Flask application setup, routing, and configuration have been implemented in `src/main.py` and `src/routes/main_routes.py`.
*   **Database Integration:** The application uses `Flask-MySQLdb` for direct MySQL database interaction. Configuration is handled via `config.py` and environment variables.
*   **HTTPS Enforcement:** `Flask-Talisman` is integrated in `src/main.py` to enforce HTTPS connections.
*   **Environment Configuration:** The setup supports different configurations for test/development and server/production environments primarily through environment variables.
*   **Dependencies:** All required Python packages are listed in `requirements.txt` and managed within a virtual environment (`venv`).

## Folder Structure

```
dorukled_reorganized/
├── venv/                     # Python virtual environment
├── src/
│   ├── models/
│   │   └── db.py             # Database initialization (Flask-MySQLdb)
│   ├── routes/
│   │   └── main_routes.py    # Application routes (Blueprints)
│   ├── static/               # Static files (CSS, JS, images, video)
│   │   ├── css/
│   │   ├── fonts/
│   │   ├── img/
│   │   ├── js/
│   │   ├── sass/
│   │   └── video/
│   ├── templates/            # HTML templates
│   └── main.py             # Main Flask application factory and entry point
├── config.py               # Main configuration file (provides defaults, reads env vars)
├── config.example.py       # Example configuration file
├── requirements.txt        # Python dependencies
└── README.md               # This documentation file
```

## Configuration for Test and Server Environments

The application uses a combination of `config.py` and environment variables to manage settings for different environments.

1.  **`config.py`:**
    *   This file defines configuration variables (like `SECRET_KEY`, `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DB`).
    *   It reads values from environment variables if they exist, otherwise, it uses default values suitable for local testing/development.
    *   **For local testing:** You can modify the defaults in `config.py` directly or set environment variables locally.
    *   **For server deployment:** You should **not** commit sensitive information like production database passwords directly into `config.py`. Instead, rely on setting environment variables on the server.

2.  **Environment Variables (Recommended for Server):**
    *   Set the following environment variables on your server to override the defaults in `config.py`:
        *   `SECRET_KEY`: A strong, unique secret key for production.
        *   `MYSQL_HOST`: Your production database host (e.g., AWS RDS endpoint).
        *   `MYSQL_USER`: Your production database username.
        *   `MYSQL_PASSWORD`: Your production database password.
        *   `MYSQL_DB`: Your production database name.
        *   `FLASK_DEBUG`: Set to `0` or `False` in production.
        *   `PORT`: The port your application should listen on (if different from 5000).

3.  **Database (`src/models/db.py`):** Initializes the `Flask-MySQLdb` connection using the configuration loaded by Flask.

4.  **HTTPS (`src/main.py`):** `Flask-Talisman` is initialized to enforce HTTPS. In a typical production setup, SSL termination might be handled by a reverse proxy (like Nginx), but Talisman provides an additional layer of security headers and HTTPS enforcement within the app.

## Running the Application

1.  **Clone the Repository:** Obtain the code (e.g., via GitHub clone).
2.  **Navigate to Project Directory:**
    ```bash
    cd dorukled_reorganized
    ```
3.  **Activate Virtual Environment:**
    ```bash
    source venv/bin/activate
    ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Configure for Environment:**
    *   **Local Test:** Modify `config.py` if needed, or set local environment variables.
    *   **Server:** Set the environment variables listed above on your server.
6.  **Run the Development Server (for Testing):**
    ```bash
    # Ensure FLASK_DEBUG is not set or is set to True/1 for development
    export FLASK_DEBUG=1 
    python src/main.py
    ```
    The application will be accessible at `http://localhost:5000` (or the specified port). Talisman will attempt to redirect HTTP to HTTPS.

7.  **Run in Production (Example with Gunicorn):**
    ```bash
    # Ensure FLASK_DEBUG is set to 0 or False for production
    export FLASK_DEBUG=0
    # Set other production environment variables (SECRET_KEY, MYSQL_*, etc.)
    gunicorn --bind 0.0.0.0:5000 src.main:app
    ```
    For production, run using a WSGI server like Gunicorn. It's recommended to run Gunicorn behind a reverse proxy (like Nginx or Apache) that handles incoming requests and SSL termination.

## Notes

*   The frontend code (HTML/CSS) remains unchanged, only its location within the project structure has been updated.
*   Ensure your MySQL server is running and accessible with the credentials provided via `config.py` or environment variables for the respective environment.

