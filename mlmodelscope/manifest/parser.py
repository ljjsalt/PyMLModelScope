import yaml
from yaml import safe_load


def parse_manifest(manifest_path):
    with open(manifest_path, "r") as stream:
        try:
            model_manifest = (safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)
    return model_manifest


if __name__ == "__main__":
    parse_manifest("../../example/resnet.yml")
