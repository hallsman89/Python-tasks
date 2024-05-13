from constants.constants import NAMES, FIRST_NAMES, LAST_NAMES, RANKS
import proto.galaxy_pb2 as pb2
import proto.galaxy_pb2_grpc as pb2_grpc
from typing import Iterable
import random
from concurrent import futures

import grpc


class Galaxy(pb2_grpc.GalaxyService):
    def get_ships(
        self, request: pb2.GalacticCoordinates, context: grpc.ServicerContext
    ) -> Iterable[pb2.Ship]:
        print(f"Coordinates: {request.coords}")
        for _ in range(random.randint(1, 10)):
            length_range = random.choice([(80, 250), (300, 4000), (5000, 20000)])
            length = random.uniform(length_range[0], length_range[1])
            crew_size_range = random.choice([(4, 30), (50, 80), (120, 250), (300, 500)])
            crew_size = random.randint(crew_size_range[0], crew_size_range[1])
            ship: pb2.Ship = pb2.Ship(
                alignment=random.randint(0, 1),
                name=random.choice(NAMES),
                length=length,
                ship_class=random.randint(0, 5),
                crew_size=crew_size,
                armed=random.choice([True, False]),
            )
            min_officers: int = 0 if ship.alignment == "Enemy" else 1
            for _ in range(random.randint(min_officers, 10)):
                officer: pb2.Ship.Officer = ship.officers.add()
                officer.first_name = random.choice(FIRST_NAMES)
                officer.last_name = random.choice(LAST_NAMES)
                officer.rank = random.choice(RANKS)
            yield ship


def server() -> None:
    server: grpc.Server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GalaxyServiceServicer_to_server(Galaxy(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    server()
