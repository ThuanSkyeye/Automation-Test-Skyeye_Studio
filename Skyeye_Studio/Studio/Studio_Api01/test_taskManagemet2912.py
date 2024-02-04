import requests
import allure
import json
import pytest
from Skyeye_Studio.Studio.Studio_Api01.test_login import login

BASE_URL = "http://172.25.185.68:1337"
LOGIN_ENDPOINT = "/api/auth/local"
GRAPHQL_ENDPOINT = "http://172.25.254.0:10104/graphql"
jwt_token = None
workspace_id = None
project_id = None
task_id = None


class TestTaskManagement:

    @allure.title("Test Create Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_workspace(self):
        global jwt_token
        jwt_token = login()
        global workspace_id
        assert jwt_token is not None

        # Create workspace
        create_workspace_payload = {
            "query": """
            mutation{
              create_workspace(
              data:
              {
              name:"TestWorkspace05", 
              description:"Skyeye_Telecom", 
              registered_services: ["ElectricPowerPole"]
              },
            org_id: 100
            ){
                id
                name
                description
                registered_services
              }
            }
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        create_workspace_response = requests.post(GRAPHQL_ENDPOINT, json=create_workspace_payload)
        create_workspace_data = create_workspace_response.json()
        workspace_info = create_workspace_data.get("data", {}).get("create_workspace")
        allure.attach(json.dumps(workspace_info), name="Workspace Info - Create",
                      attachment_type=allure.attachment_type.JSON)

        # Lưu ID của workspace vừa tạo
        workspace_id = workspace_info["id"]

    @allure.title("Test Create Project")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_project(self):
        global project_id
        assert jwt_token is not None
        assert workspace_id is not None

        # Create project
        create_project_payload = {
            "query": f"""
            mutation {{
                create_power_pole_project(
                    workspace_id: {workspace_id}
                    data: {{
                        name: "TestProject05"
                        description: "Skyeye_Telecom"
                        province_id: 19
                        is_synchronized: false
                    }}
                ) {{
                    id
                    name
                    description
                    province_id
                }}
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        create_project_response = requests.post(GRAPHQL_ENDPOINT, json=create_project_payload, headers=headers)
        create_project_data = create_project_response.json()
        project_info = create_project_data.get("data", {}).get("create_power_pole_project")
        allure.attach(json.dumps(project_info), name="Project Info - Create",
                      attachment_type=allure.attachment_type.JSON)
        project_id = project_info["id"]

    @allure.title("Test Create Task in Project")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_task_in_project(self):
        global project_id
        assert jwt_token is not None
        assert project_id is not None

        create_task_payload = {
            "query": f"""
            mutation {{
                create_power_pole_task(
                    data: {{
                        project_id: {project_id}
                        name: "TestTaskInProject"
                        description: "Testing Task in Project"
                        type_antenna: "Waterpole"
                        latitude: 12.3456
                        longitude: 78.9101
                        is_synchronized: false
                    }}
                ) {{
                    id
                    name
                    description
                    type_antenna
                    latitude
                    longitude
                    is_synchronized
                }}
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        create_task_response = requests.post(GRAPHQL_ENDPOINT, json=create_task_payload, headers=headers)
        create_task_data = create_task_response.json()
        task_info = create_task_data.get("data", {}).get("create_power_pole_task")
        allure.attach(json.dumps(task_info), name="Task Info - Create",
                      attachment_type=allure.attachment_type.JSON)
        assert task_info is not None, "Failed to create task in project"

        # Print or log the results
        print("\nExpected Result (Create Task in Project):")
        print(f"Task created successfully in project with ID: {project_id}")

        print("\nActual Result:")
        print(f"Task ID: {task_id}")

        # Check task details
        check_task_payload = {
            "query": """
            query {
              all_power_pole_task_of_project(
                q: {
                  order_by: { name: "created_time", choice: Descending }
                  pagination: { page_index: 0, page_size: 5 }
                  search: ""
                }
                project_id: {project_id}
              ) {
                data {
                  id
                  project_id
                  name
                  type_antenna
                  description
                  latitude
                  longitude
                }
                total
              }
            }
            """ % project_id
        }
        check_task_response = requests.post(GRAPHQL_ENDPOINT, json=check_task_payload, headers=headers)
        check_task_data = check_task_response.json()
        tasks = check_task_data.get("data", {}).get("all_power_pole_task_of_project", {}).get("data", [])

        # Assert the expected and actual results for the first task in the list
        assert len(tasks) > 0, "No tasks found in the project"
        first_task = tasks[0]
        assert first_task["id"] == task_id, f"Expected Task ID: {task_id}, Actual Task ID: {first_task['id']}"
        assert first_task[
                   "project_id"] == project_id, f"Expected Project ID: {project_id}, Actual Project ID: {first_task['project_id']}"
        assert first_task[
                   "name"] == "TestTask01", f"Expected Task Name: TestTask01, Actual Task Name: {first_task['name']}"
        assert first_task[
                   "type_antenna"] == "GuyedTower", f"Expected Type Antenna: GuyedTower, Actual Type Antenna: {first_task['type_antenna']}"
        assert first_task[
                   "description"] == "Skyeye_Telecom", f"Expected Description: Skyeye_Telecom, Actual Description: {first_task['description']}"
        assert first_task[
                   "latitude"] == 21.064630472940046, f"Expected Latitude: 21.064630472940046, Actual Latitude: {first_task['latitude']}"
        assert first_task[
                   "longitude"] == 105.77901989221574, f"Expected Longitude: 105.77901989221574, Actual Longitude: {first_task['longitude']}"


if __name__ == "__main__":
    pytest.main([__file__])
