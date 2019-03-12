import requests
import os
import random

class RedmineProjects(object):
    def __init__(self):
       self.redmine_login = os.environ["hg_redmine"]
       self.redmine_password = os.environ["redmine_pass"]
       self.json_data = {"issue":{"project_id":1, "tracker_id":1, "status_id":1, "priority_id":1, "subject": "Examplepost"}}
       #self.jsoned = {"issue":{"project_id":1, "tracker_id":1}}
       self.hg = os.environ["hg_url"]

    def redmine_get_projects(self):
        return requests.get(self.hg.format("projects.json")).json()

    def redmine_get_issues(self):
        return requests.get(self.hg.format("issues.json")).json()

    def redmine_post(self):
        headers = {'Content-type': 'application/json'}
        return requests.post(url=self.hg.format("issues.json"), data=self.json_data, headers=headers, auth=(self.redmine_login, self.redmine_password))

        


def main():
    RD = RedmineProjects()
    print(RD.redmine_post())
    #print(RD.redmine_get_issues())

if __name__ == '__main__':
    main()
