import re
import json


class Panda:

    def __init__(self, name, email, gender):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            raise ValueError
        else:
            self.email = email
            self.name = name
            self.gender = gender

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def isMale(self):
        return self.gender == "male"

    def isFemale(self):
        return self.gender == "female"

    def __eq__(self, other):
        your_name = self.name == other.name
        your_email = self.email == other.email
        your_gender = self.gender == other.gender
        return your_name and your_email and your_gender

    def __str__(self):
        return "Panda {} with email {} and {} gender."\
            .format(self.name, self.email, self.gender)

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(self.name,
                                                self.email, self.gender)

    def __hash__(self):
        return hash(self.__str__())


def serialize_to(path, data):
    json_string = json.dumps(data, indent=4)

    with open(path, 'w') as outfile:
        outfile.write(json_string)


def unserialize_from(path):
    with open(path, 'r') as infile:
        contents = infile.read()

    return json.loads(contents)


ivo = Panda("Ivo", "ivo@pandamail.com", "male")
serialize_to("panda.json", repr(ivo))

print (unserialize_from("panda.json"))
