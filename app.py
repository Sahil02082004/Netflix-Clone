from flask import Flask, render_template, request, redirect, url_for, session, flash

# Initialize the Flask app
app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'

# Dummy user data
users = {
    "testuser": "password123",  # Example user
    "karan": "password456"      # Example user
}

# Home Route
@app.route('/')
def home():
    # Show the home.html page with links to login or sign up
    return render_template("homee.html")

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Match the 'name' attributes from your HTML form
        username = request.form.get('uname')  # Match 'uname'
        password = request.form.get('psw')   # Match 'psw'

        # Validate input
        if not username or not password:
            flash("Please provide both username and password.", "error")
            return redirect(url_for('login'))

        # Authenticate user
        if username in users and users[username] == password:
            session['username'] = username
            flash("Login successful!", "success")
            return redirect(url_for('karan'))  # Redirect to karan.html page
        else:
            flash("Invalid credentials. Please try again.", "error")
            return redirect(url_for('login'))

    return render_template("login.html")

# Signin Route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Match the 'name' attributes from your HTML form
        username = request.form.get('uname')  # Match 'uname'
        password = request.form.get('psw')   # Match 'psw'

        # Validate input
        if not username or not password:
            flash("Both username and password are required.", "error")
            return redirect(url_for('signin'))

        # Check if user already exists
        if username in users:
            flash("User already exists. Please log in.", "warning")
            return redirect(url_for('login'))
        else:
            # Add the new user to the dictionary
            users[username] = password
            session['username'] = username  # Log the user in automatically
            flash("Registration successful!", "success")
            return redirect(url_for('login'))  # Redirect to karan.html page

    return render_template("signin.html")

# Karan Page Route
@app.route('/karan')
def karan():
    username = session.get('username')  # Check if the user is logged in
    if username:
        return render_template("karan.html", username=username)  # Display karan.html
    else:
        flash("Please log in first.", "error")
        return redirect(url_for('login'))  # Redirect to login if not authenticated

# Logout Route
@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

# OPTIONAL: Video Route
@app.route('/video')
def video():
    username = session.get('username')  # Check if the user is logged in
    if username:
        return render_template("video.html", username=username)
    else:
        flash("Please log in first to access videos.", "error")
        return redirect(url_for('login'))  # Redirect to login if not authenticated

if __name__ == "__main__":
    app.run(debug=True)
