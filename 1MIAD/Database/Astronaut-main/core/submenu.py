import core.Assets.rich as rich

def Confirm_Menu(text):
        rich.console.print(f'[yellow]{text}[/]')
        Choice=input().upper()
        if Choice in['YES','Y']:
            return True
        elif Choice in['NO','N']:
            return False
        elif Choice=='CANCEL':
            return None