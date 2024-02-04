# crud_workspace.py

import allure
from Skyeye_Studio.Studio.Studio_Api01.test_login import login
import json
import pytest
import requests

BASE_URL = "http://172.25.185.68:1337"
GRAPHQL_ENDPOINT = "http://172.25.185.68:10104/graphql"
workspace_id = None
jwt_token = None
class TestWorkspaceManagement01:

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
              name:"TestWorkspace04", 
              description:"Skyeye_Telecom", 
              registered_services: ["ElectricPowerPole"]
              },
            org_id: 5
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

        # Assert the expected and actual results
        assert workspace_info is not None, "Failed to create workspace"
        assert workspace_info[
                   "name"] == "TestWorkspace04", f"Expected name: TestWorkspace04, Actual name: {workspace_info['name']}"
        assert workspace_info[
                   "description"] == "Skyeye_Telecom", f"Expected description: Skyeye_Telecom, Actual description: {workspace_info['description']}"
        assert workspace_info["registered_services"] == [
            "ElectricPowerPole"], f"Expected registered_services: ['ElectricPowerPole'], Actual registered_services: {workspace_info['registered_services']}"

        # Lưu ID của workspace vừa tạo
        workspace_id = workspace_info["id"]

        # Print or log the results
        print("Expected Result:")
        print(f"Name: TestWorkspace04\nDescription: Skyeye_Telecom\nRegistered Services: ['ElectricPowerPole']")
        print("\nActual Result:")
        print(
            f"Name: {workspace_info['name']}\nDescription: {workspace_info['description']}\nRegistered Services: {workspace_info['registered_services']}")
    @allure.title("Test Update Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_workspace(self):
        global workspace_id
        assert jwt_token is not None

        # Update workspace
        update_workspace_payload = {
            "query": f"""
            mutation {{
                update_workspace(
                    data: {{
                        name: "Update_TestWorkspace04",
                        description: "Update_Skyeye_Telecom",
                        registered_services: ["ElectricPowerPole"]
                    }},
                    id: {workspace_id}
                ) {{
                    id
                    name
                    description
                    registered_services
                }}
            }}
            """
        }
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        update_workspace_response = requests.post(GRAPHQL_ENDPOINT, json=update_workspace_payload, headers=headers)
        update_workspace_data = update_workspace_response.json()
        updated_workspace_info = update_workspace_data.get("data", {}).get("update_workspace")
        allure.attach(json.dumps(updated_workspace_info), name="Updated Workspace Info",
                      attachment_type=allure.attachment_type.JSON)

        # Assert the expected and actual results
        # Assert the expected and actual results
        # Assert the expected and actual results
        assert updated_workspace_info is not None, "Failed to update workspace"
        assert updated_workspace_info[
                   "name"] == "Update_TestWorkspace04", f"Expected name: Update_TestWorkspace04, Actual name: {updated_workspace_info['name']}"
        assert updated_workspace_info[
                   "description"] == "Update_Skyeye_Telecom", f"Expected description: Update_Skyeye_Telecom, Actual description: {updated_workspace_info['description']}"
        assert updated_workspace_info["registered_services"] == [
            "ElectricPowerPole"], f"Expected registered_services: ['ElectricPowerPole'], Actual registered_services: {updated_workspace_info['registered_services']}"

        # Print or log the results
        print("\nExpected Result (After Update):")
        print(
            f"Name: Update_TestWorkspace04\nDescription: Update_Skyeye_Telecom\nRegistered Services: ['ElectricPowerPole']")

        print("\nActual Result:")
        print(
            f"Name: {updated_workspace_info['name']}\nDescription: {updated_workspace_info['description']}\nRegistered Services: {updated_workspace_info['registered_services']}")

    @allure.title("Test Delete Workspace")
    @pytest.mark.Skyeye_Telecom
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_workspace(self):
        global workspace_id
        assert jwt_token is not None
        assert workspace_id is not None

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
        headers = {
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        }
        delete_workspace_response = requests.post(GRAPHQL_ENDPOINT, json=delete_workspace_payload, headers=headers)
        delete_workspace_data = delete_workspace_response.json()
        allure.attach(json.dumps(delete_workspace_data), name="Delete Workspace Response",
                      attachment_type=allure.attachment_type.JSON)

        # Assert the expected and actual results
        assert delete_workspace_data.get("data", {}).get("delete_workspace") is True, "Failed to delete workspace"

        # Print or log the results
        print("\nExpected Result (After Delete):")
        print("Workspace deleted successfully")

        print("\nActual Result:")
        print(delete_workspace_data)

    # Thêm các hàm kiểm thử khác nếu cần

if __name__ == "__main__":
    pytest.main([__file__])
