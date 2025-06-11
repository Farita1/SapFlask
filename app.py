from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate
from database import db
from forms import PersonaForm
from models import Persona

#Para activar el debug mode: $env:FLASK_DEBUG = "1"
#Para crear el formulario para agregar usuario use: python -m pip install flask-wtf

app = Flask(__name__)
#Configuración de la bd
USER_DB = 'postgres'
PASS_DB = '1234'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Inicialización del objeto db de sqalchemy
#db = SQLAlchemy(app)
db.init_app(app)

#Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)

#configuración de flask-wtf
app.config['SECRET_KEY'] = 'destroymaster123'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    #Listamos a las personas
    #personas = Persona.query.all()
    personas = Persona.query.order_by('id')
    total_persona = Persona.query.count()
    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_persona}')
    return render_template('index.html', personas = personas, total_persona = total_persona)

@app.route('/ver/<int:id>')
def ver_detalle(id):
    #Recuperamos la persona según el id proporcionado
    #personas = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(object=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit:
            personaForm.populate_obj(persona)
            app.logger.debug(f'Persona a insertar: {persona}')
            #Insertamos el nuevo registro
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregar.html', forma=personaForm)

@app.route('/editar/<int:id>', methods=['POST', 'GET'])
def editar(id):
    #
    persona = Persona.query.get_or_404(id)
    personaForma = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForma.validate_on_submit():
            personaForma.populate_obj(persona)
            app.logger.debug(f'Persona a actualizar: {persona}')
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editar.html', forma=personaForma)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Persona a eliminada: {persona}')
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))
