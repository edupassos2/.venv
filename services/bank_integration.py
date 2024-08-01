import requests

def fetch_bank_transactions(user_id):
    # Supondo que exista um token de autenticação armazenado para o usuário
    access_token = 'user_access_token'  # Obtido do banco de dados ou serviço de autenticação

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get('https://api.bank.com/transactions', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch transactions'}
