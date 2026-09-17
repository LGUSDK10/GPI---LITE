import os
import tempfile
import unittest
from pathlib import Path

import programa


class TestPrograma(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_file = Path(self.temp_dir.name) / "dados.json"
        programa.ARQUIVO_DADOS = self.temp_file

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_carregar_problemas_vazio(self):
        self.assertEqual(programa.carregar_problemas(), [])

    def test_adicionar_problema_salva_no_arquivo(self):
        problema = programa.adicionar_problema("Ana", "Hardware", "Sala de aula", "Simples")

        self.assertEqual(problema["id"], 1)
        self.assertEqual(programa.carregar_problemas()[0]["nome"], "Ana")

    def test_pesquisar_problemas_por_nome(self):
        programa.adicionar_problema("Bruno", "Software", "Laboratório de Redes", "Médio")

        resultados = programa.pesquisar_problemas("bruno")

        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0]["nome"], "Bruno")


if __name__ == "__main__":
    unittest.main()
