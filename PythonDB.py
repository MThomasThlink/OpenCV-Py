import configparser
import pyodbc

import Global
from Global import gdbserver, gdbname, gdbuser, gdbpassword

connection: pyodbc.Connection = None
cursor: pyodbc.Cursor = None

def loadprops():
    print('loadprops')
    configfile = "./OpenCV-Demo.properties"
    config = configparser.ConfigParser()

    try:
        f = open(configfile)
    except FileNotFoundError:
        print('Criar arquivos com dados padrão.')
        config['SQLDB'] = {'dbserver': 'localhost',
                           'dbname': 'PythonDB',
                           'dbuser': 'sa',
                           'dbpassword': 'sbdpu2001'}
        with open(configfile, 'w') as wfile:
            config.write(wfile)
        print('Arquivo carregado')
        f = open(configfile)
    finally:
        f.close

    config.read(configfile)

    Global.gdbserver = config.get('SQLDB', 'dbserver')
    Global.gdbname = config.get('SQLDB', 'dbname')
    Global.gdbuser = config.get('SQLDB', 'dbuser')
    Global.gdbpassword = config.get('SQLDB', 'dbpassword')

def dbopen():
    print('dbopen')
    global connection
    loadprops()
    strCnx = 'DRIVER={SQL Server};SERVER=' + Global.gdbserver + ';DATABASE=' + Global.gdbname + \
             ';UID=' + Global.gdbuser + ';PWD=' + Global.gdbpassword
    print(strCnx)
    global cursor
    # ODBC Driver 17 for
    try:
        connection = pyodbc.connect(strCnx)
    except pyodbc.Error as err:
        print('Erro conexao: ', err)
        return

    cursor = connection.cursor()

def dbclose():
    connection.close()




def dbins(lname, lfoto, lenc):
    tsql = "INSERT INTO tbOCV (nome, foto, [enc000], [enc001], [enc002], [enc003], [enc004], [enc005], [enc006], " \
           "[enc007], [enc008], [enc009], [enc010], [enc011], [enc012], [enc013], [enc014], [enc015], [enc016], " \
           "[enc017], [enc018], [enc019], [enc020], [enc021], [enc022], [enc023], [enc024], [enc025], [enc026], " \
           "[enc027], [enc028], [enc029], [enc030], [enc031], [enc032], [enc033], [enc034], [enc035], [enc036], " \
           "[enc037], [enc038], [enc039], [enc040], [enc041], [enc042], [enc043], [enc044], [enc045], [enc046], " \
           "[enc047], [enc048], [enc049], [enc050], [enc051], [enc052], [enc053], [enc054], [enc055], [enc056], " \
           "[enc057], [enc058], [enc059], [enc060], [enc061], [enc062], [enc063], [enc064], [enc065], [enc066], " \
           "[enc067], [enc068], [enc069], [enc070], [enc071], [enc072], [enc073], [enc074], [enc075], [enc076], " \
           "[enc077], [enc078], [enc079], [enc080], [enc081], [enc082], [enc083], [enc084], [enc085], [enc086], " \
           "[enc087], [enc088], [enc089], [enc090], [enc091], [enc092], [enc093], [enc094], [enc095], [enc096], " \
           "[enc097], [enc098], [enc099], [enc100], [enc101], [enc102], [enc103], [enc104], [enc105], [enc106], " \
           "[enc107], [enc108], [enc109], [enc110], [enc111], [enc112], [enc113], [enc114], [enc115], [enc116], " \
           "[enc117], [enc118], [enc119], [enc120], [enc121], [enc122], [enc123], [enc124], [enc125], [enc126], " \
           "[enc127]) " \
           "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?," \
           "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?," \
           "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); "
    cursor.execute(tsql, lname, lfoto,
                        lenc[0], lenc[1], lenc[2], lenc[3], lenc[4], lenc[5], lenc[6], lenc[7], lenc[8], lenc[9],
                        lenc[10], lenc[11], lenc[12], lenc[13], lenc[14], lenc[15], lenc[16], lenc[17], lenc[18],
                        lenc[19],
                        lenc[20], lenc[21], lenc[22], lenc[23], lenc[24], lenc[25], lenc[26], lenc[27], lenc[28],
                        lenc[29],
                        lenc[30], lenc[31], lenc[32], lenc[33], lenc[34], lenc[35], lenc[36], lenc[37], lenc[38],
                        lenc[39],
                        lenc[40], lenc[41], lenc[42], lenc[43], lenc[44], lenc[45], lenc[46], lenc[47], lenc[48],
                        lenc[49],
                        lenc[50], lenc[51], lenc[52], lenc[53], lenc[54], lenc[55], lenc[56], lenc[57], lenc[58],
                        lenc[59],
                        lenc[60], lenc[61], lenc[62], lenc[63], lenc[64], lenc[65], lenc[66], lenc[67], lenc[68],
                        lenc[69],
                        lenc[70], lenc[71], lenc[72], lenc[73], lenc[74], lenc[75], lenc[76], lenc[77], lenc[78],
                        lenc[79],
                        lenc[80], lenc[81], lenc[82], lenc[83], lenc[84], lenc[85], lenc[86], lenc[87], lenc[88],
                        lenc[89],
                        lenc[90], lenc[91], lenc[92], lenc[93], lenc[94], lenc[95], lenc[96], lenc[97], lenc[98],
                        lenc[99],
                        lenc[100], lenc[101], lenc[102], lenc[103], lenc[104], lenc[105], lenc[106], lenc[107],
                        lenc[108], lenc[109],
                        lenc[110], lenc[111], lenc[112], lenc[113], lenc[114], lenc[115], lenc[116], lenc[117],
                        lenc[118], lenc[119],
                        lenc[120], lenc[121], lenc[122], lenc[123], lenc[124], lenc[125], lenc[126], lenc[127])


def dbclose():
    connection.close()


def dbstring(i, p):
    return 'SQUARE(' + str(p) + '-enc' + "{:03d}".format(i) + ')+'


def dbfullstring(n, enc):
    text = ''
    for i in range(n):
        text = text + dbstring(i, enc[i])
    # print('dbfullstring: ', text)
    return text[0:len(text) - 1]


def dbsearch(enc, maxregs, tol):
    if len(enc) == 0 | len(enc) < 128:
        print('Enconding inválido')
        return

    sqlfield = 'SQRT(' + dbfullstring(128, enc) + ')'
    # print(sqlfield)
    sqlfull = 'select	TOP ' + str(maxregs) + ' id, nome,  ' + \
              sqlfield + \
              'from	tbOCV ' + \
              'WHERE ' + sqlfield + ' < ' + str(tol) + ' ' \
                                                       'ORDER BY ' + sqlfield
    # print(sqlfull)

    global cursor
    cursor = connection.cursor()
    cursor.execute(sqlfull)
    row = cursor.fetchone()
    # while row:
    #     print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
    #     row = cursor.fetchone()
    return row
