import pandas as pd


# find ground truth bug line
def find_bug_line(code, correct_code):

    code_lines = code.split("\n")
    correct_lines = correct_code.split("\n")

    for i in range(min(len(code_lines), len(correct_lines))):
        if code_lines[i] != correct_lines[i]:
            return i + 1

    return None


def evaluate():

    dataset = pd.read_csv("C:/Users/chait/Downloads/infineon/samples.csv")
    predictions = pd.read_csv("output.csv")

    dataset = dataset.sort_values("ID").reset_index(drop=True)
    predictions = predictions.sort_values("ID").reset_index(drop=True)

    total = len(predictions)
    correct = 0

    for i in range(total):

        code = dataset.loc[i, "Code"]
        correct_code = dataset.loc[i, "Correct Code"]

        actual_bug_line = find_bug_line(code, correct_code)

        predicted_bug_line = predictions.loc[i, "Bug Line"]

        try:
            predicted_bug_line = int(str(predicted_bug_line).split(",")[0])
        except:
            predicted_bug_line = None

        if predicted_bug_line == actual_bug_line:
            correct += 1

    accuracy = (correct / total) * 100

    print("=================================")
    print("Evaluation Results")
    print("=================================")
    print(f"Total Samples: {total}")
    print(f"Correct Predictions: {correct}")
    print(f"Accuracy: {accuracy:.2f}%")
    print("=================================")


if __name__ == "__main__":
    evaluate()