from flask import render_template, request, redirect, url_for
from app.decorators import authorized
from app.dependencies.services import get_services
from . import main
from .forms import FilterForm, ChannelFilterForm

@main.route("/articles", methods=["GET", "POST"])
@authorized
def articles():
    services = get_services()
    filter_form = FilterForm()
    hours = 1

    if filter_form.validate_on_submit():
        try:
            hours = int(filter_form.hours.data)
        except Exception:
            hours = 1
        if not hours or int(hours) < 1:
            filter_form.hours.errors.append("Hours must be set to 1 or greater.")
            articles = services.articles.read_articles()

        else:
            articles = services.articles.read_articles(hours=int(hours))
    else:
        articles = services.articles.read_articles(hours=hours)

    articles.sort(key=lambda x: x.likes, reverse=True)
    return render_template("main/articles.html", articles=articles, filter_form=filter_form, current_hours = hours)


@main.route("/article/<uuid>", methods = ["GET", "POST"])
def article(uuid):
    services = get_services()
    return render_template("main/article.html", article=services.articles.read_article(uuid))


@main.route("/like_article/<uuid>", methods=["POST"])
@authorized
def like_article(uuid):
    services = get_services()
    liked = services.articles.like_article(uuid)
    return {"liked": liked}

@main.route("/channels", methods=["GET", "POST"])
@authorized
def channels():
    services = get_services()
    all_channels = services.channels.get_all_channels()
    form = ChannelFilterForm()

    if form.validate_on_submit():
        disabled_uuids = request.form.getlist("disabled")
        disabled_channels = [channel for channel in all_channels if channel.uuid in disabled_uuids]
        services.channels.set_disabled_channels(disabled_channels)

        return redirect(url_for('main.channels'))

    return render_template("main/channels.html", channels=all_channels, form=form)