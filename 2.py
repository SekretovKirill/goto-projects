from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def start():
    st1 = 0
    st2 = 0
    st3= 0
    if 'st1' in  request.args:
        st1 = int(request.args['st1'])
    if 'st2' in  request.args:
        st2 = int(request.args['st2'])
    if 'st3' in  request.args:
        st3 = int(request.args['st3'])
    P = st1 + st2 + st3
    return render_template('dop.html', P = P)
app.run(debug=True, port=8080)