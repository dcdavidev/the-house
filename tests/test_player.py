from unittest.mock import patch
from thehouse.characters.player import Player

def test_player_initialization():
    player = Player()
    assert player.escaped is False
    assert player.items == []
    assert 5 <= player.health <= 10

def test_player_str():
    player = Player()
    player.health = 5
    player.escaped = False
    assert str(player) == "Player - health: 5; escaped False"

def test_player_escape():
    player = Player()
    player.escape_the_house()
    assert player.escaped is True

@patch("thehouse.characters.player.print_pause")
def test_player_pick_item(mock_print):
    player = Player()
    player.pick_an_item("Key")
    assert "Key" in player.items
    assert "Key" in player
    mock_print.assert_called_with("You pick Key!")

@patch("thehouse.characters.player.print_pause")
def test_player_print_items_empty(mock_print):
    player = Player()
    player.print_items()
    mock_print.assert_called_with("Your pockets are empty!")

@patch("thehouse.characters.player.print_pause")
def test_player_print_items(mock_print):
    player = Player()
    player.items = ["Key", "Sword"]
    player.print_items()
    assert mock_print.call_count == 2
    mock_print.assert_any_call("- Key")
    mock_print.assert_any_call("- Sword")
