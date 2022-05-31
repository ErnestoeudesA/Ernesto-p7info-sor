import cgitb
import cgi
import math
import index

cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

    raio1 = float(form.getvalue('raio'))
    area_circ = math.pi * math.pow(raio_, 2)

    index.print_header(title)
    print("<h1>Círculo</h1>")
    print("<p>Raio: {:.1f}</p>".format(raio1))
    print("<p>Área do círculo: {:.1f}</p>".format(area_circ))
    print("<a href=\'../circulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()

    raio2 = float(form.getvalue('raio'))
    per_circ = 2 * math.pi * raio

    index.print_header(title)
    print("<h1>Círculo</h1>")
    print("<p>Raio: {:.1f}".format(raio2))
    print("<p>Perímetro do círculo: {:.1f}".format(per_circ))
    print("<a href=\'../circulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()
