print(type(login), login)
        banco.cursor.execute('SELECT COUNT(*) FROM cliente WHERE login = ?', (login,))
        if banco.cursor.fetchall()[0] > 0:
            raise ValueError("Login já existe. Escolha outro login.")