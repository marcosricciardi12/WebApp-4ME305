import os
from main import create_app,request, jsonify
app = create_app()
app.app_context().push()
from main import db
	
if __name__ == '__main__':
	db.create_all()
	app.run(host="0.0.0.0", port = os.getenv("PORT"), debug = True)
#Cambios
