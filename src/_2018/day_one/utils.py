def get_output_frequency(frequency_changes: [str]):
    return sum(map(int, frequency_changes), 0)
