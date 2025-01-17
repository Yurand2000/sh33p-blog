from flask import render_template
from globals import user_management, app_config

def render_skeleton(title, content):
    return render_template(
        "skeleton.html",
        head = head(title),
        header = header(),
        footer = footer(),
        content = content
    )

def head(title, other = ""):
    return render_template("generic/head.html", title = title, other = other)

def header():
    return render_template("generic/header.html", blogicon = app_config['blog-icon'],
                           blogiconalt = app_config['blog-icon-alt'], blogname = app_config['blog-name'],
                           login = render_login_data())

def footer():
    return render_template("generic/footer.html", footertext = app_config['footer-text'],
                           blogname = app_config['blog-name'])

def render_login_data():
    if user_management.is_logged_in():
        user_data = user_management.get_user_data()

        name = ' '.join([ str.upper(x[0]) + str.lower(x[1:]) for x in user_data.name.split(' ')])
        return render_template("generic/logged_in.html", icon=user_data.picture, iconalt=f"{name}'s icon", name= name)
    else:
        return render_template("generic/do_login.html")

def render_markdown(file: str):
    import markdown
    from md_extensions import TailwindExtension

    with open(file, 'r') as f:
        page = markdown.markdown(
            f.read(),
            extensions=['extra', TailwindExtension()]
        )

    return render_template(
        "articles/markdown_skeleton.html",
        header = "",
        markdown = page
    )