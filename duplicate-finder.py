import pandas as pd
import math

df = pd.read_excel("input.xlsx")

output_lines = []
duplicate_count = 0

while df.first_valid_index() != None:
    comparator_index = df.first_valid_index()

    comparator_tail = df.iloc[comparator_index]["Tail"]
    comparator_date = df.iloc[comparator_index]["Event Date"]
    comparator_flight = df.iloc[comparator_index]["Flight"]

    matched_indexes = df.loc[(df["Tail"] == comparator_tail) & (
        df["Event Date"] == comparator_date) & (df["Flight"] == comparator_flight)].index

    if len(matched_indexes) > 1:
        duplicate_count += 1

        title = "{}. POSSIBLE DUPLICATE\n".format(
            duplicate_count)
        output_lines.append(title)

        for match in matched_indexes:

            event_number = df.iloc[match]["Event Number"]
            event_month = df.iloc[match]["Event Date"].month
            event_day = df.iloc[match]["Event Date"].day
            event_year = df.iloc[match]["Event Date"].year
            event_flight = df.iloc[match]["Flight"]
            event_tail = df.iloc[match]["Tail"]
            event_summary = df.iloc[match]["Event Summary"]

            line = "{}\t{}/{}/{}\t{}\t{}\t{}\n".format(
                event_number, event_month, event_day, event_year, str(math.floor(event_flight)), event_tail, event_summary)
            output_lines.append(line)

        output_lines.append("\n")

        df = df.drop(matched_indexes)
    else:
        df = df.drop(comparator_index)

    df = df.reset_index(drop=True)

    with open("output.txt", "+w") as f:
        f.writelines(output_lines)
