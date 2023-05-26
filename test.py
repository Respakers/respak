from tools.connection import *
from tools.shape_to_json import *
from tools.json_parcer import *
from tools.efis_import import *

#Здесь связать название свойства json и его данные в словарь, чтобы было легче
def json_dict(parser, data):
    count = len(data["features"])
    i = 0
    mas = {}
    for write in parser:
        while i < count:
            mas[write] += data["features"][i]["properties"][write]
            i += 1
        i = 0
    print(mas)
    return mas

def select_column(parser):
    # server, cursor, table = start_db()
    # curs.execute("select * from " + table + " limit 1")
    # col_names = [description[0] for description in curs.description]
    col_names = ['fieldsid', 'raionid', 'sub_name', 'sub_kad', 'reg_name', 'reg_kad', 'reg_oktmo', 'id_sub', 'number_',
                 'area_f', 'date_', 'viewlandid', 'borderforest', 'factopashka', 'cropplanid', 'cropfactid', 'landuser',
                 'land_inn', 'usearea', 'calculationarea', 'gross', 'productivity', 'comment_', 'agrochemicals',
                 'startprocessing', 'endprocessing', 'statusisp', 'unusedid', 'organic', 'typeofrights',
                 'formofownership', 'iscreate', 'isarc', 'isconfirmmo', 'isarcyear', 'rgid', 'orgid',
                 'parentid', 'physicalid', 'updatedate', 'createdate', 'regioncropplancode', 'regioncropfactcode',
                 'islocked', 'tlu', 'crop', 'fact_crop', 'geoworldid', 'reproduction', 'seedorigin', 'seedoriginfarm',
                 'seedoriginregion', 'seedoriginarea', 'seedoriginrepublic', 'seedorigincountry', 'sowingrate',
                 'cultivationseason', 'plantingdatestart', 'platingdateend', 'humuscontent', 'nitrogencontent',
                 'phosphoruscontent', 'potassiumcontent', 'soilacidity', 'soiltype', 'variety', 'status_isp',
                 'transformfield', 'transformcomment', 'chemicalprocessingprintfileid',
                 'chemicalprocessingpesticidefileid']

    diction = {}

    for attr in parser:
        for col in col_names:
            choice = ""
            while choice not in ("1", "2"):
                print("Cопоставить атрибут БД " + col + " и атрибут json " + attr + "?\n 1. Да 2. Нет")
                choice = input()
                if choice == "2":
                    continue
                elif choice != "1":
                    print("Введите 1 или 2")
            if choice == "1":
                diction[col] = attr
                break
    return diction


data = shape_to_geojson("tools/", "2023")

parc = attribute_choser(data)
json_list = json_dict(parc, data)
columns = select_column(json_list)

print(columns)
# i = 0
# count = len(data["features"])
# counter = 0
# while counter < count:
#     for col in columns.values():
#         print(data["features"][i]["properties"][col])
#         i += 1
#     counter += 1
# for col in columns.values():
#     for property in data["features"][0]['properties']:
#         if col == property:
#             columns[]
# stop_db(server)
