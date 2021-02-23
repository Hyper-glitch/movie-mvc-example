class Actor:
    def __init__(self, name, last_name, role):
        self._name = name
        self._last_name = last_name
        self._role = role

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def role(self):
        return self._role

    def __str__(self):
        return f"{self.name} {self.last_name} in {self.role} role"


class Movie:
    def __init__(self, title, date_released, actors):
        self._title = title
        self._date_released = date_released
        self._actors = actors

    @property
    def title(self):
        return self._title

    @property
    def date_released(self):
        return self._date_released

    @property
    def actors(self):
        return self._actors

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Date released: {self.date_released}\n" \
               f"Cast: {self.actors}"
    
