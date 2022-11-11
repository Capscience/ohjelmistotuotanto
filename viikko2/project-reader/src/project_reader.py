from urllib import request
from toml import loads
from project import Project


class ProjectReader:
    """Read data from url to a Project."""
    def __init__(self, url):
        self._url = url

    def get_project(self):
        """Get and parse data from url."""
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = loads(content)
        project = Project(
            parsed['tool']['poetry']['name'],
            parsed['tool']['poetry']['description'],
            parsed['tool']['poetry']['dependencies'],
            parsed['tool']['poetry']['dev-dependencies']
        )

        return project
