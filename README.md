# 🧠 CodeMemory - AI Code Review Assistant

> Learn from your Git history. Get personalized code reviews. Track technical debt over time.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- **🎯 Personal Pattern Learning**: Analyzes YOUR commit history to identify recurring mistakes
- **🤖 Context-Aware Reviews**: AI-powered code reviews that understand your codebase
- **📊 Technical Debt Tracking**: Monitor code quality trends over time
- **🎨 Beautiful CLI**: Rich terminal interface with progress tracking
- **🔒 Privacy First**: All analysis runs locally on your machine

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codememory.git
cd codememory

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
Usage
# Initialize in your project
codememory init

# Analyze Git history
codememory analyze

# Analyze with options
codememory analyze --max-commits 500

# Check technical debt
codememory debt
📊 Example Output
🔍 Analyzing Git History...
   ✓ Processed 247 commits
   ✓ Found 3 patterns

🎯 Patterns Found:
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Pattern                         ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Frequent bug fixes detected     │    12 │
│ Debug code frequently committed │     5 │
└─────────────────────────────────┴───────┘
🏗️ Architecture
codememory/
├── codememory/
│   ├── core/          # Core analysis logic
│   ├── cli/           # Command-line interface
│   └── utils/         # Helper utilities
├── tests/             # Test suite
└── docs/              # Documentation
📝 Commands
codememory init - Initialize CodeMemory in a repository
codememory analyze - Analyze Git history and detect patterns
codememory debt - Calculate and display technical debt metrics
🤝 Contributing
Contributions are welcome! Feel free to:
Report bugs
Suggest features
Submit pull requests
📄 License
MIT License - see LICENSE for details.
🙏 Acknowledgments
Built with:
GitPython - Git integration
Rich - Beautiful terminal output
Click - CLI framework
Made with ❤️ for developers, by developers
