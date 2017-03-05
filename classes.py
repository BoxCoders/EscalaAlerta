class Post:
    """define os postos militares: 2º Ten, 1º Ten, Cap, etc"""

    posts = ["2º Ten", "1º Ten", "Cap", "Maj", "TCel", "Cel"]

    def __init__(self):
        self.post = [post for post in self.posts]

    def __getitem__(self, item):
        return self.post[item]

    def __len__(self):
        return len(self.post)

post = Post()


class Unavailability:
    """define períodos de indisponibilidade"""

    def __init__(self, begin, end, reason):
        self.begin = begin
        self.end = end
        self.reason = reason

    #TODO = criar métodos



class Point:
    """define o tipo de 'quadrinho' da escala de serviço"""

    colors = ["preta", "vermelha", "amarela", "roxa"]

    def __init__(self):
        self.color = [color for color in self.colors]

    def __getitem__(self, item):
        return self.color[item]

point = Point()


class Service(Point):
    """define a data do serviço"""

    def __init__(self, color, date):
        self.color = color
        self.date = date
        super(Service, self).__init__()


class Ballast(Point):
    """define lastros de serviço"""

    def __init__(self, color, quantity, cause):
        self.color = color
        self.quantity = quantity
        self.cause = cause
        super(Ballast, self).__init__()


class Pilot:
    """define os pilotos"""

    def __init__(self, post, name, trigram, unavailabilities, services, ballasts):
        self.post = post
        self.name = name
        self.trigram = trigram
        self.unavailabilities = unavailabilities
        self.services = services
        self.ballasts = ballasts

    def __str__(self):
        return self.trigram

    # TODO = criar métodos


class Rank:
    """define a antiguidade entre os pilotos"""

    def __init__(self, rank, trigram):
        self.rank = rank
        self.trigram = trigram

    # TODO = criar métodos


class Schedule:
    """define a escala de serviço"""

    def __init__(self, date, trigram):
        self.date = date
        self.trigram = trigram

    #TODO = criar métodos