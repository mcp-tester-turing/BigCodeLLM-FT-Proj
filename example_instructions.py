import json

def main():
    # Load the dataset
    with open("data.json", "r") as f:
        dataset = json.load(f)

    # Create a list of instructions
    instructions = []
    for item in dataset:
        instructions.append(f"Given the context '{item['context']}', the answer is '{item['answer']}'.")

    # Save the instructions to a file
    with open("instructions.jsonl", "w") as f:
        for instruction in instructions:
            f.write(json.dumps({"instruction": instruction}) + "\n")

if __name__ == "__main__":
    main()
