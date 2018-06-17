from os import walk
import datetime

from django.core.management.base import BaseCommand
import yaml

from entities.models import Entity


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.entities = []

    def add_arguments(self, parser):
        parser.add_argument("path")

    def handle(self, *args, **options):
        path = options["path"]
        self.load(path)

        for e in self.entities:
            Entity.objects.create(
                title=e["title"],
                publishedAt=e["published_at"],
                content=e["content"]
            )
            self.stdout.write(self.style.SUCCESS("created %s" % e["title"]))

    def load(self, path):
        files = []
        self.stdout.write(path)

        for (dirpath, dirnames, filenames) in walk(path):
            for name in filenames:
                if not name.startswith("."):
                    files.append(path + "/" + name)

        for file in files:
            with open(file, 'r') as infile:
                (header, separator, content) = infile.read().partition("---")
                header = yaml.load(header)

                entity = {
                    "title": header["title"],
                    "published_at": header["date"],
                    "content": content.strip()
                }

                #  d = header["date"]
                """if d.__class__ == datetime.datetime.__class__:
                    entity["published_at"] = "%s-%s-%sT%s:%s:%s.00Z" % (
                        d.year, d.strftime('%m'), d.strftime('%d'),
                        d.strftime('%H'), d.strftime('%M'), d.strftime('%S')
                    )
                else:
                    entity["published_at"] = "%s-%s-%sT00:00:00.00Z" % (
                        d.year, d.strftime('%m'), d.strftime('%d')
                    )"""

                self.entities.append(entity)
