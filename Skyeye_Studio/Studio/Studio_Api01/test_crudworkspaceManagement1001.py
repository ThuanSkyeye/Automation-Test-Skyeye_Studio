import allure
import json
import pytest
import requests
from Skyeye_Studio.Studio.Studio_Api01.test_login import login

BASE_URL = "http://172.25.185.68:1337"
GRAPHQL_ENDPOINT = "http://172.25.185.68:10104/graphql"

class TestWorkspaceManagement:
    jwt_token = None
    workspace_id = None

    @classmethod
    def setup_class(cls):
        cls.jwt_token = login()

    @allure.title("Test Create Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_workspace(self):
        assert self.jwt_token is not None

        create_workspace_payload = {
            "query": """
            mutation {
              create_workspace(
                data: {
                  name: "TestWorkspace04",
                  description: "Skyeye_Telecom",
                  registered_services: ["ElectricPowerPole"]
                },
                org_id: 5
              ) {
                id
                name
                description
                registered_services
              }
            }
            """
        }
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(GRAPHQL_ENDPOINT, json=create_workspace_payload, headers=headers)
        workspace_info = response.json().get("data", {}).get("create_workspace")
        allure.attach(json.dumps(workspace_info), name="Workspace Info - Create", attachment_type=allure.attachment_type.JSON)

        assert workspace_info is not None, "Failed to create workspace"
        assert workspace_info["name"] == "TestWorkspace04", f"Expected name: TestWorkspace04, Actual name: {workspace_info['name']}"
        assert workspace_info["description"] == "Skyeye_Telecom", f"Expected description: Skyeye_Telecom, Actual description: {workspace_info['description']}"
        assert workspace_info["registered_services"] == ["ElectricPowerPole"], f"Expected registered_services: ['ElectricPowerPole'], Actual registered_services: {workspace_info['registered_services']}"

        # Lưu ID của workspace vừa tạo
        self.workspace_id = workspace_info["id"]
        print("\nExpected Result:")
        print(f"Name: TestWorkspace04\nDescription: Skyeye_Telecom\nRegistered Services: ['ElectricPowerPole']")
        print("\nActual Result:")
        print(f"Name: {workspace_info['name']}\nDescription: {workspace_info['description']}\nRegistered Services: {workspace_info['registered_services']}")

    @allure.title("Test Update Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_workspace(self):
        assert self.jwt_token is not None
        assert self.workspace_id is not None  # Kiểm tra workspace_id có giá trị

        # Update workspace
        update_workspace_payload = {
            "query": f"""
            mutation {{
                update_workspace(
                    data: {{
                        name: "Update_TestWorkspace04",
                        description: "Update_Skyeye_Telecom",
                    }},
                    id: {self.workspace_id}
                ) {{
                    id
                    name
                    description
                }}
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(GRAPHQL_ENDPOINT, json=update_workspace_payload, headers=headers)
        updated_workspace_info = response.json().get("data", {}).get("update_workspace")
        allure.attach(json.dumps(updated_workspace_info), name="Updated Workspace Info",
                      attachment_type=allure.attachment_type.JSON)

        # In ra nội dung response
        print(response.text)

        # Kiểm tra và in ra thông tin cập nhật
        assert response.status_code == 200, f"Failed to update workspace. Status code: {response.status_code}"
        assert updated_workspace_info is not None, f"Failed to get updated workspace data in response. Response: {response.json()}"

        print("\nExpected Result (After Update):")
        print(f"Name: Update_TestWorkspace04\nDescription: Update_Skyeye_Telecom")

        print("\nActual Result:")
        print(f"Name: {updated_workspace_info['name']}\nDescription: {updated_workspace_info['description']}")

    @allure.title("Test Delete Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_workspace(self):
        assert self.jwt_token is not None
        assert self.workspace_id is not None  # Kiểm tra workspace_id có giá trị

        # Delete workspace
        delete_workspace_payload = {
            "query": f"""
            mutation {{
                delete_workspace(
                    id: {self.workspace_id}
                )
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {self.jwt_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(GRAPHQL_ENDPOINT, json=delete_workspace_payload, headers=headers)
        allure.attach(json.dumps(response.json()), name="Delete Workspace Response",
                      attachment_type=allure.attachment_type.JSON)

        # Assert the expected and actual results
        assert response.status_code == 200, f"Failed to delete workspace. Status code: {response.status_code}"
        assert response.json().get("data", {}).get("delete_workspace") is True, "Failed to delete workspace"

        # Print or log the results
        print("\nExpected Result (After Delete):")
        print("Workspace deleted successfully")

        print("\nActual Result:")
        print(response.json())


if __name__ == "__main__":
    pytest.main([__file__])
