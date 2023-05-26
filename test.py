import sqlite3

from tools.connection import *
from tools.shape_to_json import *
from tools.json_parcer import *
from tools.efis_import import *

# a = [1, 2, 3]
# data = [a, "b", "c", "d"]
# data_key = [1, 2, 3, 4]
# i = 0
# listik = {}
# while i < len(data):
#     listik[data_key[i]] = data[i]
#     i += 1
# print(listik)

# server, curs, table = start_db()

data = shape_to_geojson("2023", "tools/")
parc = attribute_choser(data)

# curs.execute("select * from " + table + " limit 1")
# col_names = [description[0] for description in curs.description]
col_names = ['fieldsid', 'raionid', 'sub_name', 'sub_kad', 'reg_name', 'reg_kad', 'reg_oktmo', 'id_sub', 'number_',
             'area_f', 'date_', 'viewlandid', 'borderforest', 'factopashka', 'cropplanid', 'cropfactid', 'landuser',
             'land_inn', 'usearea', 'calculationarea', 'gross', 'productivity', 'comment_', 'agrochemicals',
             'startprocessing', 'endprocessing', 'statusisp', 'unusedid', 'organic', 'typeofrights', 'formofownership',
             'iscreate', 'isarc', 'isconfirmmo', 'isarcyear', 'rgid', 'orgid', 'parentid', 'physicalid', 'updatedate',
             'createdate', 'regioncropplancode', 'regioncropfactcode', 'islocked', 'tlu', 'crop', 'fact_crop',
             'geoworldid', 'reproduction', 'seedorigin', 'seedoriginfarm', 'seedoriginregion', 'seedoriginarea',
             'seedoriginrepublic', 'seedorigincountry', 'sowingrate', 'cultivationseason', 'plantingdatestart',
             'platingdateend', 'humuscontent', 'nitrogencontent', 'phosphoruscontent', 'potassiumcontent',
             'soilacidity', 'soiltype', 'variety', 'status_isp', 'transformfield', 'transformcomment',
             'chemicalprocessingprintfileid', 'chemicalprocessingpesticidefileid']

diction = {}

for col in col_names:
    for attr in parc:
        if col == attr:
            diction[col] = attr
            break

# stop_db(server)

