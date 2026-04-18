import os
import matplotlib.pyplot as plt

def plot_top_batters(top_batters):
    os.makedirs('outputs', exist_ok=True)
    top_batters.plot(kind='bar', color='royalblue')
    plt.title('Top 10 Run Scorers')
    plt.xlabel('Batter')
    plt.ylabel('Total Runs')
    plt.tight_layout()
    plt.savefig('outputs/top_batters.png')
    plt.show()

def plot_top_bowlers(top_bowlers):
    top_bowlers.plot(kind='bar', color='green')
    plt.title('Top 10 Wicket Takers')
    plt.xlabel('Bowler')
    plt.ylabel('Wickets')
    plt.tight_layout()
    plt.savefig('outputs/top_bowlers.png')
    plt.show()

def plot_team_wins(wins):
    wins.head(10).plot(kind='bar', color='orange')
    plt.title('Most Wins by Team')
    plt.xlabel('Team')
    plt.ylabel('Wins')
    plt.tight_layout()
    plt.savefig('outputs/team_wins.png')
    plt.show()
