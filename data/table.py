from .models import Data
from table import Table
from table.columns import Column



class DataTable(Table):
    end_year = Column(field='end_year')
    intensity = Column(field='intensity')
    sector =Column(field='sector')
    topic = Column(field='topic')
    insight = Column(field='insight')
    url = Column(field='url')
    region = Column(field='region')
    start_year =Column(field='start_year')
    impact = Column(field='impact')
    added = Column(field='added')
    published = Column(field='published')
    country = Column(field='country')
    relevance = Column(field='relevance')
    pestle = Column(field='pestle')
    source =Column(field='source')
    title =Column(field='title')
    likelihood = Column(field='likelihood')

    class Meta:
        model = Data
