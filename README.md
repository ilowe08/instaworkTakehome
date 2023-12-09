# Team Management Project

This project is a simple team member management application built with Django. It allows users to view, edit, add, and delete team members.

## Features

- List all team members with details.
- Add a new team member.
- Edit existing team member information.
- Delete team members.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ilowe08/instaworkTakehome.git
    ```

2. Navigate to the project directory:

    ```bash
    cd instaworkTakehome
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Open the project in your web browser at http://localhost:8000/application.

## Usage

- Access the Team Members page to view, edit, add, and delete team members.
- Click on a team member's name to edit their details.
- Click the "+" button to add a new team member.


