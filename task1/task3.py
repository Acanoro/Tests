documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    name = list(map(lambda x: x["name"], filter(lambda x: x["number"] == doc_number, documents)))
    if name:
        return name[0]
    else:
        return "Документ не найден"


def get_directory(doc_number):
    directory = list(filter(lambda x: doc_number in x[1], directories.items()))

    if directory:
        return directory[0][0]
    else:
        return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    documents.append(
        {
            "type": document_type,
            "number": number,
            "name": name,
        }
    )

    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]


if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
