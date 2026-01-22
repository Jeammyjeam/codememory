"""CLI commands for CodeMemory"""
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from pathlib import Path
from codememory.core.git_analyzer import GitAnalyzer
from codememory.core.pattern_learner import PatternLearner
from codememory.core.debt_tracker import DebtTracker
from codememory.utils.config import Config

console = Console()

@click.group()
def cli():
    """🧠 CodeMemory - AI Code Review Assistant"""
    pass

@cli.command()
@click.option('--path', default='.')
def init(path):
    """Initialize CodeMemory in a repository"""
    console.print(Panel.fit("[cyan]🧠 Initializing CodeMemory[/cyan]"))
    
    repo_path = Path(path).resolve()
    
    if not (repo_path / '.git').exists():
        console.print("[red]❌ Not a Git repository![/red]")
        console.print("💡 Run: [cyan]git init[/cyan] first")
        return
    
    config_dir = repo_path / '.codememory'
    config_dir.mkdir(exist_ok=True)
    
    config = Config()
    config.save(config_dir / 'config.yaml')
    
    console.print(f"✅ Initialized in [cyan]{repo_path}[/cyan]")
    console.print("\n📝 Next steps:")
    console.print("  [cyan]codememory analyze[/cyan] - Analyze Git history")
    console.print("  [cyan]codememory debt[/cyan] - Check technical debt")

@cli.command()
@click.option('--path', default='.')
@click.option('--max-commits', default=100)
def analyze(path, max_commits):
    """Analyze Git history and learn patterns"""
    console.print(Panel.fit("[cyan]🔍 Analyzing Git History[/cyan]"))
    
    try:
        analyzer = GitAnalyzer(path)
        learner = PatternLearner()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("📚 Reading commits...", total=None)
            commits = analyzer.get_commits(max_count=max_commits)
            progress.update(task, completed=True)
            
            task = progress.add_task(f"🧠 Analyzing {len(commits)} commits...", total=None)
            patterns = learner.extract_patterns(commits)
            progress.update(task, completed=True)
        
        console.print(f"\n✅ Analysis complete!")
        console.print(f"   • Processed [cyan]{len(commits)}[/cyan] commits")
        console.print(f"   • Found [cyan]{len(patterns)}[/cyan] patterns")
        
        if patterns:
            console.print("\n[bold]🎯 Patterns Found:[/bold]")
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("Pattern", style="yellow")
            table.add_column("Count", justify="right")
            
            for p in patterns:
                table.add_row(p['description'], str(p['count']))
            
            console.print(table)
        else:
            console.print("\n[green]✅ No problematic patterns found![/green]")
            
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

@cli.command()
@click.option('--path', default='.')
def debt(path):
    """Track technical debt"""
    console.print(Panel.fit("[cyan]📊 Technical Debt Analysis[/cyan]"))
    
    try:
        tracker = DebtTracker(path)
        metrics = tracker.calculate_debt()
        
        console.print(f"\n[bold]Debt Score: [cyan]{metrics['score']:.2f}[/cyan][/bold]")
        
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Category")
        table.add_column("Issues", justify="right")
        table.add_column("Severity")
        
        for cat, data in metrics['categories'].items():
            color = 'red' if data['severity'] == 'high' else 'yellow' if data['severity'] == 'medium' else 'green'
            table.add_row(cat, str(data['count']), f"[{color}]{data['severity']}[/{color}]")
        
        console.print(table)
        
    except Exception as e:
        console.print(f"[red]❌ Error: {e}[/red]")

if __name__ == '__main__':
    cli()
