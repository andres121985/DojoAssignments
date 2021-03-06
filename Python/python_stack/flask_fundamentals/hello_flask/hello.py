from flask import Flask, render_template # Import Flask to allow us to create our app and import
                                          # render_template to allow us to render index.html.
# Global variable __name__ tells Flask whether or not we are running the file
app = Flask(__name__)
# directly, or importing it as a module.


# The "@" symbol designates a "decorator" which attaches the following
@app.route('/')
# function to the '/' route. This means that whenever we send a request to
# localhost:5000/ we will run the following "hello_world" function.
def hello_world():
    # return 'Hello World!'  # Return the string 'Hello World!' as a response.
    return render_template('index.html')  # Render the template and return it!
@app.route('/success')
def success():
  return render_template('success.html')
app.run(debug=True)      # Run the app in debug mode.
