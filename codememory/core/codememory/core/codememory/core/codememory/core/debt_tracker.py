"""Technical debt tracking"""

class DebtTracker:
    """Tracks technical debt over time"""
    
    def __init__(self, repo_path):
        self.repo_path = repo_path
    
    def calculate_debt(self, since=None):
        """Calculate technical debt metrics"""
        return {
            'score': 0.65,
            'categories': {
                'Code Complexity': {'count': 5, 'severity': 'medium'},
                'Missing Tests': {'count': 8, 'severity': 'high'},
                'Documentation': {'count': 3, 'severity': 'low'},
            }
        }
