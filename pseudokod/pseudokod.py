# Navigationssystem

def navigation_system(activate: bool):
    while activate:
        sensor_data = read_sensor_data()
        communication_data = read_communication_data()
        decision = navigation_control(sensor_data, communication_data)
        send_decision_data(decision)
        send_communication_data(sensor_data, decision)


def navigation_control(sensor_data, communication_data):
    explore: bool
    autonomous: bool
    decision: str
    autonomous = communication_data
    laptop_command = communication_data
    if autonomous:
        if explore:
            decision = "explore"
            return decision
        else:
            decision = "navigate"
            return decision
    else:
        return laptop_command


def read_sensor_data():
    pass


def read_communication_data():
    pass


def send_decision_data(sensor_data, decision):
    pass


def send_communication_data():
    pass


# Laptop
def laptop():
    manual_control: bool
    while True:
        read_laptop_com_data()
        draw_ui()
        if manual_control:
            make_navigation_decision()
        send_laptop_com_data()


def read_laptop_com_data():
    pass


def draw_ui():
    pass


def make_navigation_decision():
    pass


def send_laptop_com_data():
    pass


# Sensorsystem
def sensor_system():
    while True:
        disable_interrupts()
        read_raw_sensor_data()
        convert_data_to_SI()
        enable_interrupts()


def disable_interrupts():
    pass


def enable_interrupts():
    pass


def read_raw_sensor_data():
    pass


def convert_data_to_SI():
    pass


def send_SI_data():
    pass


# Styrsystem
def control_system():
    while True:
        command, data = read_navigation_data()
        automatic_control(data, command)
        execute_navigation_command(command)


def automatic_control(data, command):
    if command == "forward":
        pid_regulate(data)


def pid_regulate():
    pass


def read_navigation_data():
    pass




def execute_navigation_command():
    pass


# Kommunikationssystem
def communication_system():
    send_sensor_data()
    manual_command = receive_communication_data()
    if manual_command:
        send_communication_data()


def send_sensor_data():
    pass


def receive_communication_data():
    pass
