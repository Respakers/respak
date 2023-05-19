class GeojsonParcer():
    def __init__(self, json_data):
        self.__json_data = json_data
        self.__json_len = len(json_data["features"])

    def attribute_parcer(self):
        feature_list = []
        for properties in self.__json_data["features"][0]['properties']:
            feature_list.append(properties)
        return feature_list

    def attribute_choser(self):
        all_attributes = self.attribute_parcer()
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
                else:
                    print("Неправильный формат ввода!")
            if chosen == "3":
                print("Выбор закончен")
                break
        return used_attributes




