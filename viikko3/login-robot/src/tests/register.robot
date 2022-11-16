*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  simo  simo123
    Output Should Contain  New user registered

# Register With Already Taken Username And Valid Password
# ...

# Register With Too Short Username And Valid Password
# ...

# Register With Valid Username And Too Short Password
# ...

# Register With Valid Username And Long Enough Password # Containing Only Letters
# ...

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command