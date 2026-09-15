from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_removes_student_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 200
    assert email not in response.json()["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    # restore state for subsequent tests / local stability
    from src.app import activities

    activities[activity_name]["participants"].append(email)
