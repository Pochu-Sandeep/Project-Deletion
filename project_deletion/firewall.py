from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

class firewall:
        
    def firewall_details(self,project_id):
        
        credentials = GoogleCredentials.get_application_default()
        
        service = discovery.build('compute', 'v1', credentials = credentials)
        
        firewall_exist = False
        
        firewall_request = service.firewalls().list(project = project_id)

        firewall_response = firewall_request.execute()
        
        firewall_details = firewall_response.get("items","")
        
        len(firewall_details)
        
        if len(firewall_details)>0:
            
            firewall_exist = True
            
            print("Firewalls exists in project, please delete")
            
        else:
            
            print("Firewalls doesn't exist in the project")
            
        return firewall_exist
