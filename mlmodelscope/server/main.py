import ray
from ray import serve

from io import BytesIO
from PIL import Image

import torch
from torchvision import transforms
from torchvision.models import resnet18


# Starts a head-node for the cluster.
ray.init(address='auto', namespace='serve')


@serve.deployment(
    route_prefix="/image_predict",
    ray_actor_options={"num_gpus": 2.0})
class ImageModel:
    def __init__(self) -> None:
        self.model = resnet18(pretrained=True).eval().cuda()
        self.preprocessor = transforms.Compose(
            [
                transforms.Resize(224),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                # remove alpha channel
                transforms.Lambda(lambda t: t[:3, ...]),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )
        self.postprocessor = torch.nn.Softmax(dim=1)

    async def __call__(self, starlette_request):
        image_payload_bytes = await starlette_request.body()
        pil_image = Image.open(BytesIO(image_payload_bytes))
        print("[1/3] Parsed image data: {}".format(pil_image))

        pil_images = [pil_image]  # Our current batch size is one
        input_tensor = torch.cat(
            [self.preprocessor(i).unsqueeze(0) for i in pil_images]
        )
        print("[2/3] Images transformed, tensor shape {}".format(
            input_tensor.shape))

        with torch.no_grad():
            output_tensor = self.model(input_tensor.cuda())
        print("[3/3] Inference done!")
        return {"class_index": int(torch.argmax(output_tensor[0]))}


ImageModel.deploy()
