import os

from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

class main:
    
    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

    def services(self):

        #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/sandeep_pochu/sap-coe-devops-test-e30e34abb448.json'
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'echo $GOOGLE_APPLICATION_CREDENTIALS'

        projects = os.getenv("Project_id")
        
        projects_list = projects.split(",")

        for projects in projects_list:

            project_id = projects

            from project_deletion.computevm import computevm

            obj_computevm = computevm()

            instance_exist = obj_computevm.vm_instance_details(project_id)

            from project_deletion.disks import disks

            obj_disks = disks()

            disks_exist = obj_disks.disks_details(project_id)

            from project_deletion.vpn import vpn

            obj_vpn = vpn()

            vpn_exist = obj_vpn.vpn_details(project_id)

            from project_deletion.firewall import firewall

            obj_firewall = firewall()

            firewall_exist = obj_firewall.firewall_details(project_id)

            if (instance_exist | disks_exist | vpn_exist | firewall_exist):

                print("Project will not  be deleted")

            else:

                print(project_id)

                #request = service.projects().delete(projectId=project_id)

                #request.execute()
                
                from project_deletion.projectdeletion import projectdeletion
                
                obj_projectdeletion = projectdeletion()
                
                obj_projectdeletion.projectdeletion(project_id)

                print("Project is now shutdown")

obj_main = main()

obj_main.services()
