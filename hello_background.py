def hello_background(data, context):
    """Background Cloud Function.
    Args:
         data (dict): The dictionary with data specific to the given event.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata.
    """
    if data and 'name' in data:
        name = data['name']
    else:
        name = 'World'
    return 'Hello, {}!'.format(name)
