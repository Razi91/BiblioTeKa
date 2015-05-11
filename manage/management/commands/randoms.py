__author__ = 'jkonieczny'

from books.models import *

import random
import datetime
from django.core.management.base import BaseCommand, CommandError

_names1 = [
    "JAKUB",
    "KACPER",
    "SZYMON",
    "MATEUSZ",
    "FILIP",
    "MICHAŁ",
    "BARTOSZ",
    "WIKTOR",
    "PIOTR",
    "DAWID",
    "ADAM",
    "MACIEJ",
    "JAN",
    "IGOR",
    "MIKOŁAJ",
    "PATRYK",
    "PAWEŁ",
    "DOMINIK",
    "OSKAR",
    "ANTONI",
    "WOJCIECH",
    "KAMIL",
    "ALEKSANDER",
    "KRZYSZTOF",
    "OLIWIER",
    "MARCEL",
    "KAROL",
    "FRANCISZEK",
    "TOMASZ",
    "HUBERT",
    "BARTŁOMIEJ",
    "ADRIAN",
    "ALAN",
    "SEBASTIAN",
    "MIŁOSZ",
    "KRYSTIAN",
    "ŁUKASZ",
    "NIKODEM",
    "GABRIEL",
    "MARCIN",
    "STANISŁAW",
    "DAMIAN",
    "KONRAD",
    "DANIEL",
    "FABIAN",
    "BŁAEJ",
    "RAFAŁ",
    "TYMOTEUSZ",
    "KSAWERY"]


_names2 = [u"NOWAK",
    u"KOWALSKI",
    u"WIŚNIEWSKI",
    u"WÓJCIK",
    u"KOWALCZYK",
    u"KAMIŃSKI",
    u"LEWANDOWSKI",
    u"ZIELIŃSKI",
    u"WOŹNIAK",
    u"SZYMAŃSKI",
    u"DĄBROWSKI",
    u"KOZŁOWSKI",
    u"JANKOWSKI",
    u"MAZUR",
    u"KWIATKOWSKI",
    u"WOJCIECHOWSKI",
    u"KRAWCZYK",
    u"KACZMAREK",
    u"PIOTROWSKI",
    u"GRABOWSKI",
    u"ZAJĄC",
    u"PAWŁOWSKI",
    u"KRÓL",
    u"MICHALSKI",
    u"WRÓBEL",
    u"WIECZOREK",
    u"JABŁOŃSKI",
    u"NOWAKOWSKI",
    u"MAJEWSKI",
    u"OLSZEWSKI",
    u"STĘPIEŃ",
    u"DUDEK",
    u"JAWORSKI",
    u"MALINOWSKI",
    u"ADAMCZYK",
    u"PAWLAK",
    u"GÓRSKI",
    u"NOWICKI",
    u"SIKORA",
    u"WITKOWSKI",
    u"WALCZAK",
    u"RUTKOWSKI",
    u"BARAN",
    u"MICHALAK",
    u"SZEWCZYK",
    u"OSTROWSKI",
    u"TOMASZEWSKI",
    u"ZALEWSKI",
    u"WRÓBLEWSKI",
    u"PIETRZAK"]

_titles = ['łyżka',
'ręka',
'ucho',
'kolczyk',
'bluzka',
'koc',
'buty',
'kot',
'piasek',
'lawa',
'rekin',
'szuflada',
'figurka',
'biurko',
'mata',
'woda',
'kanapka',
'wózek',
'lalka',
'gitara',
'bębny',
'pianino',
'talerz',
'puzzle',
'tygrys',
'miś',
'linoleum',
'naklejka',
'folder',
'plik',
'lista',
'zegar',
'lis',
'motyl',
'klawiatura',
'kamera',
'aparat',
'telefon',
'kabaretki',
'pończochy',
'sukienka',
'żółw',
'ryba',
'ość',
'lód',
'schabowe',
'sałatka',
'samochód']

_genres = ['powieść',
'nowela',
'opowiadanie',
'epopeja',
'baśń',
'mit',
'legenda',
'pamiętnik',
'przypowieść	',
'oda',
'hymn',
'pieśń',
'tren',
'elegi',
'fraszka',
'epigramat',
'sonet	',
'dramat właściwy',
'tragedia',
'komedia',
'farsa',
'tragifarsa',
'opera']

_pub = ['GREG', 'PWN', 'ISKRA', u'Prószyński i S-ka', 'Znak']

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        authors = []
        for i in range(30):
            a = Author()
            name = _names1[int(random.random()*len(_names1))]
            name +=' ' + _names1[int(random.random()*len(_names1))]
            a.name = name
            a.born = datetime.date(1980, 1, 1)
            a.save()
            authors.append(a)

        genres = []
        for i in _genres:
            g = Genre()
            g.name = i
            g.save()
            genres.append(g)

        titles = []
        for i in range(150):
            t = BookTitle()
            t.release = datetime.date(1900+int(random.random()*115), int(1+random.random()*10), int(1+random.random()*25))
            t.title = _titles[int(random.random()*len(_titles))]
            t.save()
            for i in range(1+int(max(0, random.normalvariate(0, 1)))):
                t.author.add(authors[int(random.random()*len(authors))])
            for i in range(1+int(max(0, random.normalvariate(0, 1)))):
                t.genre.add(genres[int(random.random()*len(genres))])
            titles.append(t)
            t.save()

        publisher = []
        for pu in _pub:
            p = Publisher()
            p.name = pu
            p.save()
            publisher.append(p)

        pricing = []
        for i in range(1, 5):
            p = Pricing()
            p.name = "{0}".format(i)
            p.added = (datetime.datetime.now() - datetime.timedelta(days=random.random()*365*10))
            p.initial = i
            p.per_week = i
            p.save()
            pricing.append(p)

        for title in titles[:-5]:
            for _e in range(1+int(min(0,random.normalvariate(0,1)))):
                edition = BookEdition()
                edition.publisher = publisher[int(random.random()*len(publisher))]
                edition.isbn = ''
                edition.release = (datetime.datetime.now() - datetime.timedelta(days=random.random()*365*10)).date()
                edition.title = title
                edition.pricing = pricing[int(random.random()*len(pricing))]
                edition.save()
                for i in range(int(random.random()*20)):
                    entity = BookEntity()
                    entity.title = title
                    entity.book = edition
                    entity.quality = max(10, min(0, random.normalvariate(7, 5)))
                    entity.save()