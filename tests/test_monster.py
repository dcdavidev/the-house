from unittest.mock import MagicMock
from thehouse.characters.monster import Monster
from thehouse.characters.player import Player

def test_monster_initialization():
    player = Player()
    monster = Monster(player)
    assert monster.player == player
    assert 5 <= monster.health <= 10

def test_monster_str():
    player = Player()
    monster = Monster(player)
    monster.health = 7
    assert str(monster) == "Monster - health: 7"

def test_monster_deal_damage():
    player = MagicMock(spec=Player)
    monster = Monster(player)
    monster.deal_damage()
    player.lose_health.assert_called_once()
    # Damage is 1 or 2
    damage = player.lose_health.call_args[0][0]
    assert damage in [1, 2]
