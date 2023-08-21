# Inkpot Bookstore

Welcome to Inkpot Bookstore, a Django application for managing and browsing books online.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- [Python](https://www.python.org/downloads/) installed
- [Docker](https://www.docker.com/products/docker-desktop) installed (optional)

## Getting Started

These instructions will guide you through setting up and running the Inkpot Bookstore project on your local machine.

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/jadie404/compTask.git
    cd Inkpot_Bookstore
    ```

2. **Create and Activate a Virtual Environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Database Setup:**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Open a web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Running with Docker

If you prefer, you can also run the application using Docker:

1. **Build the Docker Image:**

    ```bash
    docker build -t bookstore .
    ```

2. **Run the Docker Container:**

    ```bash
    docker run -p 8000:8000 bookstore
    ```

3. **Access the Application:**

    Open a web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Contributing

Feel free to contribute to this project by [forking the repository](https://github.com/jadie404/compTask.git/fork) and submitting a pull request.

## Notes

- Remember to set environment variables or configuration files for sensitive information like database credentials.
- Exclude sensitive files (venv, .env, etc.) using the provided .gitignore file.
- Feel free to customize this README.md to match your project's specific setup and requirements.
