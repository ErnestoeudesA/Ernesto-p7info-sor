import cgitb, cgi
import index


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

    base = float(form.getvalue('base'))
    altura = float(form.getvalue('altura'))
    area_tri = (base * altura) / 2

    index.print_header(title)
    print("<h1>Triângulo</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Área do Triângulo: {:.1f} </p>".format(area_tri))
    print("<a href=\'../triangulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()

    base = float(form.getvalue('base'))
    lado1 = float(form.getvalue('lado1'))
    lado2 = float(form.getvalue('lado2'))

    per_tri = base + lado1 + lado2

    index.print_header(title)
    print("<h1>Triângulo</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Lado: {:.1f}".format(lado1))
    print("<p>Lado: {:.1f}".format(lado2))
    print("<p>Perímetro do Triângulo: {:.1f} </p>".format(per_tri))
    print("<a href=\'../triangulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()


