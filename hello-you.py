import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--your-name')
    args = parser.parse_args()

    operator_name = args.your-name
    
    print("Hello ", operator_name, "!")
    print("For more information on Itential Automation Service, check out:")
    print("https://docs.itential.com/itential-cloud/docs/announcements")

if __name__ == "__main__":
    main()
