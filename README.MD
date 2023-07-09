### DISCLAIMER: This README.md file has sections that were written and reviewed by ChatGPT

# FlaskAPI Project

This is a FlaskAPI project designed to help you regain knowledge of Flask and explore the integration of SQLite with Flask. The application will serve as an API that can be used by a frontend application in the future.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shearertzach/FlaskAPI
   ```

2. Navigate to the project directory:

   ```bash
   cd FlaskAPI
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that you are in the project directory and that the virtual environment is activated.

2. Start the Flask development server:

   ```bash
    gunicorn -c gunicorn.conf.py main:app
   ```

3. The FlaskAPI should now be running locally on your machine. You can access it through the following URL:

   ```
   http://localhost:8000
   ```

## Endpoints

The FlaskAPI exposes the following endpoints:

- `POST /`: Adds 10 users to the users table with random usernames

## Database (IN-PROGRESS ----- IGNORE SECTION)

This project utilizes SQLite as the backend database. The database file is named `SCHEMAS_database.db` and is located in the project directory.

Before running the application, be sure to rename `SCHEMAS_database.db` -> `database.db`

This will ensure that the application code has the required schemas and tables to run.



## Contributing

Contributions to this FlaskAPI project are welcome. If you find any issues or have any suggestions for improvements, please feel free to submit a pull request or open an issue in the repository.

## License

This project is licensed under the [MIT License](LICENSE).