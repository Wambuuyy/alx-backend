# i18n Flask Application

This project demonstrates the implementation of internationalization (i18n) in a Flask application. It includes features such as locale selection based on user preference or URL parameters, localization of timestamps, and mock user login to simulate user-specific settings.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tasks](#tasks)
  - [0. Basic Flask App](#0-basic-flask-app)
  - [1. Basic Babel Setup](#1-basic-babel-setup)
  - [2. Get Locale from Request](#2-get-locale-from-request)
  - [3. Parametrize Templates](#3-parametrize-templates)
  - [4. Force Locale with URL Parameter](#4-force-locale-with-url-parameter)
  - [5. Mock Logging In](#5-mock-logging-in)
  - [6. Use User Locale](#6-use-user-locale)
  - [7. Infer Appropriate Time Zone](#7-infer-appropriate-time-zone)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alx-backend.git
   cd alx-backend/0x02-i18n
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python3 0-app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/` to view the app.

3. To test different locales, use the URL parameter `locale`. For example:
   - `http://127.0.0.1:5000/?locale=en`
   - `http://127.0.0.1:5000/?locale=fr`

4. To test the mock login system, use the URL parameter `login_as` with a user ID. For example:
   - `http://127.0.0.1:5000/?login_as=1`

## Project Structure

```
0x02-i18n/
│
├── templates/
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 2-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   └── 6-index.html
│
├── translations/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── messages.mo
│   │       └── messages.po
│   └── fr/
│       └── LC_MESSAGES/
│           ├── messages.mo
│           └── messages.po
│
├── babel.cfg
├── 0-app.py
├── 1-app.py
├── 2-app.py
├── 3-app.py
├── 4-app.py
├── 5-app.py
└── 6-app.py
```

## Tasks

### 0. Basic Flask App

Set up a basic Flask app with a single route and a template that displays "Welcome to Holberton" as the page title and "Hello world" as the header.

### 1. Basic Babel Setup

Install Flask-Babel, create a `Config` class for available languages, and set up Babel in the Flask app.

### 2. Get Locale from Request

Create a `get_locale` function that uses `request.accept_languages` to determine the best match with supported languages.

### 3. Parametrize Templates

Use the `_` or `gettext` function to parametrize templates and set up translation dictionaries.

### 4. Force Locale with URL Parameter

Implement a way to force a particular locale by passing the `locale` parameter in the URL.

### 5. Mock Logging In

Mock a user login system using a predefined user table and the `login_as` URL parameter.

### 6. Use User Locale

Modify `get_locale` to use a user's preferred locale if it is supported.

### 7. Infer Appropriate Time Zone

Define a `get_timezone` function to infer the correct time zone from URL parameters, user settings, or default to UTC.

## Resources

- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n tutorial](https://flask.palletsprojects.com/en/1.1.x/patterns/i18n/)
- [pytz](https://pythonhosted.org/pytz/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

