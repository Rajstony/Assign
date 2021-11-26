from google.cloud import google_api_client
from google.apiclient import discovery
service = discovery.build('compute', 'v1')
print('VM Instance starting')

project = 'us-gcp-ame-con-116-npd-1'

zone = 'uswest2a'

instance = 'murugt-hu-word'

request = service.instances().stop(project = 'us-gcp-ame-con-116-npd-1', zone = 'uswest2a', instance = 'murugt-hu-word')
response = request.execute()