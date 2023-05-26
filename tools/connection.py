import sys
import psycopg2
from sshtunnel import SSHTunnelForwarder
import xmltodict
import codecs


def start_db():
    handle = codecs.open("config.xml", "r", "utf_8_sig")
    content = handle.read()
    data = xmltodict.parse(content)

    db_names = ["omega", "beta", "kalmikia", "irkutsk", "bashkiria", "altai"]
    print("Список доступных серверов:\n1.Омега\n2.Бета\n3.Калмыкия\n4.Иркутск\n5.Башкирия\n6.Алтай")
    server_name = db_names[int(input()) - 1]
    server = connect_SSH(server_name, data)
    conn = connect_DB(server_name, server)
    table = table_names(server_name)
    return server, conn, table


def connect_SSH(server_name, data):
    print(data['server'][server_name]['ssh']['host'])
    # Подключаемся к серверу
    try:
        server = SSHTunnelForwarder(
            (str(data['server'][server_name]['ssh']['host']),
             int(data['server'][server_name]['ssh']['port'])),
            ssh_username=str(data['server'][server_name]['ssh']['user']),
            ssh_password=str(data['server'][server_name]['ssh']['password']),
            remote_bind_address=('localhost', 5432),
            local_bind_address=('localhost', 22)
        )

        server.start()
        print("Подключились к серверу")

    except EOFError as e:
        print(e)
        print("Не удалось подключиться к серверу")
        sys.exit()

    return server


def connect_DB(server_name, server):
    # Подключаемся к БД

    print(server_name)

    try:
        conn = psycopg2.connect(dbname=str(data['server'][server_name]['db']['dbname']),
                                user=str(data['server'][server_name]['db']['user']),
                                password=str(data['server'][server_name]['db']['password']),
                                host=server.local_bind_host,
                                port=server.local_bind_port)
        # Проверка на работоспособность запросов в БД
        cur = conn.cursor()
        cur.execute("select * from organization_ limit 1")
        count = cur.fetchall()
        print("Обращение к БД успешно")

    except EOFError as e:
        print(e)
        print("Не удалось подключиться к БД")
        server.stop()
        sys.exit()

    return cur


def table_names (server_name):
    if server_name == "omega" or server_name == "kalmikia":
        table = "resp2_0_land_field"
    else:
        table = "cadastr_fields"
    return table


def stop_db(server):
    server.stop()
    server.close()
