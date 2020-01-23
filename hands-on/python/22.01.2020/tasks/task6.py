#Get the value Mats from the Dict

body = {
    'query': {
        'filtered': {
            'query': {
                'match': {'description': 'addictive'}
            },
            'filter': {
                'term': {'created_by': 'Mats'}
            }
        }
    }
}

#Modify the below statement to print Mats
print(body["query"]['filtered']['filter']['term']['created_by'])
