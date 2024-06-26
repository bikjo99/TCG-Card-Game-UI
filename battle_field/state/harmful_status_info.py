class HarmfulStatusInfo:
    def __init__(self):
        self.harmful_status = {}

    def update_harmful_status(self, unit_index, harmful_status):
        print(type(unit_index))
        print(f"update_harmful_status_of_unit: index - {unit_index}")
        print(f"current_harmful_status_info: {self.harmful_status}")
        self.harmful_status.update()
        if unit_index not in self.harmful_status.keys():
            self.harmful_status[unit_index] = []
            self.harmful_status[unit_index] = harmful_status
        else:
            self.harmful_status[unit_index] = harmful_status

        print(f"updated_harmful_status_info: {self.harmful_status}")

    def is_index_in_harmful_status(self, index):
        if index in self.harmful_status.keys():
            return True
        else:
            return False

    def get_harmful_status_of_index(self, unit_index):

        if unit_index in self.harmful_status.keys():
            return self.harmful_status[unit_index]
        else:
            return None

    def remove_harmful_status_of_index(self, unit_index):
        if unit_index not in self.harmful_status.keys():
            return None
        else:
            self.harmful_status.pop(unit_index, None)

