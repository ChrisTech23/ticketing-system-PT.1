# Import necessary modules from Flask
from flask import Flask, render_template, request, redirect, url_for, flash

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for using session and flash messages (replace 'your_secret_key' with your own secret key)
app.secret_key = 'your_secret_key'

# Define a route for the index page to handle both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the request method is POST (form submission)
        
        # Retrieve form data (title and description) from the request
        title = request.form['title']
        description = request.form['description']
        
        # Process form data here (e.g., save to a database)
        
        # Flash success message
        flash('Ticket submitted successfully!', 'success')
        
        # Redirect to the index page after form submission
        return redirect(url_for('index'))
    
    # Render the HTML template for the index page
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
