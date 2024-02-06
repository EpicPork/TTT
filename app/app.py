from flask import Flask

# Create an instance of the Flask class. This instance will be the WSGI application.
app = Flask(__name__)

@app.route('/')
def index():
    """
    Define the route at the root URL ('/') and its corresponding request handler.

    When a web browser requests this route, the function returns a welcome message
    for the Tic Tac Toe game.
    
    Returns:
        str: A welcome message for users visiting the root URL.
    """
    return "Welcome to Tic Tac Toe Game!"

# Check if the executed script is the main program and run the Flask application.
# 'debug=True' enables Flask's debugger, providing useful tools for development.
if __name__ == '__main__':
    app.run(debug=True)