from unittest import TestCase
from src.infra.database import make_migrations

class TestMigrationSchema(TestCase):

    def test_migration_schema(self):

        make_migrations()

        self.assertTrue(True)