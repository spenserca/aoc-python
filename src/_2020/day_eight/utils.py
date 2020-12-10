class HandheldGame:
    def __init__(self, boot_code: [str]):
        self.boot_code = boot_code
        self.processed_instructions = []
        self.accumulator = 0
        self.current_instruction = 0
        self.current_operation = ''
        self.current_arg = 0

    def parse_instruction(self, instruction: str):
        op, str_arg = instruction.split(' ')
        self.current_arg = int(str_arg)
        self.current_operation = op

    def add_processed_instruction(self, processed_instruction: int):
        self.processed_instructions.append(processed_instruction)

    def handle_acc_instruction(self):
        self.current_instruction += 1
        self.accumulator += self.current_arg

    def handle_jmp_instruction(self):
        if self.current_arg > 0:
            if self.current_instruction + self.current_arg > len(self.boot_code):
                self.current_instruction = ((self.current_instruction + self.current_arg) - len(self.boot_code)) - 1
            else:
                self.current_instruction += self.current_arg
        if self.current_arg < 0:
            if self.current_instruction + self.current_arg < 0:
                self.current_instruction = len(self.boot_code) - abs(self.current_instruction + self.current_arg)
            else:
                self.current_instruction += self.current_arg

    def handle_nop_instruction(self):
        self.current_instruction += 1

    def get_current_instruction(self):
        self.add_processed_instruction(self.current_instruction)
        return self.boot_code[self.current_instruction]

    def run_game(self):
        instruction = self.get_current_instruction()
        self.parse_instruction(instruction)

        if self.current_operation == 'acc':
            self.handle_acc_instruction()
        elif self.current_operation == 'jmp':
            self.handle_jmp_instruction()
        elif self.current_operation == 'nop':
            self.handle_nop_instruction()


def get_accumulator_value_after_one_loop(boot_code: [str]):
    handheld_game = HandheldGame(boot_code)

    while handheld_game.current_instruction not in handheld_game.processed_instructions:
        handheld_game.run_game()

    return handheld_game.accumulator


def get_accumulator_value_after_termination(boot_code: [str]):
    accumulator = 0
    current_instruction = 0
    terminate_instruction = len(boot_code)
    visited_instructions = []
    toggled_op_instructions = []

    while current_instruction not in visited_instructions:
        instruction = boot_code[current_instruction]
        visited_instructions.append(current_instruction)
        op, str_arg = instruction.split(' ')
        arg = int(str_arg)

        if op == 'acc':
            accumulator += arg
            current_instruction += 1
        elif op == 'jmp':
            if arg > 0:
                if current_instruction + arg > len(boot_code):
                    current_instruction = ((current_instruction + arg) - len(boot_code)) - 1
                else:
                    current_instruction += arg
            if arg < 0:
                if current_instruction + arg < 0:
                    current_instruction = len(boot_code) - abs(current_instruction + arg)
                else:
                    current_instruction += arg
        elif op == 'nop':
            current_instruction += 1

    return accumulator
