def serialize_search(items):
    results = []
    for item in items:
        results.append({
            'id': item.pk,
            'place_name': item.place_name,
            'subnational_entity': item.subnational_entity,
            'postal_code': item.postal_code
        })
        
    return results
