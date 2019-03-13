import requests
import os
import random
import json
import pprint

class RedmineProjects(object):
    def __init__(self):
       self.redmine_login = os.environ["hg_redmine"]
       self.redmine_password = os.environ["redmine_pass"]
       self.json_data = json.dumps({"issue":{"project_id":1, "tracker_id":1, "status_id":1, "priority_id":1, "subject": "Examplepost"}})
       self.hg = os.environ["hg_url"]
       #self.trello_api_key = os.environ["trello_key"]
       #self.trello_secret = os.environ["trello_secret"]
       #self.trello_token = os.environ["trello_token"]

    def trello_data(self):
        pass

    def redmine_get_projects(self):
        return requests.get(self.hg.format("projects.json")).json()

    def redmine_get_issues(self):
        return requests.get(self.hg.format("issues.json")).json()

    def redmine_get_issue_name(self):
        '''
        Method needed for getting subjects of all current issues in redmine.
        This method is needed in redmine_post method to determine which issues
        are already posted through API to redmine and which still needs posting.
        Input: dictionary of all issues that are listed in redmine
        Output: list of subjects of all issues
        '''
        issues_dict = self.redmine_get_issues()
        subject_list = []
        for issue in issues_dict["issues"]:
            subject_list.append(issue['subject'])
        return subject_list

    def redmine_post(self):
        headers = {'Content-type': 'application/json'}
        trello_issues = self.trello_data
        redmine_issues = self.redmine_get_issue_name()
        for trello_issue in trello_issues:
            if trello_issue not in redmine_issues:
                requests.post(url=self.hg.format("issues.json"), data=trello_issues, headers=headers, auth=(self.redmine_login, self.redmine_password))
                return 201
        


def main():
    RD = RedmineProjects()
    #print(RD.redmine_post())
    print(RD.redmine_get_issues())
    #print(RD.redmine_get_issue_name())
if __name__ == '__main__':
    main()
