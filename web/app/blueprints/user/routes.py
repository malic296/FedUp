from app.decorators import authorized
from app.dependencies.services import get_services
from .forms import CredentialsForm
from app.api_client.models import UpdateCredentialsDTO, TokenResponse
from flask import redirect, url_for, render_template
from app.utils.auth import set_auth_cookie, delete_auth_cookie
from . import user
from flask import request, flash

@user.route("/profile", methods=["GET", "POST"])
@authorized
def profile():
    services = get_services()
    form = CredentialsForm()

    if form.validate_on_submit():
        req = UpdateCredentialsDTO(old_password=form.old_password.data)
        if form.new_username.data:
            req.new_username = form.new_username.data

        if form.new_password.data:
            req.new_password = form.new_password.data

        token: TokenResponse = services.consumers.update_credentials(req)

        if token:
            resp = redirect(url_for("user.profile"))
            resp = delete_auth_cookie(resp)
            resp = set_auth_cookie(resp, token.access_token)

            return resp
    else:
        if request.method == "POST":
            for field, errors in form.errors.items():
                for error in errors:
                    flash(str(error), "danger")

    user = services.consumers.get_current_user()
    return render_template("user/profile.html", user=user, form=form)

@user.route("/logout", methods=["GET", "POST"])
@authorized
def logout():
    resp = redirect(url_for("auth.index"))
    resp = delete_auth_cookie(resp)
    return resp