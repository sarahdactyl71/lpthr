from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from flask import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    #this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route('/game', methods=['POST', 'GET'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            #why is this here? Do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')

        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

            if not next_room:
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)

        return redirect(url_for("game"))

#CHANGE THIS
app.secret_key = 'some secret'

if __name__ == "__main__":
    app.run()
