from estruturas.hash_table.hash_table import HashTable


def test_insert_and_search():
    table = HashTable(5)

    table.inserir("Caio", 22)

    assert table.buscar("Caio") == 22


def test_search_nonexistent_key():
    table = HashTable(5)

    assert table.buscar("Lucas") is None


def test_update_existing_key():
    table = HashTable(5)

    table.inserir("Vinicius", 25)
    table.inserir("Vinicius", 60)

    assert table.buscar("Vinicius") == 60


def test_remove_existing_key():
    table = HashTable(5)

    table.inserir("Pedro", 31)

    assert table.remover("Pedro") is True
    assert table.buscar("Pedro") is None


def test_remove_nonexistent_key():
    table = HashTable(5)

    assert table.remover("Carlos") is False


