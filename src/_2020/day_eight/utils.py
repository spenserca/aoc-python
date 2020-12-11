class HandheldGame:
    def __init__(self, boot_code: [str]):
        self.boot_code = boot_code
        self.processed_instructions = []
        self.accumulator = 0
        self.current_instruction = 0
        self.current_operation = ''
        self.current_arg = 0
        self.terminated = False

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
        self.current_instruction += self.current_arg

    def handle_nop_instruction(self):
        self.current_instruction += 1

    def get_current_instruction(self):
        self.add_processed_instruction(self.current_instruction)
        return self.boot_code[self.current_instruction]

    def run_game(self):
        while self.current_instruction not in self.processed_instructions and not self.terminated:
            self.process_instruction()

        return self.accumulator

    def process_instruction(self):
        instruction = self.get_current_instruction()
        self.parse_instruction(instruction)
        if self.current_operation == 'acc':
            self.handle_acc_instruction()
        elif self.current_operation == 'jmp':
            self.handle_jmp_instruction()
        elif self.current_operation == 'nop':
            self.handle_nop_instruction()
        if self.current_instruction >= len(self.boot_code):
            self.terminated = True


def get_accumulator_value_after_one_loop(boot_code: [str]):
    handheld_game = HandheldGame(boot_code)

    return handheld_game.run_game()


def get_accumulator_value_after_termination(boot_code: [str]):
    i = 0
    while i <= len(boot_code):
        instruction = boot_code[i]
        original_op, arg = instruction.split(' ')
        modified_op = 'acc'
        if original_op == 'nop':
            modified_op = 'jmp'
        elif original_op == 'jmp':
            modified_op = 'nop'

        boot_code[i] = modified_op + ' ' + arg

        handheld_game = HandheldGame(boot_code)

        handheld_game.run_game()

        if handheld_game.terminated:
            return handheld_game.accumulator

        boot_code[i] = instruction
        i += 1
