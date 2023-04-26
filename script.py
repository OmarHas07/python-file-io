import re
import sys

def read_file(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def find_heritability_words(lines):

    pattern = re.compile(r'\b(heritable|inherit(?:ed|s|ance|ors?|ing|able)?|heritability)\b', re.IGNORECASE)
    results = []

    for index, line in enumerate(lines, start=1):
        matches = pattern.findall(line)
        for match in matches:
            results.append((index, match))

    return results

def write_results(results, output_file):

    with open(output_file, 'w') as file:
        for line_number, word in results:
            file.write(f'{line_number}\t{word}\n')

def main():
    input_file = 'origin.txt'
    output_file = 'heritability_results.txt'
    lines = read_file(input_file)
    results = find_heritability_words(lines)
    write_results(results, output_file)

if __name__ == '__main__':
    main()
