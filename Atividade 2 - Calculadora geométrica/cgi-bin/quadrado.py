import cgitb, cgi
import index


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

    base = float(form.getvalue('lado1'))
    altura = float(form.getvalue('lado2'))

    area_quad = base * altura

    index.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Lado {}</p>".format(valor))
    print("<p>Área do Quadrado: {} </p>".format(area_quad))
    print("<a href=\'../quadrado.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()

    lado = float(form.getvalue('lado1'))
    per_quad = valor * 4

    index.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Lado {}</p>".format(valor))
    print("<p>Perímetro do Quadrado: {} </p>".format(per_quad))
    print("<a href=\'../quadrado.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()