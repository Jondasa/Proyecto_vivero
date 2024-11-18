from django.test import TestCase

from vivero.models import Finca, Productor

# Pruebas para el modelo Productor
class ProductorModelTest(TestCase):

    def setUp(self):
        self.productor = Productor.objects.create(
            documento_identidad="123456789",
            nombre="Juan",
            apellido="Pérez",
            telefono="3001234567",
            correo="juan.perez@example.com"
        )

    def test_crear_productor(self):
        """Verifica que se puede crear un Productor correctamente"""
        self.assertEqual(self.productor.nombre, "Juan")
        self.assertEqual(self.productor.apellido, "Pérez")

    def test_documento_unico(self):
        """Verifica que el documento de identidad es único"""
        with self.assertRaises(Exception):
            Productor.objects.create(
                documento_identidad="123456789",  # Mismo documento
                nombre="Ana",
                apellido="Gómez",
                telefono="3109876543",
                correo="ana.gomez@example.com"
            )

    def test_string_representation(self):
        """Verifica la representación en string del Productor"""
        self.assertEqual(str(self.productor), "Juan Pérez")

# Pruebas para el modelo Finca
class FincaModelTest(TestCase):

    def setUp(self):
        self.productor = Productor.objects.create(
            documento_identidad="987654321",
            nombre="Ana",
            apellido="Gómez",
            telefono="3109876543",
            correo="ana.gomez@example.com"
        )
        self.finca = Finca.objects.create(
            numero_catastro="123ABC",
            municipio="Bogotá",
            productor=self.productor
        )

    def test_crear_finca(self):
        """Verifica que se puede crear una Finca correctamente"""
        self.assertEqual(self.finca.municipio, "Bogotá")
        self.assertEqual(self.finca.productor, self.productor)

    def test_numero_catastro_unico(self):
        """Verifica que el número de catastro es único"""
        with self.assertRaises(Exception):
            Finca.objects.create(
                numero_catastro="123ABC",  # Mismo número de catastro
                municipio="Medellín",
                productor=self.productor
            )

    def test_string_representation(self):
        """Verifica la representación en string de la Finca"""
        self.assertEqual(str(self.finca), "Finca 123ABC - Bogotá")