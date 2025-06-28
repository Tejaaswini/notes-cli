#!/usr/bin/env python3
import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from db import add_note, get_notes_by_period, get_notes_by_tag
from utils import parse_period
import questionary

console = Console()

def show_banner():
    """Display a nice banner when the app starts."""
    ascii_banner = '''
 _   _       _            
| \ | |     | |           
|  \| | ___ | |_ ___  ___ 
| . ` |/ _ \| __/ _ \/ __|
| |\  | (_) | ||  __/\__ \\
\_| \_/\___/ \__\___||___/
                          
                          
'''
    console.print(f"[bold blue]{ascii_banner}[/bold blue]")
    subtitle = Text("review and append notes/todos")
    panel = Panel(
        subtitle,
        border_style="blue",
        padding=(1, 2)
    )
    console.print(panel)

def interactive_menu():
    choice = questionary.select(
        "What do you want to do?",
        choices=[
            "Add TODO",
            "Add Note",
            "View Notes",
            "Other",
            "Exit"
        ]
    ).ask()

    if choice == "Add TODO":
        note = questionary.text("Enter your TODO:").ask()
        add_note(note, "todo")
        console.print("[bold green]TODO added![/bold green]")
    elif choice == "Add Note":
        note = questionary.text("Enter your note:").ask()
        add_note(note)
        console.print("[bold green]Note added![/bold green]")
    elif choice == "View Notes":
        # You can add more submenus or just show all notes
        notes = get_notes_by_period("all")
        if notes:
            table = Table(title="All Notes", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Text", style="white")
            table.add_column("Timestamp", style="green")
            table.add_column("Tag", style="yellow")
            for note in notes:
                tag = note[3] if len(note) > 3 and note[3] else ""
                table.add_row(str(note[0]), note[1], note[2], tag)
            console.print(table)
        else:
            console.print("[bold red] No notes found.[/bold red]")
    elif choice == "Other":
        # Implement other features
        pass
    elif choice == "Exit":
        sys.exit(0)

def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="A CLI tool for adding and reviewing notes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  notes "Buy groceries" --tag todo
  notes "Remember to call mom"
  notes today
  notes todo
  notes "this week"
  notes "all"
        """
    )
    parser.add_argument("input", nargs="*", help="Note text or command")
    parser.add_argument("--tag", help="Tag to attach to the note")
    
    args = parser.parse_args()

    if not args.input:
        interactive_menu()
        return

    command = " ".join(args.input).strip().lower()

    if command in ["today", "yesterday", "this week", "15 days", "a month", "all"]:
        notes = get_notes_by_period(parse_period(command))
        if notes:
            table = Table(title=f"Notes: {command.title()}", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Text", style="white")
            table.add_column("Timestamp", style="green")
            table.add_column("Tag", style="yellow")
            for note in notes:
                tag = note[3] if len(note) > 3 and note[3] else ""
                table.add_row(str(note[0]), note[1], note[2], tag)
            console.print(table)
        else:
            console.print("[bold red] No notes found.[/bold red]")
    elif command == "todo":
        notes = get_notes_by_tag("todo")
        if notes:
            table = Table(title="TODO Notes", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="cyan", no_wrap=True)
            table.add_column("Text", style="white")
            table.add_column("Timestamp", style="green")
            table.add_column("Tag", style="yellow")
            for note in notes:
                tag = note[3] if len(note) > 3 and note[3] else ""
                table.add_row(str(note[0]), note[1], note[2], tag)
            console.print(table)
        else:
            console.print("[bold red] No TODO notes found.[/bold red]")
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
