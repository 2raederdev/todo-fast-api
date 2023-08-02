from datetime import datetime

from pydantic import BaseModel

class Item(BaseModel):
    title: str
    description: str | None = None
    is_done: bool

    class Config:
      orm_mode = True

items = [
    {
        'title': 'Get flight tickets',
        'description': 'Buy tickets to Berlin for next month',
        'is_done': False,
    },
    {
        'title': 'Lula\'s doc',
        'description': 'Schedule an appointment with the vet for Lula',
        'is_done': True,
    }
]