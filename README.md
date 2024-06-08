# YUM2YOU - Train Food Ordering Website

## Description
YUM2YOU allows train travelers in India to order food from trusted vendors along their route.

## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/YUM2YOU.git
    cd YUM2YOU
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Initialize the database and add sample data:
    ```
    python create_db.py
    ```

5. Run the application:
    ```
    flask run
    ```

## Deployment

To deploy on Heroku, follow these steps:

1. Login to Heroku and create a new app:
    ```
    heroku login
    heroku create your-app-name
    ```

2. Push the code to Heroku:
    ```
    git push heroku main
    ```

3. Set the environment variables on Heroku:
    ```
    heroku config:set SECRET_KEY=your_secret_key
    heroku config:set DATABASE_URL=your_database_url
    ```

4. Open the application:
    ```
    heroku open
    ```

## License

This project is licensed under the MIT License.
