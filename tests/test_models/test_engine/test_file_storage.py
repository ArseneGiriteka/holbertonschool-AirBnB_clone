#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open('file.json', 'r') as file:
            self.assertIn(obj.id, file.read())

    def test_reload(self):
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)