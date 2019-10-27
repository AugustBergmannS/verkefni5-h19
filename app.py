from flask import Flask, render_template, session, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Leyno'

vorur=[
	[0,"Pylsupasta",10000,"pylsupasta.jpg"],
	[1,"Sítrónurjómapasta",2000,"sitronurjomapasta.jpg"],
	[2,"Ravioli",1600,"ravioli.jpg"],
	[3,"Spagetti Með Hvítlauki",3400,"spagetti_med_hvitlauki.jpg"],
	[4,"Mexíkósk Ramen",100,"mexikosk_ramen.jpg"],
	[5,"Grúm Taco Pasta",4000,"grum_taco_pasta.jpg"]
]


@app.route('/')
def index():
	karfa = 0
	if 'karfa' in session:
		karfa = len(session['karfa'])
		til = True
	else:
		til = False
	return render_template("index.tpl", vorur=vorur, k=karfa, til=til)


@app.route('/ikorfu/<int:id>')
def ikorfu(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.append(id)
		session['karfa'] = karfa
	else:
		karfa.append(id)
		session['karfa'] = karfa
	print(len(karfa))
	return render_template("ikorfu.tpl", vorur=vorur)


@app.route('/karfa')
def karfa():
	karfa = []
	k=0
	heild=0
	if 'karfa' in session:
		karfa = session['karfa']
		k = len(session['karfa'])
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("karfa.tpl", vorur=vorur, karfa=karfa, k=k, heild=heild)


@app.route('/eyda/<int:id>')
def eyda(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.remove(id)
		session['karfa'] = karfa
	return render_template("eyda.tpl", vorur=vorur)

@app.route('/taema')
def taema():
	session.pop('karfa',None)
	return render_template("taema.tpl", vorur=vorur)

@app.route('/karfa/kaupa')
def kaupa():
	karfa = []
	heild = 0
	if 'karfa' in session:
		karfa = session['karfa']
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("kaupa.tpl", vorur=vorur, karfa=karfa, heild=heild)

@app.route('/karfa/kaupa/takk', methods=['GET','POST'])
def takk():
	if request.method == 'POST':
		nafn = request.form['name']
		netfang = request.form['email']
	karfa = []
	session['karfa'] = karfa
	return render_template("takk.tpl", vorur=vorur, nafn=nafn, netfang=netfang)

@app.errorhandler(404)
def error404(error):
	return render_template("404.tpl"),404

if __name__ == "__main__":
	app.run(debug=True)