import json

directory = 'blackjack/stats.json'

def get_stats():
    with open(directory, 'r') as file:
        stats = json.load(file)
    return stats

def get_average_win_rate():
    stats = get_stats()
    total_games = stats['wins'] + stats['losses']
    if total_games == 0:
        return 0
    return stats['wins'] / total_games

def update_stats(won):
    with open(directory, 'r') as file:
        stats = json.load(file)
    if won:
        stats['wins'] += 1
    else:
        stats['losses'] += 1
    with open(directory, 'w') as file:
        json.dump(stats, file, indent=4)

def print_stats():
    stats = get_stats()
    print(f"Wins: {stats['wins']}\nLosses: {stats['losses']}")
    
def get_money():
    stats = get_stats()
    return stats['money']

def update_money(won, money):
    with open(directory, 'r') as file:
        stats = json.load(file)
        if won:
            stats["money"] += money
        else: 
            stats["money"] -= money
        with open(directory, 'w') as file:
            json.dump(stats, file, indent=4)
    