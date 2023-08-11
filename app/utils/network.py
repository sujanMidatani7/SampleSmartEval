from asyncio import Semaphore
from typing import Optional
from aiohttp import ClientSession


class Network:
    """
    Singleton class for aiohttp session
    """
    _instance: Optional["Network"] = None
    session: ClientSession
    semaphore: Semaphore  # for threadpools if needed

    def __new__(cls):
        if cls._instance is None:
            instance = super(Network, cls).__new__(cls)
            instance.session = ClientSession()
            instance.semaphore = Semaphore(10)
            cls._instance = instance
        return cls._instance
