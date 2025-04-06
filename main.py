from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)


app.secret_key = 'gdiahuodeısaıfhlkchlıhvıh' 


puan = 0

@app.route('/')
def index():
    session.clear()
    return render_template('index.html',puan=0)

@app.route('/gas')
def gas():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('gas.html',puan=session['puan'])

@app.route('/plane')
def plane():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('plane.html',puan=session['puan'])

@app.route('/person')
def people():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('person.html',puan=session['puan'])

@app.route('/food')
def food():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('food.html',puan=session['puan'])

@app.route('/cloth')
def cloth():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('cloth.html',puan=session['puan'])


@app.route('/product')
def product():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('product.html',puan=session['puan'])


@app.route('/recycle')
def recycle():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('recycle.html',puan=session['puan'])


@app.route('/garbage')
def garbage():
    puan = int(request.args.get('puan', 0))
    if 'puan' in session:
        session['puan'] += puan
    else:
        session['puan'] = puan 
    print(f"Şu anki puan: {session['puan']}") 
    return render_template('garbage.html',puan=session['puan'])

@app.route('/end')
def end():
    return render_template('end.html',puan=session['puan'])



if __name__ == '__main__':
    app.run(debug=True)
