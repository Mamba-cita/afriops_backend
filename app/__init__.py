from flask import Flask


app = Flask(__name__)



from views.guest import views
from views.admin import views













