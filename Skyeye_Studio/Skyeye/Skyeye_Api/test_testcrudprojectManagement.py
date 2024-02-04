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

    @allure.title("Test Update Project")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_project(self):
        global project_id
        assert jwt_token is not None
        assert workspace_id is not None

        # Update project
        update_project_payload = {
            "query": f"""
            mutation {{
                update_power_pole_project(
                    id: {project_id}
                    data: {{
                        name: "Update_TestProject05"
                        province_id: 51
                        description: "Update_Skyeye_Telecom"
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
        update_project_response = requests.post(GRAPHQL_ENDPOINT, json=update_project_payload, headers=headers)
        update_project_data = update_project_response.json()
        updated_project_info = update_project_data.get("data", {}).get("update_power_pole_project")
        allure.attach(json.dumps(updated_project_info), name="Updated Project Info - Update",
                      attachment_type=allure.attachment_type.JSON)
        assert updated_project_info is not None, "Failed to update project"
        # Assert the expected and actual results
        assert updated_project_info["name"] == "Update_TestProject05", f"Expected name: Update_TestProject05, Actual name: {updated_project_info['name']}"
        assert updated_project_info["description"] == "Update_Skyeye_Telecom", f"Expected description: Update_Skyeye_Telecom, Actual description: {updated_project_info['description']}"
        assert updated_project_info["province_id"] == 51, f"Expected province_id: 51, Actual province_id: {updated_project_info['province_id']}"

        # Print or log the results
        print("\nExpected Result (After Update):")
        print(f"Name: Update_TestProject05\nDescription: Update_Skyeye_Telecom\nProvince ID: 51")

        print("\nActual Result:")
        print(f"Name: {updated_project_info['name']}\nDescription: {updated_project_info['description']}\nProvince ID: {updated_project_info['province_id']}")

    @allure.title("Test Delete Project")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_project(self):
        global project_id
        assert jwt_token is not None
        assert project_id is not None

        # Delete project
        delete_project_payload = {
            "query": f"""
            mutation {{
                remove_power_pole_project(
                    project_id: {project_id}
                )
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        delete_project_response = requests.post(GRAPHQL_ENDPOINT, json=delete_project_payload, headers=headers)
        delete_project_data = delete_project_response.json()
        allure.attach(json.dumps(delete_project_data), name="Delete Project Data",
                      attachment_type=allure.attachment_type.JSON)
        assert "errors" not in delete_project_data, "Failed to delete project"
        assert delete_project_data.get("data", {}).get("remove_power_pole_project") is True, "Delete project failed"

        # Print or log the results
        print("\nExpected Result (After Delete Project):")
        print("Project deleted successfully")

        print("\nActual Result:")
        print(delete_project_data)

        # Delete workspace
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
