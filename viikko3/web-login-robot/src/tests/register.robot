*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  simo
    Set Password  simo1234
    Set Password Confirmation  simo1234
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  xd
    Set Password  simo1234
    Set Password Confirmation  simo1234
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  simo
    Set Password  simo1
    Set Password Confirmation  simo1
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  simo
    Set Password  simo1234
    Set Password Confirmation  simo1235
    Submit Credentials
    Register Should Fail With Message  Passwords must match

Login After Successful Registration
    Set Username  simo
    Set Password  simo1234
    Set Password Confirmation  simo1234
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  simo
    Set Password  simo1234
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  si
    Set Password  simo1234
    Set Password Confirmation  simo1234
    Submit Credentials
    Register Should Fail With Message  Username is too short
    Go To Login Page
    Set Username  si
    Set Password  simo1234
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login