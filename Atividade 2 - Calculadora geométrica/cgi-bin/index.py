def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <meta charset="UTF-8">
                    <title>{}</title>
                    <link rel="stylesheet" href="css/resultado.css">
                </head>
                <body>""".format(title))


def print_footer():
    print("</body></html>")