import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a from-scratch neural network.")
    parser.add_argument("--dataset", choices=["xor"], default="xor")
    parser.add_argument("--epochs", type=int, default=1000)
    parser.add_argument("--lr", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=0)
    # TODO: --hidden-sizes, --batch-size, and a path argument for a real dataset
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Hello, welcome to the entry point for my neural network training project")
    # TODO: build rng from args.seed, load data, build Network, fit, then print the loss history summary and final accuracy
    raise NotImplementedError


if __name__ == "__main__":
    main()
