import json
import unicodedata

def corregir_caracteres(texto):
    # Primero, convertimos el texto a la forma NFC para normalizar caracteres combinados.
    texto_normalizado = unicodedata.normalize('NFC', texto)
    
    reemplazos = {
        "Ã¡": "á", "Ã©": "é", "Ã­": "í", "Ã³": "ó", "Ãº": "ú",
        "Ã": "Á", "Ã‰": "É", "Ã": "Í", "Ã“": "Ó", "Ãš": "Ú",
        "Ã±": "ñ", "Ã‘": "Ñ", "Ã¼": "ü", "Ãœ": "Ü",
        "Â": "", "â€“": "–", "â€™": "’", "â€": "", 
        "â€œ": "“", "â€": "”", "â€¢": "•",
        "Ã§": "ç", "Ã": "í", "Ã¥": "å", "Ã¯": "ï", "Ã©": "é",
        "Å": "ō", "Å": "œ", "Å¸": "Ÿ"
    }
    
    for incorrecto, correcto in reemplazos.items():
        texto_normalizado = texto_normalizado.replace(incorrecto, correcto)
    
    return texto_normalizado

def corregir_json(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for entry in data:
        if 'countryName' in entry:
            entry['countryName'] = corregir_caracteres(entry['countryName'])
    
    with open(archivo_salida, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    archivo_entrada = "biometric_country_en.json"  # Cambia esto por la ruta de tu archivo de entrada
    archivo_salida = "biometric_country_en_corregido.json"  # Cambia esto por la ruta de tu archivo de salida
    corregir_json(archivo_entrada, archivo_salida)
    print(f"Archivo corregido guardado como {archivo_salida}")
