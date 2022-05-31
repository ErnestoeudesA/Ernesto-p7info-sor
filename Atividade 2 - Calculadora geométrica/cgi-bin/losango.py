import cgitb, cgi
import index


cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

    diagonal_maior = float(form.getvalue('diagM'))
    diagonal_menor = float(form.getvalue('diagMe'))

    area_los = diagonal_maior * diagonal_menor

    index.print_header(title)
    print("<h1>Losango</h1>")
    print("<p>Diagonal Maior {}</p>".format(diagonal_maior))
    print("<p>Diagonal Menor: {:.1f}".format(diagonal_menor))
    print("<p>Área do Losango: {:.1f} </p>".format(area_los))
    print("<a href=\'../losango.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()

    lado = float(form.getvalue('lado-rhombus'))

    per_los = lado * 4

    index.print_header(title)
    print("<h1>Losango</h1>")
    print("<p>Lado: {}".format(lado))
    print("<p>Perímetro do Losango: {:.1f} </p>".format(per_los))
    print("<a href=\'../losango.html\'><button class='buttom'>Calcular novamente</button></a>")
    index.print_footer()