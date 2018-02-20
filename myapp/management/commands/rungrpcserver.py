from contextlib import contextmanager
from django.core.management.base import BaseCommand, CommandError
from concurrent import futures
from myapp.services.user_service import UserService

import myapp.gen_py.users_pb2_grpc as user_service
import grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


@contextmanager
def serve_forever():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service.add_UsersServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    yield
    server.stop(0)


class Command(BaseCommand):
    help = 'api server'

    def handle(self, *args, **options):
        with serve_forever():
            self.stdout.write(self.style.SUCCESS(
                'Successfully started grpc server '))
            try:
                while True:
                    time.sleep(_ONE_DAY_IN_SECONDS)
            except KeyboardInterrupt:
                pass
