from flask import render_template
from app.models.errors import RedirectError
from flask import flash, redirect, url_for

def register_error_handlers(app):
    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        if isinstance(error, RedirectError):
            flash(str(error), "danger")
            return redirect(url_for(error.redirect_url))

        return render_template("error.html", message=str(error))