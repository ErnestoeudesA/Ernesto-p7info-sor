import cgitb, cgi
import index


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

    base = float(form.getvalue('lado1-rectangle'))
    altura = float(form.getvalue('lado2-rectangle'))

    area_ret = base * altura

    index.print_header(title)
    print("<h1>Retângulo</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Área do Retângulo: {:.1f} </p>".format(area_ret))
    print("<a href=\'../retangulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()

    base = float(form.getvalue('lado1-rectangle'))
    altura = float(form.getvalue('lado2-rectangle'))
    
    per_ret = (base * 2) + (altura *2)

    index.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Perímetro do Retângulo: {:.1f} </p>".format(per_ret))
    print("<a href=\'../retangulo.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()