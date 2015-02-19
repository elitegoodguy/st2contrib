from lib.base import BaseJiraAction

__all__ = [
    'GetJiraIssueAction'
]


class GetJiraIssueAction(BaseJiraAction):
    def run(self, issue_key):
        issue = self._client.issue(issue_key)

        split = issue.permalink().split(' - ', 1)
        url = split[0]

        if issue.fields.resolution:
            resolution = issue.fields.resolution.name
        else:
            resolution = None

        if issue.fields.reporter:
            reporter = issue.fields.reporter.displayName
        else:
            reporter = None

        if issue.fields.assignee:
            assignee = issue.fields.assignee.displayName
        else:
            assignee = None

        result = {
            'id': issue.id,
            'key': issue_key,
            'url': url,
            'summary': issue.fields.summary,
            'description': issue.fields.description,
            'status': issue.fields.status.name,
            'resolution': resolution,
            'labels': issue.fields.labels,
            'reporter': reporter,
            'assignee': assignee,
            'created_at': issue.fields.created,
            'updated_at': issue.fields.updated,
            'resolved_at': issue.fields.resolutiondate
        }
        return result
