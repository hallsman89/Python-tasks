from voight_kampff import VoightKampff


def main() -> None:
    test: VoightKampff = VoightKampff("./questions/questions_en.json")
    test.run()


if __name__ == "__main__":
    main()
