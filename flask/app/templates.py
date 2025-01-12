from flask import render_template, session

def render_skeleton(title, content, app_config):
    return render_template(
        "skeleton.html",
        head = head(title),
        header = header(app_config),
        footer = footer(app_config),
        content = content
    )

def head(title, other = ""):
    return render_template("generic/head.html", title = title, other = other)

def header(app_config):
    return render_template("generic/header.html", blogicon = app_config['blog-icon'],
                           blogiconalt = app_config['blog-icon-alt'], blogname = app_config['blog-name'],
                           login = render_login_data())

def footer(app_config):
    return render_template("generic/footer.html", footertext = app_config['footer-text'],
                           blogname = app_config['blog-name'])

def render_login_data():
    if session.get('uid') is not None:
        return render_template("generic/logged_in.html", icon='/static/portraits/sheep.jpg', iconalt='alt', name='Name')
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