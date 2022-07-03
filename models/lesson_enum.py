from enum import Enum
from models_manager import Model, Field, FieldGenericEnum

class Config(Enum):
    dev = 'dev'
    test = 'test'
    prod = 'prod'
    
    @classmethod
    def list(cls):
        return [domain.value for domain in cls]

print(Config.dev.value)
print(Config.list())

for domain in Config:
    print(domain)

print(Config['dev'].value)

def get_url(domain: Config):
    pass


get_url(Config.dev)

class Config(FieldGenericEnum):
    active = 'active'
    disabled = 'disabled'
    pending = 'pending'

class Course(Model):
    id = Field(category=int, json='id')
    title = Field(category=str, json='title')
    status = Field(category=str, json='status', choices=Config.to_list())


print(Course.manager.to_schema)