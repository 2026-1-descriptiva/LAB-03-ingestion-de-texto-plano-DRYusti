"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import re
import pandas as pd


def pregunta_01():
    rows = []

    with open("files/input/clusters_report.txt", "r") as f:
        content = f.read()

    blocks = re.split(r'\n(?=\s{0,4}\d+\s)', content)

    for block in blocks:
        lines = block.strip().split('\n')
        first = lines[0]
        m = re.match(r'^\s*(\d+)\s+(\d+)\s+([\d,]+\s*%)\s+(.*)', first)
        if not m:
            continue

        cluster = int(m.group(1))
        cantidad = int(m.group(2))
        porcentaje = float(m.group(3).replace('%', '').replace(',', '.').strip())
        keywords_part = m.group(4).strip()

        for line in lines[1:]:
            keywords_part += ' ' + line.strip()

        keywords_part = keywords_part.rstrip('.')
        keywords_part = re.sub(r'  +', ' ', keywords_part)
        keywords = [kw.strip() for kw in keywords_part.split(',') if kw.strip()]
        keywords_str = ', '.join(keywords)

        rows.append((cluster, cantidad, porcentaje, keywords_str))

    df = pd.DataFrame(rows, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ])

    return df


print(pregunta_01())

"""
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
