import os
import json
from mock import patch
from telebot import types
from src import erase


def test_read_json():
    """This is the test function for read json"""
    try:
        if not os.path.exists('./test/dummy_expense_record.json'):
            with open('./test/dummy_expense_record.json', 'w') as json_file:
                json_file.write('{}')
            return json.dumps('{}')
        elif os.stat('./test/dummy_expense_record.json').st_size != 0:
            with open('./test/dummy_expense_record.json') as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")


def create_message(text):
    """This is the create message function"""
    params = {'messagebody': text}
    chat = types.User("894127939", False, 'test')
    return types.Message(1, None, None, chat, 'text', params, "")


# @patch('telebot.telebot')
# def test_delete_run_with_data(mock_telebot, mocker):
#     MOCK_USER_DATA = test_read_json()
#     mocker.patch.object(erase, 'helper')
#     erase.helper.read_json.return_value = MOCK_USER_DATA
#     print("Hello", MOCK_USER_DATA)
#     erase.helper.write_json.return_value = True
#     mock_message_data = create_message("Hello")

#     mc = mock_telebot.return_value
#     mc.send_message.return_value = True
#     erase.run(mock_message_data, mc)
#     assert(erase.helper.write_json.called)


@patch('telebot.telebot')
def test_delete_with_no_data(mock_telebot, mocker):
    """This is the test function for delete with no data method"""
    mocker.patch.object(erase, 'helper')
    # erase.helper.read_json.return_value = {}
    # erase.helper.write_json.return_value = True
    mock_message_data = create_message("Hello")
    mock_value = mock_telebot.return_value
    mock_value.send_message.return_value = True
    erase.run(mock_message_data, mock_value)
    # if erase.helper.write_json.called is False:
    #     assert True
