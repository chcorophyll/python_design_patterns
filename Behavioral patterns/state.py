"""
references:
https://github.com/youngsterxyf/mpdp-code
https://sourcemaking.com/design_patterns/creational_patterns
"""


from state_machine import State, Event, acts_as_state_machine
from state_machine import after, before, InvalidStateTransition


RUNNING = "running"
WAITING = "waiting"
BLOCKED = "blocked"
TERMINATED = "terminated"


@acts_as_state_machine
class Process(object):

    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    wait = Event(from_states=(created, running, blocked, swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked), to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    @after("wait")
    def wait_info(self):
        print("{} entered waiting mode".format(self.name))

    @after("run")
    def run_info(self):
        print("{} is running".format(self.name))

    @before("terminate")
    def terminate_info(self):
        print("{} terminated".format(self.name))

    @after("block")
    def block_info(self):
        print("{} is blocked".format(self.name))

    @after("swap_wait")
    def swap_wait_info(self):
        print("{} is swapped out and waiting".format(self.name))

    @after("swap_block")
    def swap_block_info(self):
        print("{} is swapped out and blocked".format(self.name))


def transition(process, event, event_name):
    try:
        event()
    except InvalidStateTransition as e:
        print("Error: transition of {} from {} to {} failed".format(process.name, process.current_state, event_name))


def state_info(process):
    print("state of {}: {}".format(process.name, process.current_state))


def main():
    p_0, p_1 = Process("process_0"), Process("process_1")
    [state_info(p) for p in (p_0, p_1)]
    print("****************")
    transition(p_0, p_0.wait, WAITING)
    transition(p_1, p_1.terminate, TERMINATED)
    [state_info(p) for p in (p_0, p_1)]
    print("****************")
    transition(p_0, p_0.run, RUNNING)
    transition(p_1, p_1.wait, WAITING)
    [state_info(p) for p in (p_0, p_1)]
    print("****************")
    transition(p_1, p_1.run, RUNNING)
    [state_info(p) for p in (p_0, p_1)]
    print("****************")
    [transition(p, p.block, BLOCKED) for p in (p_0, p_1)]
    [state_info(p) for p in (p_0, p_1)]
    print("****************")
    [transition(p, p.terminate, TERMINATED) for p in (p_0, p_1)]
    [state_info(p) for p in (p_0, p_1)]


if __name__ == "__main__":
    main()



