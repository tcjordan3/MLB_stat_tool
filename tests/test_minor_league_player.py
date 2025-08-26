#!/usr/bin/env python3
"""
Minor League Player Stats Test
Testing Bradley Hanner (ID: 690440) from Columbus Clippers (Team: 445)
"""

import statsapi
from pprint import pprint

def test_bradley_hanner():
    """Test fetching stats for Bradley Hanner - minor league player"""
    print("=" * 70)
    print("TESTING: BRADLEY HANNER (Minor League Player)")
    print("Player ID: 690440")
    print("Team: Columbus Clippers (445)")
    print("=" * 70)
    
    player_id = 690440
    player_name = "Bradley Hanner"
    
    # Test 1: Basic lookup to confirm player exists
    print("\n1. BASIC PLAYER LOOKUP:")
    print("-" * 30)
    try:
        lookup_results = statsapi.lookup_player("Bradley Hanner")
        print(f"Lookup results for '{player_name}':")
        print(f"Number of results: {len(lookup_results)}")
        
        for i, player in enumerate(lookup_results):
            print(f"\nResult {i+1}:")
            pprint(player)
            
            # Check if this matches our known ID
            if player.get('id') == player_id:
                print("✅ MATCH FOUND - This is our player!")
                
    except Exception as e:
        print(f"❌ Lookup error: {e}")
    
    # Test 2: Direct player stat data using known ID
    print(f"\n\n2. DIRECT STAT DATA FETCH (ID: {player_id}):")
    print("-" * 50)
    
    stat_groups = ['hitting', 'pitching', 'fielding']
    stat_types = ['career', 'season']
    
    for group in stat_groups:
        print(f"\n--- {group.upper()} STATS ---")
        
        for stat_type in stat_types:
            try:
                stats = statsapi.player_stat_data(player_id, group=f"[{group}]", type=stat_type)
                
                if stats:
                    print(f"✅ {stat_type.upper()} {group} stats found:")
                    print(f"Data type: {type(stats)}")
                    if isinstance(stats, dict):
                        print(f"Keys: {list(stats.keys())}")
                    print("Full data structure:")
                    pprint(stats)
                else:
                    print(f"❌ No {stat_type} {group} stats found")
                    
            except Exception as e:
                print(f"❌ Error fetching {stat_type} {group} stats: {e}")
    
    # Test 3: Formatted stats (text version)
    print(f"\n\n3. FORMATTED STATS (ID: {player_id}):")
    print("-" * 40)
    
    for group in stat_groups:
        for stat_type in stat_types:
            try:
                formatted_stats = statsapi.player_stats(player_id, group=group, type=stat_type)
                
                if formatted_stats:
                    print(f"\n✅ FORMATTED {stat_type.upper()} {group.upper()} STATS:")
                    print(formatted_stats)
                else:
                    print(f"❌ No formatted {stat_type} {group} stats")
                    
            except Exception as e:
                print(f"❌ Error getting formatted {stat_type} {group} stats: {e}")

def test_columbus_clippers_team():
    """Test the Columbus Clippers team data"""
    print("\n" + "=" * 70)
    print("TESTING: COLUMBUS CLIPPERS TEAM DATA")
    print("Team ID: 445")
    print("=" * 70)
    
    team_id = 445
    
    # Test 1: Team roster
    print("\n1. TEAM ROSTER:")
    print("-" * 20)
    try:
        roster = statsapi.roster(team_id)
        
        if roster:
            print(f"✅ Roster found - {len(roster)} characters")
            print(f"Sample roster data:\n{roster[:500]}...")
            
            # Check if Bradley Hanner is in the roster
            if "hanner" in roster.lower() or "bradley" in roster.lower():
                print("🎯 Bradley Hanner found in roster!")
            else:
                print("❓ Bradley Hanner not found in roster text")
                
        else:
            print("❌ No roster data found")
            
    except Exception as e:
        print(f"❌ Roster error: {e}")
    
    # Test 2: Team standings
    print("\n2. TEAM STANDINGS:")
    print("-" * 20)
    try:
        standings = statsapi.standings(teamId=team_id)
        
        if standings:
            print(f"✅ Standings found - {len(standings)} characters")
            print(f"Sample standings:\n{standings[:300]}...")
        else:
            print("❌ No standings data found")
            
    except Exception as e:
        print(f"❌ Standings error: {e}")
    
    # Test 3: Team leaders
    print("\n3. TEAM LEADERS:")
    print("-" * 20)
    try:
        team_leaders = statsapi.team_leaders(team_id)
        
        if team_leaders:
            print(f"✅ Team leaders found - {len(team_leaders)} characters")
            print(f"Sample team leaders:\n{team_leaders[:400]}...")
        else:
            print("❌ No team leaders data found")
            
    except Exception as e:
        print(f"❌ Team leaders error: {e}")

def test_alternative_approaches():
    """Test alternative ways to get minor league player data"""
    print("\n" + "=" * 70)
    print("TESTING: ALTERNATIVE APPROACHES")
    print("=" * 70)
    
    player_id = 690440
    team_id = 445
    
    print("\n1. TESTING DIFFERENT GROUP FORMATS:")
    print("-" * 40)
    
    # Try different group parameter formats
    group_formats = [
        "hitting", "[hitting]", "Hitting",
        "pitching", "[pitching]", "Pitching", 
        "fielding", "[fielding]", "Fielding",
        "catching", "[catching]",
        "baserunning", "[baserunning]"
    ]
    
    for group_format in group_formats:
        try:
            result = statsapi.player_stat_data(player_id, group=group_format, type="career")
            if result:
                print(f"✅ '{group_format}' format works!")
                print(f"   Data type: {type(result)}")
                if isinstance(result, dict) and len(result) > 0:
                    print(f"   Keys: {list(result.keys())[:5]}...")  # First 5 keys
            else:
                print(f"❌ '{group_format}' - no data")
        except Exception as e:
            print(f"❌ '{group_format}' - error: {str(e)[:50]}...")
    
    print("\n2. TESTING DIFFERENT TYPE PARAMETERS:")
    print("-" * 40)
    
    type_formats = ["career", "season", "gameLog", "vsTeam", "vsPlayer"]
    
    for type_format in type_formats:
        try:
            result = statsapi.player_stat_data(player_id, group="[hitting]", type=type_format)
            if result:
                print(f"✅ type='{type_format}' works!")
                print(f"   Data type: {type(result)}")
            else:
                print(f"❌ type='{type_format}' - no data")
        except Exception as e:
            print(f"❌ type='{type_format}' - error: {str(e)[:50]}...")

def main():
    """Run all tests for Bradley Hanner and Columbus Clippers"""
    print("MINOR LEAGUE PLAYER STATS TEST")
    print("Testing Bradley Hanner (690440) from Columbus Clippers (445)")
    print("\nMake sure you have: pip install MLB-StatsAPI\n")
    
    try:
        test_bradley_hanner()
        test_columbus_clippers_team()
        test_alternative_approaches()
        
        print("\n" + "=" * 70)
        print("TEST RESULTS SUMMARY")
        print("=" * 70)
        print("This test will show us:")
        print("1. ✅ Whether minor league player stats are accessible")
        print("2. ✅ What data fields are available for MiLB players") 
        print("3. ✅ How minor league team data works")
        print("4. ✅ The best API parameters for MiLB data")
        print("5. ✅ Data structure for your database schema")
        print("\nIf successful, this proves prospects can be included in your trade engine!")
        
    except ImportError:
        print("Error: MLB-StatsAPI package not installed!")
        print("Please install with: pip install MLB-StatsAPI")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()