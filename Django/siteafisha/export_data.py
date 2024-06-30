import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siteafisha')  # Замените 'your_project' на имя вашего проекта
django.setup()

from django.core import serializers
from django.apps import apps

def export_data():
    data = []
    for model in apps.get_models():
        queryset = model.objects.all()
        data.extend(serializers.serialize('json', queryset, ensure_ascii=False))
    
    with open('db.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    export_data()