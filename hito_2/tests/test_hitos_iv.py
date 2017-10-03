#!/bib/bash
"""Modulo de test para el archivo hitos_iv.py."""

import unittest
# import sys
import hitos_iv


class HitosIvTest(unittest.TestCase):
    """Clase para testing del modulo hitos_iv."""

    def test_milestone_number(self):
        """Test para obtenerr numero de hitos."""
        self.assertEqual(hitos_iv.milestone_number(), 2,
                         "Número correcto de hitos")


if __name__ == '__main__':
    unittest.main()
