from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

        # Agregar los tres miembros especificados
        self.add_member({
            "first_name": "John",
            "last_name": last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

        self.add_member({
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5,
            "lucky_numbers": [1]
        })

    def _generateId(self):
        # Cambiar la generación de IDs aleatorios por una asignación secuencial
        new_id = len(self._members)
        return new_id

    def add_member(self, member):
        member_id = self._generateId()
        member["id"] = member_id
        self._members.append(member)
        return member_id

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def update_member(self, id, new_member):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i] = new_member
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
