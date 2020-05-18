def read_template(path):
    with open(path) as file:
        contents = file.read().strip()
    return contents


def parse_template(template):
    # split the template apart
    # return two things, a stripped string and speech parts as  a tuple

    # A {Adjective} and {Adjective} {Noun}.
    #             ^
    # stripped_string = A {
    # speech_part_in_progress = Adjective
    # can refactor the code to remove/reduce duplicate such as stripped_string += char

    stripped_string = ""
    speech_parts = []
    flag = False
    speech_part_in_progress = ""

    for char in template:
        if char == "{":
            stripped_string += char
            flag = True

        elif char == "}":
            stripped_string += char
            flag = False
            speech_parts.append(speech_part_in_progress)
            speech_part_in_progress = ""

        elif flag:
            speech_part_in_progress += char

        else:
            stripped_string += char

    return stripped_string, tuple(speech_parts)


def merge(stripped_template, responses):
    # merge a string e.g. "A {} and {} {}." and a tuple e.g. ("dark","stormy", "night") into "A dark and stormy night".

    return stripped_template.format(*responses)


def collect_input(parts):
    responses = []
    for part in parts:
        response = input(f"Enter a {part} ")
        responses.append(response)

    return responses


def save_madlib(merged, path):
    with open(path, "w") as f:
        f.write(merged)


def main(path):
    template = read_template(path)

    stripped_template, speech_parts = parse_template(template)

    responses = collect_input(speech_parts)

    merged_string = merge(stripped_template, responses)

    out_path = path.replace(".txt", ".completed.txt")

    save_madlib(merged_string, out_path)


if __name__ == "__main__":
    path = 'input1.txt'
    main (path)

