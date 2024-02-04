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
task_id = None

class TestTaskManagement:
    @pytest.mark.Skyeye_Telecom
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
              name:"TestWorkspace06", 
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
        workspace_id = workspace_info["id"]

    @allure.title("Test Create Project")
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
                        name: "TestProject06",
                        description: "Skyeye_Telecom",
                        province_id: 19,
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

    @allure.title("Test Create Task")
    def test_create_task(self):
        global task_id
        assert jwt_token is not None
        assert workspace_id is not None
        assert project_id is not None

        # Create task
        create_task_payload = {
            "query": f"""
            mutation {{
                create_power_pole_task(
                    data: {{
                        project_id: {project_id},
                        name: "TestTask",
                        description: "Testing",
                        type_antenna: "Waterpole",
                        latitude: 12.3456,
                        longitude: 78.9101,
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
        allure.attach(json.dumps(task_info), name="Task Info - Create", attachment_type=allure.attachment_type.JSON)

        # Assert the expected and actual results
        assert task_info is not None, "Failed to create task"
        assert task_info["name"] == "TestTask", f"Expected name: TestTask, Actual name: {task_info['name']}"
        assert task_info["description"] == "Testing", f"Expected description: Testing, Actual description: {task_info['description']}"
        assert task_info["type_antenna"] == "Waterpole", f"Expected type_antenna: Waterpole, Actual type_antenna: {task_info['type_antenna']}"
        assert task_info["latitude"] == 12.3456, f"Expected latitude: 12.3456, Actual latitude: {task_info['latitude']}"
        assert task_info["longitude"] == 78.9101, f"Expected longitude: 78.9101, Actual longitude: {task_info['longitude']}"
        assert task_info["is_synchronized"] is False, f"Expected is_synchronized: False, Actual is_synchronized: {task_info['is_synchronized']}"

        # Save the ID of the created task
        task_id = task_info["id"]

        # Print or log the results
        print("\nExpected Result (Create Task):")
        print(
            f"Name: TestTask\nDescription: Testing\nType Antenna: Waterpole\nLatitude: 12.3456\nLongitude: 78.9101\nIs Synchronized: False")

        print("\nActual Result:")
        print(
            f"Name: {task_info['name']}\nDescription: {task_info['description']}\nType Antenna: {task_info['type_antenna']}\n"
            f"Latitude: {task_info['latitude']}\nLongitude: {task_info['longitude']}\nIs Synchronized: {task_info['is_synchronized']}")

    @allure.title("Test Update Task")
    def test_update_task(self):
        global task_id
        assert jwt_token is not None

        # Update task
        update_task_payload = {
            "query": f"""
            mutation {{
                update_power_pole_task(
                    id: {task_id},
                    data: {{
                        name: "UpdatedTaskName",
                        description: "UpdatedTaskDescription",
                        type_antenna: "Rooftop"
                    }}
                ) {{
                    id
                    name
                    description
                    type_antenna
                }}
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        update_task_response = requests.post(GRAPHQL_ENDPOINT, json=update_task_payload, headers=headers)
        update_task_data = update_task_response.json()
        updated_task_info = update_task_data.get("data", {}).get("update_power_pole_task")
        allure.attach(json.dumps(updated_task_info), name="Updated Task Info - Update",
                      attachment_type=allure.attachment_type.JSON)

        # Assert the expected and actual results
        assert updated_task_info is not None, "Failed to update task"
        assert updated_task_info["name"] == "UpdatedTaskName", f"Expected name: UpdatedTaskName, Actual name: {updated_task_info['name']}"
        assert updated_task_info["description"] == "UpdatedTaskDescription", f"Expected description: UpdatedTaskDescription, Actual description: {updated_task_info['description']}"
        assert updated_task_info["type_antenna"] == "Rooftop", f"Expected type_antenna: Rooftop, Actual type_antenna: {updated_task_info['type_antenna']}"

        # Print or log the results
        print("\nExpected Result (After Update Task):")
        print(f"Name: UpdatedTaskName\nDescription: UpdatedTaskDescription\nType Antenna: Rooftop")

        print("\nActual Result:")
        print(
            f"Name: {updated_task_info['name']}\nDescription: {updated_task_info['description']}\nType Antenna: {updated_task_info['type_antenna']}")

    @allure.title("Test Delete Task")
    def test_delete_task(self):
        global task_id
        assert jwt_token is not None
        assert task_id is not None

        # Delete task
        delete_task_payload = {
            "query": f"""
            mutation {{
                remove_power_pole_task(
                    task_id: {task_id}
                )
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        delete_task_response = requests.post(GRAPHQL_ENDPOINT, json=delete_task_payload, headers=headers)
        allure.attach(delete_task_response.text.strip(), name="Delete Task Response Content",
                      attachment_type=allure.attachment_type.TEXT)
        delete_task_data = delete_task_response.json()
        assert "errors" not in delete_task_data, "Failed to delete task"
        assert delete_task_data.get("data", {}).get("remove_power_pole_task") is True, "Delete task failed"

        # Print or log the results
        print("\nExpected Result (After Delete Task):")
        print("Task deleted successfully")

        print("\nActual Result:")
        print(delete_task_data)
        delete_workspace_payload = {
            "query": f"""
            mutation {{
                delete_workspace(
                    id: {workspace_id}
                )
            }}
            """
        }
        delete_workspace_response = requests.post(GRAPHQL_ENDPOINT, json=delete_workspace_payload, headers=headers)
        delete_workspace_data = delete_workspace_response.json()
        allure.attach(json.dumps(delete_workspace_data), name="Delete Workspace Data",
                      attachment_type=allure.attachment_type.JSON)


if __name__ == "__main__":
    pytest.main([__file__])
