mport os
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Get the application version from an environment variable,
# defaulting to 'v1' if the environment variable is not set.
APP_VERSION = os.environ.get('APP_VERSION', 'v2')

# Define a route for the home page ('/')
@app.route('/')
def hello_version():
    """
    This function handles requests to the root URL and returns
    a greeting message including the dynamically configured version.
    """
    return f'Hello version {APP_VERSION}'

# This block ensures the Flask development server runs only when the script
# is executed directly (not when imported as a module).
if __name__ == '__main__':
    # Run the Flask application.
    # host="0.0.0.0" makes the server accessible from any IP,
    # which is useful in containerized environments.
    # debug=True enables debug mode, providing a debugger and auto-reloading
    # on code changes.
    app.run(host="0.0.0.0", debug=True)
