"""Configuration management"""
import yaml

class Config:
    """Manages CodeMemory configuration"""
    
    def __init__(self):
        self.data = {
            'max_commits': 1000,
            'min_patterns': 3,
            'ai_provider': 'openai'
        }
    
    def save(self, path):
        """Save configuration to file"""
        with open(path, 'w') as f:
            yaml.dump(self.data, f)
