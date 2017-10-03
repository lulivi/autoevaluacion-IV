#!/usr/bin/env python
"""Modulo de test para el archivo hitos_iv.py."""

import unittest
import __init__
import hitos_iv


class HitosIvTest(unittest.TestCase):
    """Clase para testing del modulo hitos_iv."""

    def test_read_json(self):
        """Comprueba si lee correctamente el fichero."""
        self.assertFalse(
            hitos_iv.read_json('../hitos.json') == {},
            'Diccionario no vacío')

    def test_milestone_number(self):
        """Test para obtenerr numero de hitos."""
        mil_dict = hitos_iv.read_json('../hitos.json')
        self.assertEqual(
            hitos_iv.milestone_number(mil_dict), 2, "Número correcto de hitos")


if __name__ == '__main__':
    unittest.main()
