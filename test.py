import json
traj_file = ".\questionsInput.json"
camera_trajectory = json.load(open(traj_file))
print(camera_trajectory["questionsList"][1]["category"])
