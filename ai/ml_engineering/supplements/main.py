import hydra


@hydra.main(
    config_path="./",
    config_name="config.yaml",
    # version_base=None
)
def hello(cfg):
    return cfg


if __name__ == "__main__":
    hello()
