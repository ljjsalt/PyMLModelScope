import torch
from torchvision.models import resnet18

import ray

ray.init(address='ray://128.205.43.180:10001')


def get_model(weight):
    model = resnet18(num_classes=10, pretrained=False).eval()
    model.load_state_dict(torch.load(weight))
    return model


@ray.remote(num_gpus=1.0)
def predict(model):
    model = model.cuda()
    for _ in range(100):
        input_tensor = torch.randn(1, 3, 224, 224)
    output_tensor = model(input_tensor.cuda())
    return output_tensor.cpu()


if __name__ == '__main__':
    model_ref = ray.put(get_model('./model.pth'))
    output_ref = predict.remote(model_ref)
    print(ray.get(output_ref))
