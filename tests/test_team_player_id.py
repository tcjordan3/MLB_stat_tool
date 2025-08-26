import statsapi

# MLB = 1, MiLB = 11
SPORT_IDS = [1, 11]

def get_teams_and_players():
    for sport_id in SPORT_IDS:
        print(f"\n=== Teams for sportId={sport_id} ===\n")
        teams = statsapi.get("teams", {"sportId": sport_id})
        
        for team in teams.get("teams", []):
            team_id = team["id"]
            team_name = team["name"]
            print(f"TEAM: {team_id} - {team_name}")

            # Fetch roster (active players only)
            try:
                roster = statsapi.get("team_roster", {"teamId": team_id, "rosterType": "active"})
                for player in roster.get("roster", []):
                    player_id = player["person"]["id"]
                    player_name = player["person"]["fullName"]
                    print(f"   PLAYER: {player_id} - {player_name}")
            except Exception as e:
                print(f"   Could not fetch roster for {team_name}: {e}")

if __name__ == "__main__":
    get_teams_and_players()
