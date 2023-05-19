import json
import sys
import psycopg2
from sshtunnel import SSHTunnelForwarder
import xmltodict
import codecs

class Import():
    def __init__(self, json_file: json, connection, data: dict):
        self.geojson_data = json_file
        self.conn = connection
        self.data = data

    def import_old_format(self):
        request = {}
        cur = self.conn.cursor()
        for features in self.geojson_data["features"]:
            for element in self.data.keys():
                el = str(features['properties'][str(self.data[str(element)])])
                if element == 'id_sub':
                    request.update({"id_sub": "'" + el + "'"})
                elif element == 'reg_kad':
                    request.update({"reg_kad": el.split(".0")[0]})
                    request.update({"reg_name": "select ror.\"name\" from resp_organizationregistry_raionrequisites ror  where ror.codelp = '" + el.split(".0")[0] + "' limit 1"})
                    request.update({"reg_name": "select ror.oktmo from resp_organizationregistry_raionrequisites ror  where ror.codelp = '" + el.split(".0")[0] + "' limit 1"})
                elif element == 'cropplanid':
                    request.update({"cropplanid": ""})







