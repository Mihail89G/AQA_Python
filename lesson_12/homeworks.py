
def validate_new_user(record):
    """Перевіряє дані нового користувача.словник з ключами 'id', 'email', 'age', 'balance', 'password'  """
    id_valid = isinstance(record.get('id'), int) and record['id'] > 0
    email_valid = isinstance(record.get('email'), str) and '@' in record['email']
    age_valid = isinstance(record.get('age'), int) and 18 <= record['age'] <= 120
    balance_valid = isinstance(record.get('balance'), (int, float)) and record['balance'] >= 0
    password_valid = isinstance(record.get('password'), str) and 6 <= len(record['password']) <= 20

    all_valid = all([id_valid, email_valid, age_valid, balance_valid, password_valid])

    return {
        'id_valid': id_valid,
        'email_valid': email_valid,
        'age_valid': age_valid,
        'balance_valid': balance_valid,
        'password_valid': password_valid,
        'all_valid': all_valid
    }

    #print("Validation result:", result)
    #return result

#user = {'id': 1, 'email': 'user@example.com', 'age': 30, 'balance': 100, 'password': 'secret123'}
#validate_new_user(user)