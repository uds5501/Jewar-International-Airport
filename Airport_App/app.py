from flask import Flask, render_template,redirect,request,url_for
import ticket_gen

app=Flask(__name__)



@app.route("/main")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
        return render_template('signup.html')

@app.route('/ContactUs')
def showContactUs():
    return render_template('Contact.html')


if __name__=="__main__":
    app.run()
