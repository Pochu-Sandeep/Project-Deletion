from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

class projectdeletion:
    
    def projectdeletion(self,project_id):

        credentials = GoogleCredentials.get_application_default()

        service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
        
        request = service.projects().delete(projectId=project_id)
        
        request.execute()
