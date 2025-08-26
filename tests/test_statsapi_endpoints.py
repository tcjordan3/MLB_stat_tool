"""
MLB Stats API Data Explorer
Explores player_stats, lookup_player, and player_stat_data endpoints
"""

import statsapi
import json
from pprint import pprint

def explore_lookup_player():
    """Explore the lookup_player endpoint"""

    print("=" * 60)
    print("EXPLORING: statsapi.lookup_player()")
    print("=" * 60)
    
    # Let's look up a well-known player
    try:
        # Search for Christian Yelich (Brewers star)
        yelich_data = statsapi.lookup_player("Christian Yelich")
        print(f"Search for 'Christian Yelich':")
        print(f"Type: {type(yelich_data)}")
        print(f"Length: {len(yelich_data)}")
        print("\nFirst result:")
        pprint(yelich_data[0] if yelich_data else "No results found")
        
        # Also try a more common name to see multiple results
        print("\n" + "-" * 40)
        martinez_data = statsapi.lookup_player("Martinez")
        print(f"\nSearch for 'Martinez' (should return multiple players):")
        print(f"Number of results: {len(martinez_data)}")
        print("\nFirst 3 results:")
        for i, player in enumerate(martinez_data[:3]):
            print(f"\nPlayer {i+1}:")
            pprint(player)
            
    except Exception as e:
        print(f"Error in lookup_player: {e}")

def explore_player_stat_data():
    """Explore the player_stat_data endpoint"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.player_stat_data()")
    print("=" * 60)
    
    try:
        # Use Christian Yelich's player ID (592885) - Hitter
        yelich_id = 592885
        
        print("HITTING STATS:")
        print("-" * 20)
        # Get career hitting stats
        career_stats = statsapi.player_stat_data(yelich_id, group="[hitting]", type="career")
        print(f"Career hitting stats for player ID {yelich_id}:")
        print(f"Type: {type(career_stats)}")
        
        # Parse and display key information
        if career_stats:
            # The data comes as a dict, let's explore its structure
            print("\nTop-level keys:")
            print(list(career_stats.keys()))
            
            # Look at the stats structure
            print("\nDetailed structure:")
            pprint(career_stats)
            
        # Also try season stats
        print("\n" + "-" * 40)
        season_stats = statsapi.player_stat_data(yelich_id, group="[hitting]", type="season")
        print(f"\nSeason hitting stats for player ID {yelich_id}:")
        if season_stats:
            print("Season stats structure:")
            pprint(season_stats)
            
    except Exception as e:
        print(f"Error in hitting player_stat_data: {e}")

def explore_pitcher_stats():
    """Explore pitcher statistics specifically"""

    print("\n" + "=" * 60)
    print("EXPLORING: PITCHER STATISTICS")
    print("=" * 60)
    
    try:
        # Use Corbin Burnes' player ID (669203) - Brewers ace pitcher
        burnes_id = 669203
        
        print("PITCHING STATS:")
        print("-" * 20)
        
        # Get career pitching stats
        career_pitching = statsapi.player_stat_data(burnes_id, group="[pitching]", type="career")
        print(f"Career pitching stats for player ID {burnes_id} (Corbin Burnes):")
        print(f"Type: {type(career_pitching)}")
        
        if career_pitching:
            print("\nTop-level keys:")
            print(list(career_pitching.keys()))
            
            print("\nDetailed pitching structure:")
            pprint(career_pitching)
            
        # Get season pitching stats
        print("\n" + "-" * 40)
        season_pitching = statsapi.player_stat_data(burnes_id, group="[pitching]", type="season")
        print(f"\nSeason pitching stats for player ID {burnes_id}:")
        if season_pitching:
            print("Season pitching structure:")
            pprint(season_pitching)
            
        # Try formatted pitching stats as well
        print("\n" + "-" * 40)
        formatted_pitching = statsapi.player_stats(burnes_id, group="pitching", type="career")
        print("Formatted career pitching stats:")
        print(formatted_pitching)
        
    except Exception as e:
        print(f"Error in pitcher stats: {e}")

def explore_defensive_stats():
    """Explore defensive statistics"""

    print("\n" + "=" * 60)
    print("EXPLORING: DEFENSIVE STATISTICS")
    print("=" * 60)
    
    try:
        # Use Christian Yelich for fielding stats
        yelich_id = 592885
        
        print("FIELDING STATS:")
        print("-" * 20)
        
        # Try fielding group
        career_fielding = statsapi.player_stat_data(yelich_id, group="[fielding]", type="career")
        print(f"Career fielding stats for player ID {yelich_id}:")
        print(f"Type: {type(career_fielding)}")
        
        if career_fielding:
            print("\nTop-level keys:")
            print(list(career_fielding.keys()))
            
            print("\nDetailed fielding structure:")
            pprint(career_fielding)
            
        # Get season fielding stats
        print("\n" + "-" * 40)
        season_fielding = statsapi.player_stat_data(yelich_id, group="[fielding]", type="season")
        print(f"\nSeason fielding stats for player ID {yelich_id}:")
        if season_fielding:
            print("Season fielding structure:")
            pprint(season_fielding)
        
        # Try formatted fielding stats
        print("\n" + "-" * 40)
        formatted_fielding = statsapi.player_stats(yelich_id, group="fielding", type="career")
        print("Formatted career fielding stats:")
        print(formatted_fielding)
        
        # Also try with a known good defender (maybe a shortstop or catcher)
        print("\n" + "=" * 40)
        print("ADDITIONAL FIELDING EXAMPLE:")
        print("=" * 40)
        
        # Let's try Willy Adames (Brewers shortstop) - player ID 642715
        adames_id = 642715
        adames_fielding = statsapi.player_stat_data(adames_id, group="[fielding]", type="season")
        print(f"Season fielding stats for player ID {adames_id} (Willy Adames - SS):")
        if adames_fielding:
            pprint(adames_fielding)
        
    except Exception as e:
        print(f"Error in defensive stats: {e}")

def explore_stat_groups():
    """Explore what stat groups are available"""

    print("\n" + "=" * 60)
    print("EXPLORING: AVAILABLE STAT GROUPS")
    print("=" * 60)
    
    print("Testing different group parameters to see what's available:")
    
    yelich_id = 592885
    burnes_id = 669203
    
    groups_to_try = [
        "hitting", "[hitting]",
        "pitching", "[pitching]", 
        "fielding", "[fielding]",
        "catching", "[catching]",
        "baserunning", "[baserunning]"
    ]
    
    for group in groups_to_try:
        try:
            print(f"\nTrying group='{group}' with Yelich:")
            result = statsapi.player_stat_data(yelich_id, group=group, type="season")
            if result:
                print(f"  ✓ Success - Type: {type(result)}")
                if isinstance(result, dict):
                    print(f"  Keys: {list(result.keys())}")
            else:
                print("  ✗ No data returned")
                
        except Exception as e:
            print(f"  ✗ Error: {e}")

def explore_player_stats():
    """Explore the player_stats endpoint (formatted text version)"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.player_stats() - Formatted Text Version")
    print("=" * 60)
    
    try:
        # Use Christian Yelich's player ID
        yelich_id = 592885
        
        # Get formatted career stats
        formatted_career = statsapi.player_stats(yelich_id, group="hitting", type="career")
        print("Formatted career stats:")
        print(formatted_career)
        
        print("\n" + "-" * 40)
        
        # Get formatted season stats
        formatted_season = statsapi.player_stats(yelich_id, group="hitting", type="season")
        print("Formatted season stats:")
        print(formatted_season)
        
    except Exception as e:
        print(f"Error in player_stats: {e}")

def explore_league_leaders():
    """Explore the league_leaders endpoint"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.league_leaders()")
    print("=" * 60)
    
    try:
        # Get current season batting average leaders
        ba_leaders = statsapi.league_leaders(leaderCategories="battingAverage", season=2024)
        print("Batting Average Leaders (2024):")
        print(f"Type: {type(ba_leaders)}")
        print("Sample output:")
        print(ba_leaders[:500] + "..." if len(ba_leaders) > 500 else ba_leaders)
        
        print("\n" + "-" * 40)
        
        # Get home run leaders
        hr_leaders = statsapi.league_leaders(leaderCategories="homeRuns", season=2024)
        print("Home Run Leaders (2024):")
        print("Sample output:")
        print(hr_leaders[:500] + "..." if len(hr_leaders) > 500 else hr_leaders)
        
    except Exception as e:
        print(f"Error in league_leaders: {e}")

def explore_roster():
    """Explore the roster endpoint"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.roster()")
    print("=" * 60)
    
    try:
        # Get Milwaukee Brewers roster (team ID 158)
        brewers_roster = statsapi.roster(158)
        print("Milwaukee Brewers Roster:")
        print(f"Type: {type(brewers_roster)}")
        print("Sample output:")
        print(brewers_roster[:1000] + "..." if len(brewers_roster) > 1000 else brewers_roster)
        
        print("\n" + "-" * 40)
        
        # Try getting roster data (structured format)
        try:
            from datetime import date
            brewers_roster_data = statsapi.roster_data(158)
            print("Milwaukee Brewers Roster Data (structured):")
            print(f"Type: {type(brewers_roster_data)}")
            if isinstance(brewers_roster_data, dict):
                print("Top-level keys:")
                print(list(brewers_roster_data.keys()))
                print("\nDetailed structure (first few items):")
                pprint(brewers_roster_data)
            else:
                print("Raw data:")
                pprint(brewers_roster_data)
        except AttributeError:
            print("roster_data method not available, using roster only")
        
    except Exception as e:
        print(f"Error in roster: {e}")

def explore_standings():
    """Explore the standings endpoint"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.standings()")
    print("=" * 60)
    
    try:
        # Get current standings
        current_standings = statsapi.standings()
        print("Current MLB Standings:")
        print(f"Type: {type(current_standings)}")
        print("Sample output:")
        print(current_standings[:1000] + "..." if len(current_standings) > 1000 else current_standings)
        
        print("\n" + "-" * 40)
        
        # Try standings data (structured)
        try:
            standings_data = statsapi.standings_data()
            print("Standings Data (structured):")
            print(f"Type: {type(standings_data)}")
            if isinstance(standings_data, dict):
                print("Top-level keys:")
                print(list(standings_data.keys()))
                print("\nDetailed structure:")
                pprint(standings_data)
        except AttributeError:
            print("standings_data method not available, using standings only")
        
    except Exception as e:
        print(f"Error in standings: {e}")

def explore_team_leaders():
    """Explore the team_leaders endpoint"""

    print("\n" + "=" * 60)
    print("EXPLORING: statsapi.team_leaders()")
    print("=" * 60)
    
    try:
        # Get Milwaukee Brewers team leaders
        brewers_leaders = statsapi.team_leaders(158)
        print("Milwaukee Brewers Team Leaders:")
        print(f"Type: {type(brewers_leaders)}")
        print("Sample output:")
        print(brewers_leaders[:1000] + "..." if len(brewers_leaders) > 1000 else brewers_leaders)
        
        print("\n" + "-" * 40)
        
        # Try team leader data (structured)
        try:
            brewers_leaders_data = statsapi.team_leader_data(158)
            print("Milwaukee Brewers Team Leaders Data (structured):")
            print(f"Type: {type(brewers_leaders_data)}")
            if isinstance(brewers_leaders_data, dict):
                print("Top-level keys:")
                print(list(brewers_leaders_data.keys()))
                print("\nDetailed structure:")
                pprint(brewers_leaders_data)
        except AttributeError:
            print("team_leader_data method not available, using team_leaders only")
        
    except Exception as e:
        print(f"Error in team_leaders: {e}")

def main():
    """Run all exploration functions"""

    print("MLB Stats API Data Exploration")
    
    try:
        # Test if the API is working
        print("Testing API connectivity...")
        test_data = statsapi.lookup_player("test")
        print("✓ API connection successful!\n")
        
        # Run explorations
        explore_lookup_player()
        explore_player_stat_data() 
        explore_pitcher_stats()
        explore_defensive_stats()
        explore_stat_groups()
        explore_player_stats()
        explore_league_leaders()
        explore_roster()
        explore_standings()
        explore_team_leaders()
        
        print("\n" + "=" * 60)
        print("EXPLORATION COMPLETE")
        print("=" * 60)
        print("Key takeaways for your schema:")
        print("1. lookup_player() returns a list of player dictionaries")
        print("2. player_stat_data() returns structured data (dict)")
        print("3. Available stat groups: [hitting], [pitching], [fielding], possibly others")
        print("4. Pitching stats: ERA, WHIP, wins/losses should be available")
        print("5. Defensive stats: fielding percentage, errors, assists available")
        print("6. For database schema, focus on *_data() methods for structured data")
        print("7. league_leaders, roster, standings, team_leaders show team/league context")
        print("8. Team ID 158 = Milwaukee Brewers")
        print("9. Player IDs: Yelich=592885, Burnes=669203, Adames=642715")
        print("12. Trade realism factors: MLB stats + contract data should be sufficient to start")
        
    except ImportError:
        print("Error: MLB-StatsAPI package not installed!")
        print("Please install with: pip install MLB-StatsAPI")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()