import unittest
from unittest.mock import MagicMock, patch

from behavior.basicbehavior.fishing import Fishing
# 필요에 따라 import 수정
from behavior.sub_facility.canoe import Canoe


class TestCanoe(unittest.TestCase):

    def setUp(self):
        self.input_behavior = MagicMock(spec=Fishing)
        self.canoe = Canoe(self.input_behavior)

    @patch('repository.game_status_repository.game_status_repository.game_status')
    @patch('repository.player_status_repository.player_status_repository.player_status')
    def test_canUse(self, mock_player_status, mock_game_status):
        # Mock the current player and their cards
        mock_game_status.now_turn_player = 1
        mock_player_status[1].card.put_sub_card = [self.canoe]

        # Test when input_behavior is Fishing and Canoe card is present
        self.assertTrue(self.canoe.canUse())

        # Test when input_behavior is not Fishing
        self.canoe.input_behavior = MagicMock()
        self.assertFalse(self.canoe.canUse())

        # Test when Canoe card is not present
        mock_player_status[1].card.putSubCard = []
        self.assertFalse(self.canoe.canUse())

    @patch('repository.game_status_repository.game_status_repository.game_status')
    @patch('repository.player_status_repository.player_status_repository.player_status')
    def test_execute(self, mock_player_status, mock_game_status):
        # Mock the current player and their resources
        mock_game_status.now_turn_player = 1
        current_player = mock_player_status[1]
        current_player.resource.food = 0
        current_player.resource.reed = 0

        # Mock the resource methods
        current_player.resource.set_food = MagicMock()
        current_player.resource.set_reed = MagicMock()

        # Execute the method
        self.assertTrue(self.canoe.execute())

        # Verify the resources were updated
        current_player.resource.set_food.assert_called_with(1)
        current_player.resource.set_reed.assert_called_with(1)

    def test_log(self):
        # Test log method
        self.canoe.log_text = "Test log message"
        self.assertEqual(self.canoe.log(), "Test log message")

    @patch('repository.game_status_repository.game_status_repository.game_status')
    @patch('repository.player_status_repository.player_status_repository.player_status')
    def test_putDown(self, mock_player_status, mock_game_status):
        # Mock the current player and their resources/cards
        mock_game_status.now_turn_player = 1
        current_player = mock_player_status[mock_game_status.now_turn_player]
        current_player.resource.wood = 3
        current_player.card.hand_sub_card = [self.canoe]
        current_player.card.put_sub_card = []

        # Mock the resource method
        current_player.resource.set_wood = MagicMock()

        # Put down the card
        self.assertTrue(self.canoe.putDown())

        # Verify the card was moved and resources updated
        self.assertNotIn(self.canoe, current_player.card.hand_sub_card)
        self.assertIn(self.canoe, current_player.card.put_sub_card)
        current_player.resource.set_wood.assert_called_with(1)

    @patch('repository.game_status_repository.game_status_repository.game_status')
    @patch('repository.player_status_repository.player_status_repository.player_status')
    def test_canPutDown(self, mock_player_status, mock_game_status):
        # Mock the current player and their resources/cards
        mock_game_status.now_turn_player = 1
        current_player = mock_player_status[1]
        current_player.resource.wood = 3
        current_player.card.put_job_card = [MagicMock()]

        # Test canPutDown method
        self.assertTrue(self.canoe.canPutDown())

        # Test when conditions are not met
        current_player.resource.wood = 1
        self.assertFalse(self.canoe.canPutDown())

        current_player.resource.wood = 3
        current_player.card.put_job_card = []
        self.assertFalse(self.canoe.canPutDown())


if __name__ == '__main__':
    unittest.main()
