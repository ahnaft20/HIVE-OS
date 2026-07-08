from datetime import datetime


class Organization:

    def __init__(self):

        self.organization = {

            "CEO": None,

            "Departments": {},

        }

    def set_ceo(self, name):

        self.organization["CEO"] = {

            "name": name,

            "appointed": datetime.now().strftime("%H:%M:%S"),

        }

    def create_department(self, name):

        if name not in self.organization["Departments"]:

            self.organization["Departments"][name] = {

                "manager": None,

                "members": [],

            }

    def appoint_manager(
        self,
        department,
        manager,
    ):

        self.create_department(department)

        self.organization["Departments"][department]["manager"] = manager

    def add_member(
        self,
        department,
        member,
    ):

        self.create_department(department)

        if member not in self.organization["Departments"][department]["members"]:

            self.organization["Departments"][department]["members"].append(member)

    def export(self):

        return self.organization