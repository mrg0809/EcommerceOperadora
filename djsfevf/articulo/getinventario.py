import firebirdsql
from .models import VarianteArticulo

"""Datos para conexion a base de datos remota"""
conn = firebirdsql.connect(
    host='sfan.ddns.net',
    database='C:\Microsip datos\SPORTS FAN 2016.FDB',
    port=2000,
    user='SYSDBA',
    password='flexracer',
    charset='WIN1251'
)
cur = conn.cursor()



def get_inventario(upc):
    existencia = 0
    paridarticulo = ['', 'N', 'N', upc]
    cur.execute("select * from BUSCA_ARTICULOS_NO_DUP(?, ?, ?, ?)", (paridarticulo))
    resultadoid = cur.fetchone()
    microsipid = resultadoid[0]
    parexistencia = [microsipid, 0, '31.12.2021', '']
    cur.execute("select * from EXIVAL_ART(?, ?, ?, ?)", (parexistencia))
    resultadoexistencia = cur.fetchone()
    existencia = int(resultadoexistencia[1])
    print(existencia)         
    return existencia


def actualiza_inventario(upc):
    obj = VarianteArticulo.objects.get(upc=upc)
    print(obj)


actualiza_inventario(464646456)