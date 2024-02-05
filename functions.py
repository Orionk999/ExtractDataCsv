from datetime import datetime

def tryToConvertData(cadena):
    try:
        fecha = datetime.strptime(cadena, '%Y-%m-%d %H:%M:%S')
        return fecha
    except ValueError:
        return False