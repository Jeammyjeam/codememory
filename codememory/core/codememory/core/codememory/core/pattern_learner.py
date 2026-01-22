"""Pattern learning from Git history"""

class PatternLearner:
    """Learns patterns from commit history"""
    
    def extract_patterns(self, commits):
        """Extract patterns from commits"""
        patterns = []
        messages = [c['message'].lower() for c in commits]
        
        # Detect frequent bug fixes
        fixes = [m for m in messages if 'fix' in m or 'bug' in m]
        if len(fixes) > 3:
            patterns.append({
                'description': 'Frequent bug fixes detected',
                'count': len(fixes),
                'resolved': False
            })
        
        # Detect debug code commits
        debug = [m for m in messages if 'debug' in m or 'console' in m]
        if len(debug) > 2:
            patterns.append({
                'description': 'Debug code frequently committed',
                'count': len(debug),
                'resolved': False
            })
        
        return patterns
    
    def save_patterns(self, patterns):
        """Save patterns to database"""
        pass
