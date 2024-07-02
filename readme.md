# Django Weather Greeting API

This Django project provides an API endpoint that greets the user by name and provides the current weather information based on their public IP address.

## Requirements

- Django
- Django REST Framework
- `public_ip` Python package
- `ipinfo` Python package
- `requests` Python package

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Oghenekevbe/hng1.git
    cd hng1
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. Install the required packages from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your OpenWeatherMap API key and IPinfo access token in the `settings.py` file:

    ```python
    OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'
    access_token = 'your_ipinfo_access_token'
    ```

## Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the API endpoint at:

    ```
    http://127.0.0.1:8000/api/hello?visitor_name="YourName"
    ```

    Replace `YourName` with your name. The response will include your public IP address, location, and the current temperature in your city.

## Example

**Request:**

```http
GET /api/hello?visitor_name="Mark"
```

**Response:**

```http
{
    "client_ip": "123.45.67.89",
    "location": "New York",
    "greeting": "Hello, Mark!, the temperature is 22 degrees Celsius in New York"
}

```
