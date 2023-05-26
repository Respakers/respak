import codecs
import json

import geopandas as gps



def shape_to_geojson(work_directory, file_name):
    # Чтение файлов из шейпа и перевод их в GeoJson
    # try:
    #     zipfile = path + file_name + "." + form
    #     file = gps.read_file(zipfile)
    #     file.to_file(work_directory + file_name + '.geojson', driver='GeoJSON',
    #                  encoding='utf-8')
    #     print("Данные успешно переведены по пути " + work_directory + file_name + ".geojson")
    #
    # except EOFError as e:
    #     print(e)
    #     print("Не удалось перевести данные в GeoJson")

    # Чтение данных из GeoJson

    try:
        file_json = codecs.open(work_directory + file_name + '.geojson', "r",
                                   "utf_8_sig")
        json_read = file_json.read()
        file_json.close()
        json_data = json.loads(json_read)
        print("Данные успешно прочитаны")

    except EOFError as e:
        print(e)
        print("Ошибка при чтении файла")

    return json_data
