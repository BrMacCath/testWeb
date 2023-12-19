from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from Math_161.models import Week,Day,Quiz


class Command(BaseCommand):
    help = "Notices which weeks have a quiz connected to them and sets quiz_boolean to true. Set's all other to false."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("text",type=str)

    def handle(self, *args,**options ) -> str | None:
        text = options["text"]
        print(text)
            

