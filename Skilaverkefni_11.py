#þurfum að setja pymysql upp í pyCharm (sama rútína og bottle-beaker)
import pymysql
from bottle import *
import os

@route('/leita')
def leit():
    return '''
        <form action="/leita" method="post">
                Skráningarnúmer bíls: <input name="leit" type="text" />
            <input value="Leit" type="submit" />

        </form>
                <form action="/breyta" method="post">
                Skráningarnúmer bíls: <input name="breyta" type="text" />
            <input value="breyta skráningu" type="submit" />

        </form>
        </form>
                <form action="/eyda" method="post">
                Skráningarnúmer bíls: <input name="eyda" type="text" />
            <input value="Eyða Skráningu" type="submit" />
        </form>
        <p><a href="http://localhost:8080/skra">Skrá nýtt ökutæki</a>
            '''

#route sem tekur við upplýsingum frá leitar forminu
@route('/leita',  method = 'post')
def skilar():
    leitad = request.forms.get('leit')
    bilanr = []
    # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword', db='1503953219_vef2verk11')
    cur = conn.cursor()
    # lesa alla úr töflunni
    cur.execute("SELECT skraningarnumer FROM bilar")
    for row in cur:
        bilanr.append(row[0])
    cur.close()
    conn.close()
    if leitad in bilanr:
        # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword',
                               db='1503953219_vef2verk11')
        cur = conn.cursor()
        # lesa alla úr töflunni
        cur.execute("SELECT * FROM bilar WHERE skraningarnumer = %s", (leitad))
        for row in cur:
            bill = row
        cur.close()
        conn.close()
        skraningarnr = bill[0]
        tegund = bill[1]
        verksmidjunr = bill[2]
        skraningardagur = bill[3]
        co2 = bill[4]
        thyngd = bill[5]
        skodun = bill[6]
        stada = bill[7]

        return template('index.tpl', skraningarnr = skraningarnr, tegund = tegund, verksmidjunr = verksmidjunr, skraningardagur = skraningardagur, skodun = skodun, co2 = co2, thyngd = thyngd, stada = stada)
    else:
        return """<p>Ekkert ökutæki fannst með þetta skráningarnúmer</P>
        <p><a href="http://localhost:8080/leita">Fara aftur á upphafsíðu </a>
        """

@route('/skra')
def skra():
    return template('nyskraning.tpl')

@route('/skra', method = 'post')
def skra():
    # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword',
                           db='1503953219_vef2verk11')
    cur = conn.cursor()
    t = request.forms.get('tegund')
    nr = request.forms.get('skraningarnr')
    v = request.forms.get('verksmidjunr')
    sd = request.forms.get('skraningardagur')
    u = int(request.forms.get('co2'))
    ti = int(request.forms.get('thyngd'))
    s = request.forms.get('skodun')
    st = request.forms.get('stada')
    cur.execute("Insert into bilar values('{}','{}','{}','{}','{:d}','{:d}','{}','{}')".format(nr, t, v, sd, u, ti, s, st))
    conn.commit()
    cur.close()
    conn.close()
    return 'Skráning tóks!<br><a href="http://localhost:8080/leita">Hætta við og fara aftur í leit</a>'

@route('/breyta',  method = 'post')
def skilar():
    leitad = request.forms.get('breyta')
    bilanr = []
    # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword', db='1503953219_vef2verk11')
    cur = conn.cursor()
    # lesa alla úr töflunni
    cur.execute("SELECT skraningarnumer FROM bilar")
    for row in cur:
        bilanr.append(row[0])
    cur.close()
    conn.close()
    if leitad in bilanr:
        # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword',
                               db='1503953219_vef2verk11')
        cur = conn.cursor()
        # lesa alla úr töflunni
        cur.execute("SELECT * FROM bilar WHERE skraningarnumer = %s", (leitad))
        for row in cur:
            bill = row
        cur.close()
        conn.close()
        skraningarnr = bill[0]
        tegund = bill[1]
        verksmidjunr = bill[2]
        skraningardagur = bill[3]
        co2 = bill[4]
        thyngd = bill[5]
        skodun = bill[6]
        return template('breyta.tpl', skraningarnr = skraningarnr, tegund = tegund, verksmidjunr = verksmidjunr, skraningardagur = skraningardagur, skodun = skodun, co2 = co2, thyngd = thyngd)
    else:
        return """<p>Ekkert ökutæki fannst með þetta skráningarnúmer</P>
        <p><a href="http://localhost:8080/leita">Fara aftur á upphafsíðu </a>
        """

@route('/breyting', method = 'post')
def skra():
    # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword',
                           db='1503953219_vef2verk11')
    cur = conn.cursor()
    t = request.forms.get('tegund')
    nr = request.forms.get('skraningarnr')
    v = request.forms.get('verksmidjunr')
    sd = request.forms.get('skraningardagur')
    u = int(request.forms.get('co2'))
    ti = int(request.forms.get('thyngd'))
    s = request.forms.get('skodun')
    st = request.forms.get('stada')
    cur.execute("Update bilar set skraningarnumer='{}', tegund='{}', verksmidjunumer='{}',skraningardagur='{}',co2='{:d}',þyngd='{:d}',skodun='{}',stada='{}' where skraningarnumer='{}'".format(nr, t, v, sd, u, ti, s, st, nr))
    conn.commit()
    cur.close()
    conn.close()
    return 'Breyting tókst!<br><a href="http://localhost:8080/leita">Hætta við og fara aftur á upphafsíðu</a>'

@route('/eyda',  method = 'post')
def skilar():
    leitad = request.forms.get('eyda')
    bilanr = []
    # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword', db='1503953219_vef2verk11')
    cur = conn.cursor()
    # lesa alla úr töflunni
    cur.execute("SELECT skraningarnumer FROM bilar")
    for row in cur:
        bilanr.append(row[0])
    cur.close()
    conn.close()
    if leitad in bilanr:
        # tengir okkur við þjón og ákveðinn grunn. cursor object veitir okkur tilvísun á ákveðinn gagnagrunn.
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='1503953219', passwd='mypassword',
                               db='1503953219_vef2verk11')
        cur = conn.cursor()
        # lesa alla úr töflunni
        leitadi = leitad
        cur.execute("delete from bilar where skraningarnumer = %s", leitadi)
        conn.commit()
        cur.close()
        conn.close()
        return 'Skráning hefur verið eydd!<br><a href="http://localhost:8080/leita">Hætta við og fara aftur á upphafsíðu</a>'
    else:
        return """<p>Ekkert ökutæki fannst með þetta skráningarnúmer</P>
        <p><a href="http://localhost:8080/leita">Fara aftur á upphafsíðu </a>
        """
run(host = '0.0.0.0', port=os.environ.get('PORT'))

