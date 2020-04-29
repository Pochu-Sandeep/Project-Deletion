from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

class computevm:    
   
    def vm_instance_details(self,project_id):
        
        credentials = GoogleCredentials.get_application_default()
        
        service = discovery.build('compute', 'v1', credentials=credentials)
        
        instance_exist = False
            
        zone_request = service.zones().list(project = project_id)

        zone_response = zone_request.execute()
                
        for zone_details in zone_response['items']:
                 
            zone_name=zone_details.get("name")
            
            print(zone_name)
            
            instance_request = service.instances().list(project = project_id, zone = zone_name)
            
            instance_response = instance_request.execute()
            
            instance_details = instance_response.get("items","")
                                        
            if len(instance_details) > 0:
                
                instance_exist =  True  
                
                break
               
        if instance_exist ==1:
            
            print("Instances exists in project please delete ........." +project_id)
                  
        else:
                    
            print("Instances doesn't exists in the project " +project_id)
        
        print(instance_exist)
                       
        return instance_exist
                
            
                    
                    
