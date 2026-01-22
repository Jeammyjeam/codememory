"""Main entry point for CodeMemory CLI"""
import sys
from codememory.cli.commands import cli

def main():
    try:
        cli()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
