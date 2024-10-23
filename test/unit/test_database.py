import database

from unittest.mock import patch

def test_is_database_up_should_return_true_if_database_is_accessible():
    with patch.object(database, 'SessionLocal') as mocked_session_local:
        assert database.is_database_up() is True
        mocked_session_local.return_value.execute.assert_called_once()


def test_is_database_up_should_return_false_if_some_exception_is_raised():
    with patch.object(database, 'SessionLocal') as mocked_session_local:
        mocked_session_local.return_value.execute.side_effect = Exception()
        
        assert database.is_database_up() is False
        mocked_session_local.return_value.execute.assert_called_once()
