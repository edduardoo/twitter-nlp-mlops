import hydra

@hydra.main(config_path=".", config_name="config")
def app(cfg):
    print(cfg.model_params.max_words)
    print(cfg.model_params.max_len)

if __name__ == "__main__":
    app()