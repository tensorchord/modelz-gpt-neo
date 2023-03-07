import torch
from transformers import pipeline
from mosec import Server, Worker


class Inference(Worker):
    def __init__(self) -> None:
        device = torch.cuda.current_device() if torch.cuda.is_available() else "cpu"
        self.model = pipeline(
            "text-generation", model="EleutherAI/gpt-neo-1.3B", device=device
        )

    def forward(self, data):
        res = self.model(data, do_sample=True, max_length=200)
        return [text[0]["generated_text"] for text in res]

    def deserialize(self, data: bytes) -> str:
        return data.decode()

    def serialize(self, data: str) -> bytes:
        return data.encode()


if __name__ == "__main__":
    server = Server()
    server.append_worker(Inference, max_batch_size=16, max_wait_time=20, num=1)
    server.run()
