from bottle import route, run, static_file, template, TEMPLATE_PATH

# add the templates folder
TEMPLATE_PATH.append("./view/templates")

# Serve media files from the 'media' directory
@route('/media/<filepath:path>')
def serve_media(filepath):
    return static_file(filepath, root='./media')


@route('/')
def hello():
    return template("home")

if (__name__ == "__main__"):
    run(
        host='192.168.4.51', # 192.168.4.51 or localhost
        port=8080,
        debug=True
    )
