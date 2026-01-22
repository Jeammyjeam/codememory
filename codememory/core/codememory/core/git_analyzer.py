"""Git repository analyzer"""
from typing import List, Dict
from datetime import datetime
import git

class GitAnalyzer:
    """Analyzes Git repository history"""
    
    def __init__(self, repo_path: str = '.'):
        try:
            self.repo = git.Repo(repo_path, search_parent_directories=True)
        except git.InvalidGitRepositoryError:
            raise ValueError(f"Not a Git repository: {repo_path}")
    
    def get_commits(self, since=None, until=None, branch=None, max_count=1000):
        """Get commits from repository"""
        commits = []
        kwargs = {'max_count': max_count}
        if since:
            kwargs['since'] = since
        if until:
            kwargs['until'] = until
        if branch:
            kwargs['rev'] = branch
        
        for commit in self.repo.iter_commits(**kwargs):
            commits.append({
                'sha': commit.hexsha,
                'message': commit.message.strip(),
                'author': str(commit.author),
                'date': datetime.fromtimestamp(commit.committed_date),
            })
        return commits
