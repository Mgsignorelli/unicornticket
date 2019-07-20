from datetime import datetime

import pytz

from tickets.models import BugWork, FeatureWork


def get_aggregate_count(definition):
    output = []

    for d in definition:
        bugs_count = BugWork.objects.filter(created__range=(
            d.get('range')[0],
            d.get('range')[1],
        )).count()
        features_count = FeatureWork.objects.filter(created__range=(
            d.get('range')[0],
            d.get('range')[1],
        )).count()

        output.append({
            'label': d.get('label'),
            'range': {
                'start': str(d.get('range')[0]),
                'start': str(d.get('range')[1]),
            },
            'bugs': bugs_count,
            'features': features_count,
        })

    return output
