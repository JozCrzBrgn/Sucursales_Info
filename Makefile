run:
# Corremos la app
	streamlit run streamlit_app.py

#? make cred NAMES="['Josefina', 'Bob', 'Charlie']" USRN="['alice123', 'bob456', 'charlie789']" PSS="['pass1', 'pass2', 'pass3']"
cred:
# Creamos las credenciales
	@py -c "from .env.generate_keys import crear_credenciales; crear_credenciales($(NAMES), $(USRN), $(PSS))";