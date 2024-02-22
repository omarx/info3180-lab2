from datetime import datetime
from .views import format_date_joined
from app import app
from flask import render_template, request, url_for, flash


@app.route('/profile/')
def profile():
    now = datetime.now()
    # date_joined = datetime.date(2019, 2, 7)
    formatted_date_joined = format_date_joined(now)
    return render_template('profile.html', date_joined=formatted_date_joined)
