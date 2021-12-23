import PySimpleGUI as sg
import email_interface

sg.theme('Black')

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter your email address:"), sg.Input(key='-EMAIL_ADDRESS-', do_not_clear=True, size=(10, 1))],
          # "RADIO" makes the radio buttons part of the same group, so when you click one, the other will be unchecked
          [sg.Multiline("", do_not_clear=True, key = '-MESSAGE-')],

          [sg.Button('Send Email'), sg.Exit()]
]

window = sg.Window('Python Email Client', layout)



def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-NAME-']) == 0:
        values_invalid.append('Name')
        is_valid = False
    
    if len(values['-EMAIL_ADDRESS-']) == 0:
        values_invalid.append('Passport Number')
        is_valid = False
    
    if '@' not in values['-EMAIL_ADDRESS-']:
        values_invalid.append('Email Address')
        is_valid = False
    
    if len(values['-MESSAGE-']) == 0:
        values_invalid.append('MESSAGE')
        is_valid = False

    result = [is_valid, values_invalid]
    return result

def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Send Email':
        validation_result = validate(values)
        if validation_result[0]:
            email_interface.send_email(values['-MESSAGE-'], values['-EMAIL_ADDRESS-'])
            sg.popup('EMAIL SENT!')
        else:
            error_message = generate_error_message(validation_result[1])
            sg.popup(error_message)
window.close()
