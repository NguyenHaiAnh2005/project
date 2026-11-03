"""Exercise the real Streamlit app and its session-state interactions."""

from pathlib import Path
import unittest

from streamlit.testing.v1 import AppTest


class AppTests(unittest.TestCase):
    def setUp(self):
        self.app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / "app.py")).run()

    def test_initial_render(self):
        self.assertEqual(len(self.app.exception), 0)
        self.assertEqual(self.app.session_state["joy"], 0)
        self.assertEqual(len(self.app.button), 2)

    def test_message_changes_and_counter_persists(self):
        previous = self.app.session_state["message"]
        self.app.button[0].click().run()
        self.assertEqual(len(self.app.exception), 0)
        self.assertNotEqual(self.app.session_state["message"], previous)
        self.assertEqual(self.app.session_state["joy"], 1)
        self.app.button[1].click().run()
        self.assertEqual(len(self.app.exception), 0)
        self.assertEqual(self.app.session_state["joy"], 2)

    def test_each_mood_shows_support_without_adding_points(self):
        for mood in self.app.selectbox[0].options:
            self.app.selectbox[0].select(mood).run()
            self.assertEqual(len(self.app.exception), 0)
            self.assertEqual(len(self.app.info), 1)
            self.assertTrue(self.app.info[0].value)
            self.assertEqual(self.app.session_state["joy"], 0)


if __name__ == "__main__":
    unittest.main()
