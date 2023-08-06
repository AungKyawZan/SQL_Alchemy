import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func

#create engine
engine = create_engine('sqlite:///hawaii.sqlite')

#create new model from old
Base = automap_base()

# reflect tables
Base.prepare(autoload_with=engine)

# Save ref
measurment = Base.classes.measurement
stations = Base.classes.station

# Flask Setup
app = Flask(__name__)


