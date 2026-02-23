from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        event = request.form['event']
        phone = request.form['phone']

        return f"""
<h2 style='color:green;'>🎉 Thank You for Registering!</h2>
<p><b>Name:</b> {name}</p>
<p><b>Email:</b> {email}</p>
<p><b>Selected Event:</b> {event}</p>
<hr>
<p>Your registration has been recorded successfully.</p>
<a href="/">Register Another User</a>
"""

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    print("CI/CD working")