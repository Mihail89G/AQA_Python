import logging
from unittest.mock import patch # створив щоб не писати реальний лог файл
import pytest

from homework_logs import log_event


@pytest.mark.parametrize("username,status,expected_level", [
    ("Alice", "success", "info"),
    ("Max", "expired", "warning"),
    ("Karl", "failed", "error"),
    ("Anna", "unknown", "error"),  # тест на неочікуваний статус
])
def test_log_event_logs_correctly(username, status, expected_level):
    expected_message = f"Login event - Username: {username}, Status: {status}"

    with patch("logging.getLogger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value

        log_event(username, status)


        mock_get_logger.assert_called_once_with("log_event")


        if expected_level == "info":
            mock_logger.info.assert_called_once_with(expected_message)
            mock_logger.warning.assert_not_called()
            mock_logger.error.assert_not_called()
        elif expected_level == "warning":
            mock_logger.warning.assert_called_once_with(expected_message)
            mock_logger.info.assert_not_called()
            mock_logger.error.assert_not_called()
        elif expected_level == "error":
            mock_logger.error.assert_called_once_with(expected_message)
            mock_logger.info.assert_not_called()
            mock_logger.warning.assert_not_called()

# запуск з консолі
# python -m pytest -v homework_14.py