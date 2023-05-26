def attribute_parcer(json_data):
    feature_list = []
    for properties in json_data["features"][0]['properties']:
        feature_list.append(properties)
    return feature_list


def attribute_choser(json_data):
    all_attributes = attribute_parcer(json_data)
    print(all_attributes)
    used_attributes = []
    for attribute in all_attributes:
        chosen = ""
        while chosen not in ("1", "2", "3"):
            print("Использовать ли атрибут " + str(attribute) + "\n1. Да\n2. Нет\n3. Закончить выбор")
            chosen = input()
            if chosen == "1":
                print("Атрибут использован")
                used_attributes.append(str(attribute))
            elif chosen == "2":
                print("Атрибут не использован")
            elif chosen != "3":
                print("Неправильный формат ввода!")
        if chosen == "3":
            print("Выбор закончен")
            break
    return used_attributes
