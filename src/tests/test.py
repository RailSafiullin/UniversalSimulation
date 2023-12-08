import pytest
import pygame
from Factory import Factory
from initWindow import InitWindow
from Storage import Storage
from UniversalSimulation import Universal_simulation

def test_init():
    simulation = Universal_simulation()
    assert len(simulation.stars) == 200  # Проверяем, что список звезд содержит 200 элементов по умолчанию

@pytest.fixture(scope="module")
def app():
    app = Factory.create(InitWindow)
    yield app


@pytest.fixture(scope="module")
def storage():
    storage = Storage()
    yield storage


def test_storage_get_version(storage):
    result = storage.get_version()
    type(result) == str


def test_storage_get_help(storage):
    result = storage.get_help()
    type(result) == str
