
from flask import Flask, render_template, request, redirect

from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)


@app.route('/')
def slash():
    return redirect('/sign-up')


@app.route('/Home', methods=['GET', 'POST'])
def home():
    return render_template('Home.html')


@app.route('/Login', methods=['GET', 'POST'])
def login():

    print('REQUEST METHOD:', request.method)

    if request.method == 'POST':
        print('POST RECEIVED')

        username = request.form.get('username')
        password = request.form.get('password')

        print(username)

        hashed_password = generate_password_hash(password)

        # Password checking will go here later
        # Example:
        if check_password_hash(hashed_password, password):
            print('Login successful')

    return render_template('Login.html')


@app.route('/sign-up', methods=['GET', 'POST'])
def signup():

    print('REQUEST METHOD:', request.method)

    if request.method == 'POST':
        print('POST RECEIVED')

        fname = request.form.get('fname', '')
        lname = request.form.get('lname', '')
        username = request.form.get('username', '')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        
        if fname.strip() == '' or lname.strip() == '':
            print('One of the name fields has been left blank')
            return render_template(
                'sign-up.html',
                error='Please enter your first or last name'
            )
        
        
        
        if username.strip() == '':
            print('Please enter a username')
            return render_template(
                'sign-up.html',
                error='Please enter a username'
            )

       

        if password.strip() == "" or confirm_password.strip() == "":
            print('You left one of the password fields blank')
            return render_template(
                'sign-up.html',
                error='You left one of the password fields blank'
            )


        elif password == confirm_password:
            print('Password matches')
        
            hashed_password = generate_password_hash(password)
        
            print(fname)
            print(lname)
            print(username)
            print(hashed_password)

            #  username and hashed password
            # database here.

        else:
            print('Password does not match')

            return render_template(
                'sign-up.html',
                error='Passwords do not match'
            )

    return render_template('sign-up.html')


if __name__ == '__main__':
    app.run(debug=True)
