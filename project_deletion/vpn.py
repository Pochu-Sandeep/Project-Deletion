from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

class vpn:
    
    def vpn_details(self,project_id):
        
        credentials = GoogleCredentials.get_application_default()
        
        service = discovery.build('compute', 'v1', credentials = credentials)
        
        vpn_exist = False
        
        vpn_list_request = service.networks().list(project = project_id)
        
        vpn_list_response = vpn_list_request.execute()
        
        vpn_details = vpn_list_response.get("items","")
        
        len(vpn_details)
        
        if len(vpn_details)>0:
            
            vpn_exist = True
            
            print("VPN exists in project, please delete ..... " +project_id)
            
        else:
            
            print("VPN does not exists in the project " +project_id)
          
        return vpn_exist
