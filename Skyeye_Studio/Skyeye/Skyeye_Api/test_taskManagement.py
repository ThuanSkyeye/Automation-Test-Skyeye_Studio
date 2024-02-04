import requests
import allure
import json
import pytest

BASE_URL = "http://172.25.254.0:1337"
LOGIN_ENDPOINT = "/api/auth/local"
GRAPHQL_ENDPOINT = "http://172.25.254.0:10104/graphql"
jwt_token = None
workspace_id = None
project_id = None


class TestProjectManagement:
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test Login")
    def test_login(self):
        global jwt_token
        login_payload = {
            "identifier": "vanthuancontact@gmail.com",
            "password": "Kentran212431302$"
        }
        login_response = requests.post(BASE_URL + LOGIN_ENDPOINT, json=login_payload)
        login_data = login_response.json()
        jwt_token = login_data.get("jwt")
        allure.attach(jwt_token, name="JWT Token", attachment_type=allure.attachment_type.TEXT)
        assert jwt_token is not None, "Login failed"

    @allure.title("Test Create Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_workspace(self):
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
        # Assert the expected and actual results
        assert project_info is not None, "Failed to create project"
        assert project_info[
                   "name"] == "TestProject05", f"Expected name: TestProject05, Actual name: {project_info['name']}"
        assert project_info[
                   "description"] == "Skyeye_Telecom", f"Expected description: Skyeye_Telecom, Actual description: {project_info['description']}"
        assert project_info[
                   "province_id"] == 19, f"Expected province_id: 19, Actual province_id: {project_info['province_id']}"

        # Print or log the results
        print("\nExpected Result (Create Project):")
        print(f"Name: TestProject05\nDescription: Skyeye_Telecom\nProvince ID: 19")

        print("\nActual Result:")
        print(
            f"Name: {project_info['name']}\nDescription: {project_info['description']}\nProvince ID: {project_info['province_id']}")

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


if __name__ == "__main__":
    pytest.main([__file__])
