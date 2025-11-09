from flask import Flask, render_template

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'  # Output folder for static files
app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', '.gitignore', 'venv*']  # Ignore these
app.config['FREEZER_RELATIVE_URLS'] = True  # For clean URLs

@app.route('/')
def home():
    # Simple marketing logic: e.g., generate dynamic content at build time
    marketing_message = "Unlock 20% off your first purchase!"
    return render_template('home.html', message=marketing_message)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)