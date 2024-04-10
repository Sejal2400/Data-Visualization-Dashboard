import json
from django.core.management.base import BaseCommand
from data.models import Data


class Command(BaseCommand):
    help= 'Import External json File data  into sqllite database'

    def handle(self,*args,**kwargs):
        with open(r'C:\Users\USER\Desktop\assignment_blackcoffer\project\jsondata.json','r',encoding='utf8') as file:
            data = json.load(file)
            #print(data)
            for item in data:
                Data.objects.create(
                    end_year=item['end_year'],   
                    intensity=item['intensity'],
                    sector=item['sector'], 
                    topic=item['topic'], 
                    insight=item['insight'], 
                    url=item['url'], 
                    region=item['region'], 
                    start_year=item['start_year'], 
                    impact=item['impact'], 
                    added=item['added'], 
                    published=item['published'], 
                    country=item['country'], 
                    relevance=item['relevance'], 
                    pestle=item['pestle'], 
                    source=item['source'], 
                    title=item['title'], 
                    likelihood=item['likelihood'], 

                         )
                self.stdout.write(self.style.SUCCESS('Done'))
                                 
